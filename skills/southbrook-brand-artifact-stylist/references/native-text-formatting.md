# Native text ranges and trailing-character QA

A live formatting failure left each paragraph's last visible character at its previous font size. The cause was subtracting one from an endpoint that already excluded the newline. Raw Google Docs paragraph endpoints generally include the paragraph delimiter; a connector's normalized text endpoints may exclude it. Do not assume these representations have identical semantics.

For native Google Docs branding:

1. Read indexed native text runs, the actual tab, and revision. Use [native_text_ranges.mjs](../scripts/native_text_ranges.mjs) to compute each visible run's exclusive end as `startIndex + visibleText.length` in JavaScript (UTF-16). Exclude an actual final newline only when it is present. Never blindly subtract one, trim meaningful spaces, or use Unicode code-point counts. Preserve inline objects and native controls; text-only helpers must not flatten them.
2. Apply named paragraph styles before explicit character styling. Apply the intended family/size/color through every visible run. Preserve links, emphasis, list identity, citations, exact wording and approval status. Inserts shift subsequent positions: calculate the shift or insert the identity header after existing ranges are styled. Guard writes with the current revision.
3. Read the result back once. Check all visible runs against the intended size for their paragraph, using `fontSizeIssues`; missing/inherited sizes need resolution against the actual named/default styles. Verify the final visible letter and punctuation, not only the first run. Check family, weight, color and link ranges as well. Intentional superscripts or mixed-size content need explicit exceptions, not automatic normalization.
4. Compare exact text and the ordered linked labels/targets before and after. For a formatting-only backlog, the only permitted text difference is the new blank identity-header paragraph where a logo was added; do not rewrite wording or numbering. Keep existing Drive IDs and parents.
5. Export/render where images or pagination matter. Inspect titles, wrapped lines, last letters, headings, page breaks and final pages. A successful API response or native-style audit is not visual QA. Repair and recheck any failures before declaring completion; disclose any remaining visual coverage limit.

Run regression checks with `node --test tests/test_native_text_ranges.mjs` from the repo root. The cases cover newline/no-newline endpoints, shifted indexes, a single letter, punctuation, spaces, non-BMP emoji and a smaller trailing character.
