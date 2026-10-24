import test from 'node:test';
import assert from 'node:assert/strict';
import {visibleRunRange, fontSizeIssues} from '../skills/southbrook-brand-artifact-stylist/scripts/native_text_ranges.mjs';

test('includes the last letter whether or not a newline is returned', () => {
  for (const content of ['Share', 'Share\n']) {
    assert.deepEqual(visibleRunRange({startIndex:3,endIndex:3+content.length,textRun:{content}},'t.0'),
      {startIndex:3,endIndex:8,tabId:'t.0'});
  }
});
test('handles one letter, punctuation, meaningful spaces and UTF-16 emoji', () => {
  for (const [content,length] of [['A',1],['Go!',3],['Go  ',4],['Pray 🙏',7]]) {
    assert.equal(visibleRunRange({startIndex:9,textRun:{content}}).endIndex,9+length);
  }
  assert.equal(visibleRunRange({startIndex:9,textRun:{content:'\n'}}),null);
});
test('rejects an opaque element or a range that exceeds its native extent', () => {
  assert.throws(() => visibleRunRange({startIndex:1,inlineObjectElement:{}}));
  assert.throws(() => visibleRunRange({startIndex:1,endIndex:3,textRun:{content:'Share'}}));
});
test('detects a single smaller trailing letter and accepts a corrected paragraph', () => {
  const paragraph = {elements:[
    {startIndex:1,endIndex:5,textRun:{content:'Shar',textStyle:{fontSize:{magnitude:22}}}},
    {startIndex:5,endIndex:6,textRun:{content:'e',textStyle:{fontSize:{magnitude:10}}}},
    {startIndex:6,endIndex:7,textRun:{content:'\n',textStyle:{}}}
  ]};
  assert.equal(fontSizeIssues(paragraph,22,'t.0').length,1);
  paragraph.elements[1].textRun.textStyle.fontSize.magnitude=22;
  assert.deepEqual(fontSizeIssues(paragraph,22,'t.0'),[]);
});
