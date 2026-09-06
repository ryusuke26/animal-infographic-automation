"""Regressions for text limits, explanatory cards and safe sidecar derivation."""

from pathlib import Path
import sys
import subprocess
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from x_text import count_post
from validate_package import parse_locked_copy, validate_prompt_lock
from validate_x_post_format import validate_file, validate_post_length
from sync_posting_sidecars import sync


COPY = """Copy format: cards-v2
Title: {title}
Scientific name: *Testus specimen*

Observation cards:
1. Heading: First discovery
   Explanation: First explanation.
2. Heading: Second discovery
   Explanation: Second explanation.
3. Heading: Third discovery
   Explanation: Third explanation.

Footer/status:
IUCN Red List 2026: Test footer
"""


def make_package(root: Path) -> Path:
    package = root / "2026-09-06-test-species"
    (package / "images").mkdir(parents=True)
    for lang, word, title in (("ja", "japanese", "テスト種"), ("en", "english", "Test Species")):
        copy = package / f"infographic-copy-{lang}.md"
        copy.write_text(COPY.format(title=title), encoding="utf-8")
        lines = parse_locked_copy(copy, [])
        (package / f"image-prompt-{lang}.md").write_text(
            'Text, verbatim:\n' + '\n'.join('"' + line + '"' for line in lines) + '\n', encoding="utf-8"
        )
        main = f"A surprising discovery.\n{title}\nTestus specimen\n\nIUCN Red List 2026: Test footer\n#TestSpecies"
        story = "Two connected observations."
        if lang == "ja":
            story += "\n\nそれがテスト種の、ちょっと不思議な暮らし。"
        source = ("出典メモ：" if lang == "ja" else "Source note:") + " https://example.org/evidence"
        blocks = zip(("Main post", "Story reply", "ALT text", "Source/context reply"),
                     (main, story, "A test poster.", source))
        (package / f"x-post-{lang}.md").write_text(
            '\n'.join(f"## {name}\n\n```text\n{text}\n```\n" for name, text in blocks), encoding="utf-8"
        )
        # Sidecar routing needs a selected path; image decoding is tested by package QA.
        (package / "images" / f"test_{word}_posting_2026-09-06.png").touch()
    return package


class XCountTests(unittest.TestCase):
    def test_official_weighting(self):
        cases = {"あ" * 200: 400, "a" * 275: 275, "あいうabc": 9,
                 "👨‍👩‍👧‍👦": 2, "🙋🏽": 2, "🇯🇵": 2, "e\u0301": 1,
                 "https://example.com/" + "a" * 300: 23}
        for value, expected in cases.items():
            with self.subTest(value=value[:20]):
                self.assertEqual(count_post(value)[0], expected)

    def test_budget_and_invalid_characters(self):
        path = Path("2026-09-06-test/x-post-ja.md")
        self.assertTrue(validate_post_length(path, "あ" * 200, "main post"))
        self.assertFalse(validate_post_length(path, "a" * 275, "main post"))
        self.assertTrue(validate_post_length(path, "a" * 276, "main post"))
        self.assertTrue(validate_post_length(path, "bad\ufffe", "main post"))


class CopyAndSyncTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.package = make_package(Path(self.temp.name))

    def test_new_copy_and_prompt_pair(self):
        errors = []
        lines = parse_locked_copy(self.package / "infographic-copy-ja.md", errors)
        self.assertEqual(len(lines), 9)
        validate_prompt_lock(self.package, errors)
        self.assertEqual(errors, [])

    def test_new_format_passes_pre_image_package_command(self):
        (self.package / "README.md").write_text(
            "Workflow mode: Quality Run\nEditorial classification group: Plants\n", encoding="utf-8"
        )
        (self.package / "sources-qa.md").write_text(
            "IUCN check: test fixture only\n", encoding="utf-8"
        )
        result = subprocess.run(
            [sys.executable, "-B", str(Path(__file__).resolve().parents[1] / "validate_package.py"),
             str(self.package), "--pre-image", "--skip-git"],
            capture_output=True, text=True, encoding="utf-8", timeout=30,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_missing_or_reordered_explanation_rejected(self):
        path = self.package / "infographic-copy-ja.md"
        original = path.read_text(encoding="utf-8")
        for invalid in (original.replace("   Explanation: First explanation.\n", ""),
                        original.replace("2. Heading:", "3. Heading:"),
                        original.replace("First explanation.", " ")):
            path.write_text(invalid, encoding="utf-8")
            errors = []
            self.assertEqual(parse_locked_copy(path, errors), [])
            self.assertTrue(errors)

    def test_explanation_mismatch_rejected(self):
        path = self.package / "image-prompt-ja.md"
        path.write_text(path.read_text(encoding="utf-8").replace("First explanation.", "Changed claim."), encoding="utf-8")
        errors = []
        validate_prompt_lock(self.package, errors)
        self.assertTrue(errors)

    def test_old_labels_still_supported(self):
        path = self.package / "infographic-copy-ja.md"
        path.write_text("Title: Test\nScientific name: *Testus specimen*\nObservation labels:\n1. A\n2. B\n3. C\nFooter/status:\nStatus\n", encoding="utf-8")
        errors = []
        self.assertEqual(parse_locked_copy(path, errors), ["Test", "Testus specimen", "A", "B", "C", "Status"])
        self.assertEqual(errors, [])

    def test_source_reply_limit_for_new_format(self):
        path = self.package / "x-post-en.md"
        path.write_text(path.read_text(encoding="utf-8").replace("Source note:", "Source note:" + "a" * 300), encoding="utf-8")
        self.assertTrue(any("source/context reply" in error for error in validate_file(path, "Source note:", language="en")))

    def test_sync_check_write_idempotence_and_crlf(self):
        path = self.package / "x-post-ja.md"
        path.write_bytes(path.read_bytes().replace(b"\n", b"\r\n"))
        self.assertEqual(len(sync(self.package)), 8)
        self.assertEqual(list((self.package / "images").glob("*.txt")), [])
        self.assertEqual(len(sync(self.package, write=True)), 8)
        before = {p: p.stat().st_mtime_ns for p in (self.package / "images").glob("*.txt")}
        self.assertEqual(sync(self.package, write=True), [])
        self.assertEqual(before, {p: p.stat().st_mtime_ns for p in before})

    def test_invalid_second_language_prevents_all_writes(self):
        (self.package / "x-post-en.md").write_text("invalid", encoding="utf-8")
        with self.assertRaises(ValueError):
            sync(self.package, write=True)
        self.assertEqual(list((self.package / "images").glob("*.txt")), [])

    def test_ambiguous_selected_image_prevents_writes(self):
        (self.package / "images" / "other_japanese_posting.png").touch()
        with self.assertRaises(ValueError):
            sync(self.package, write=True)
        self.assertEqual(list((self.package / "images").glob("*.txt")), [])


if __name__ == "__main__":
    unittest.main()
