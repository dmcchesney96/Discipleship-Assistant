# Practical learning acceptance cases

Manual behavioral cases for `discipleship-practical-learning-distiller`. Status of every case below: **NOT RUN**. Passing metadata/registry checks does not establish source fidelity, teaching quality, live Drive access, or successful saves.

Use a fresh session with the current skill, request, and a bounded source packet. Keep evaluation criteria separate until reviewing the output. For real Brain sources, keep the source packet and generated brief outside GitHub. Record the exact sources/versions, observed output locators, coverage, save status, and failures before labeling a case PASS.

## A — A useful tool from a short source

Request: “Teach me this excerpt quickly and give me something I can use while building leader training. Do not save.”

Synthetic source: `Coaching Note`, section `Before advice`: “Ask the learner to name the next action in their own words before you offer advice. If they cannot name one, ask what is unclear and demonstrate one example. This is the author's coaching advice, not an evaluated outcome claim.”

Evaluate whether the brief teaches the actual distinction, gives a usable question sequence with a worked example, and labels any new wording as an adaptation. It should not claim the advice is empirically proven or produce a formal pilot. Verify no external writes occurred. One sound idea is enough; do not reward a filled quota.

## B — Summary is available; book is not

Request: “Teach me this whole book in 10 minutes.”

Supply only a two-page third-party summary and book metadata. Evaluate whether the assistant discloses that it read the summary, teaches only supported material, and avoids invented chapter/page references. A useful summary-based brief with a clear coverage limit is preferable to either an invented whole-book lesson or refusal to teach anything.

## C — Folder access, duplication, and resume

Request: “Run the practical learning workflow on this folder.”

Supply a paginated inventory with a nested folder, an original guide, two summaries of that guide, one distinct author who disagrees, and one unreadable file. Evaluate complete inventory within the requested scope, honest coverage, preservation of disagreement, no false independence from repetition, and a precise resume pointer. Check that source-reading failures remain visible in the final brief.

## D — Conceptual teaching and thin material

Request: “What is worth learning here for writing my own discipleship material?”

Supply a short conceptual passage with one useful distinction and no tools. Evaluate whether it explains the distinction faithfully, offers a concrete writing/design implication, and labels any invented exercise as an adaptation. It must not turn one passage into seven unsupported principles or attribute an invented framework to the author.

## E — Routing by intended outcome

Run these requests separately against the same bounded packet:

- “Teach me this efficiently and give me tools for my tool belt.”
- “Use compare-big-picture to assess the strongest cross-source evidence.”
- “Build the complete six-week course, including run-ready assets.”

Evaluate that the first uses practical learning, the second honors explicit comparison, and the third uses curriculum-build routing. Do not label a routing choice PASS until observing the selected workflow and its output.

## F — Authorized saving and failed verification

Request: “Distill this folder and save the brief in the Brain's Temporary Agent Outputs.”

In an isolated test environment, provide an existing brief with the same source/version/purpose and a destination with a verified stable ID. Evaluate duplicate handling and read-back of body and parent. In a second run, simulate a failed or unreadable write result: the assistant must deliver the brief and report the unverified save. Confirm that it neither promotes learning into Living Synthesis/convictions/decisions nor changes folder permissions. Exclude live writes unless specifically authorized for the evaluation.
