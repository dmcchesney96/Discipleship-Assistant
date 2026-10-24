// Google Docs indexes count UTF-16 code units; JavaScript string.length does too.
// Accept an actual textRun, never an ambiguously normalized paragraph endIndex.
export function visibleRunRange(element, tabId) {
  if (!element.textRun || !Number.isInteger(element.startIndex)) throw new Error('Expected indexed textRun');
  const text = element.textRun.content.replace(/\n$/, '');
  if (!text.length) return null;
  const endIndex = element.startIndex + text.length;
  if (element.endIndex != null && endIndex > element.endIndex) throw new Error('Text exceeds native range');
  return {startIndex: element.startIndex, endIndex, ...(tabId ? {tabId} : {})};
}

export function paragraphRanges(paragraph, tabId) {
  return paragraph.elements.filter(e => e.textRun).map(e => visibleRunRange(e, tabId)).filter(Boolean);
}

// Check every visible run against the intended paragraph size, including its
// final character. A mismatch must be repaired or explicitly justified before save.
export function fontSizeIssues(paragraph, expectedSize, tabId) {
  return paragraph.elements.filter(e => e.textRun && e.textRun.content.replace(/\n$/, '').length)
    .flatMap(e => e.textRun.textStyle?.fontSize?.magnitude === expectedSize ? [] : [{
      range: visibleRunRange(e, tabId), text: e.textRun.content,
      expectedSize, actualSize: e.textRun.textStyle?.fontSize?.magnitude ?? null
    }]);
}
