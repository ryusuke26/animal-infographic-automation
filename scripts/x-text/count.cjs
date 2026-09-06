// Use the official parser: NFC, URL shortening, CJK and emoji sequences.
const fs = require('node:fs');
const { parseTweet } = require('twitter-text');
const texts = JSON.parse(fs.readFileSync(0, 'utf8'));
if (!Array.isArray(texts) || texts.some(text => typeof text !== 'string')) {
  throw new Error('Expected a JSON array of strings');
}
process.stdout.write(JSON.stringify(texts.map(text => {
  const result = parseTweet(text);
  return { weightedLength: result.weightedLength, valid: result.valid };
})));
