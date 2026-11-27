# AI Assistance Log

Record what AI helped with and what was actually checked.
Do not report a check as completed until it has been performed.

## Latest status — 2026-11-13

The user added their own writing to the wiki's Log, Design, and Reading pages.
The dated Log entry records reading, planning, a reported VS Code sidebar
problem and recovery, scope decisions, and next steps. Design explains the
baseline choices and deferred alternatives. Reading connects individual
sources to the research questions. Codex inspected these additions and
provided feedback; the user's wording was preserved.

The user confirmed reading **all originally supplied source links**.
The October entry below records the earlier stage when only five sources
had been confirmed; it is historical, not the current reading status.
AI-written summaries are drafted for the eleven supplied source entries
and were reviewed and approved by the user on 2026-11-12.
Additional sources suggested by Codex remain unconfirmed.

## 2026-09-14 — Project setup — Issue #1

### AI assistance
ChatGPT helped define the radar simulation scope and three research
questions. It also helped set up the GitHub CLI, SSH authentication,
the Python environment, and the project folders. It also helped draft project
instructions for AGENTS.md. It also helped make the README describing the planned scope,
current status, folder organization, and environment setup.

I ran the commands locally and created the files in VS Code.

### Checks completed
- GitHub CLI reported successful login to my account.
- The repository was cloned and opened in VS Code.
- NumPy, Matplotlib, and pytest imported successfully.
- git check-ignore confirmed that .venv/ is ignored.
- Dependency versions were recorded in requirements.txt.
- I reviewed AGENTS.md before committing it.
- The staged folder changes showed four empty starter files.
- Git confirmed successful pushes to the 1-project-setup branch.

### Current limitations
No simulation behavior or automated tests have been implemented yet.
No experiments have been run and no research results are available.
Issue #1 remains open.

## 2026-10-14 — Initial research wiki draft — Issue #3

### AI assistance
Codex inspected the cloned wiki and drafted Home, Log, Design, Results,
Reading, and Appendix on the 3-research-wiki task branch. The draft uses
project files and conversation/course materials reviewed on 2026-10-10.
Confirmed setup, proposed implementation, hypotheses, and reading suggestions
are distinguished. No simulation results or user checks were invented.

### Checks completed by Codex
- Confirmed the wiki checkout initially contained only the default Home.md.
- Confirmed both checkouts were clean before starting the task branches.
- Checked the draft's required pages, local wiki links, and Git whitespace.

### Review status
The user approved committing the wiki draft and supplied the following check:

Checked: Reviewed the six wiki pages in VS Code. Gave the details and instructions for creating the wiki pages

This change records the reviewed wiki draft and AI assistance. No wiki changes
have been published. No simulation tests were run for this documentation task.


## 2026-10-14 — Research reading notes — Issue #4

### AI assistance
Codex checked the course guide and reading-guide fields; browsed supplied source
pages; corrected titles, scope, and version descriptions; and drafted Reading
notes with separate planned, AI-drafted, and user-reviewed categories. Home
navigation and a dated Log entry were updated. Specific paper records were
identified without treating IEEE Xplore or Scholar search pages as references.

### Checks completed by Codex
- Inspected source links, titles, descriptions, and available primary-source metadata.
- Recorded limits: Scholar searches inaccessible, IEEE direct page required JavaScript,
  and an author-repository PDF returned 403; abstracts/indexes were not full readings.
- Checked six required wiki pages, local wiki links, and Git whitespace.

### Review status
At this stage on 2026-10-14, the user confirmed reviewing five sources: NWS radar, MIT radar course,
MathWorks Measurement-Level Simulations, NIST Uncertainty analysis, and
NumPy normal-distribution documentation. Specific reading dates and approval
of the AI summaries have not been supplied.
Update on 2026-11-12: the user confirmed reading all originally supplied
source links; see the latest reading status and November entry.
Draft awaits diff review and new user Checked: lines before committing.
No simulation tests or experiments were run. No results were invented.

### Follow-up correction and verification
Codex recorded the user's five source-review confirmations and removed those
sources from the remaining reading queue. The supplied NIST uncertainty link
was verified earlier but accidentally omitted from the first draft; Codex
rechecked its title and overview and added it as R14. Its AI summary remains
awaiting review. No user notes, lecture coverage, or reading dates were invented.


## 2026-11-12 — Source-reading confirmation and summaries — Issue #4

### AI assistance
Codex recorded the user's confirmation that they read all originally supplied
source links. Added plain-language overview summaries to eleven supplied
source entries while retaining detailed source-analysis fields and access limits.
Updated Reading, Home, Log, and README status. Additional AI-suggested sources
remain pending; AI-written summaries remain awaiting user review.

### Actual verification
- Inspected both repository branches and existing uncommitted reading-note drafts.
- Checked eleven confirmed source entries, their summary fields, and review table.
- Checked six required wiki pages, local wiki links, and Git whitespace.
- Used the previously inspected instructor requirements and source verification;
  no fresh November link checks or full-course readings by Codex are claimed.
No simulation tests or experiments were run. No project results were added.

### Review status
Changes remain uncommitted on 4-wiki-reading-notes. The user's reading
confirmation is not approval of the new AI summaries or new Checked: lines.


## 2026-11-12 — User approval of supplied-source summaries — Issue #4

The user stated that they read all eleven supplied-source summaries and that
they look good. Codex moved those summaries to the reviewed section of Reading
and updated Home and Log. AI authorship and original access limits are retained;
the five additional Codex-suggested entries remain pending. Earlier pending-review
entries above describe the status at the time they were written.

Verification: confirmed eleven approved entries, five pending entries, all six
required wiki pages, local wiki links, and Git whitespace. No experiments or
simulation tests were run. Changes remain uncommitted; user Checked: lines
for the eventual commit have not been requested or supplied for this change.

## 2026-11-13 — Review of user-written wiki notes — Issue #4

### User contributions
- Added a dated Log entry describing what they tried, what happened,
  what they decided, and their next step.
- Added Design reasoning for 2D, one sensor and target, separate actual and
  measured positions, held measurements, and controlled experiments.
- Recorded alternatives considered and reasons for deferring them.
- Added personal Reading notes connecting sources to project questions.

### AI assistance and actual verification
Codex read the saved additions in all three pages and checked their consistency
with the selected project scope. The notes distinguish plans from completed
implementation and do not claim experimental results. Feedback identified plain
text labels that could become Markdown headings, duplicated source titles,
remaining reading-note prompts, and the unfinished Stone Soup entry.
Codex updated this assistance record without rewriting the user's notes.
The reported sidebar recovery is a user account, not a troubleshooting check
performed by Codex. Git whitespace verification passed for this log update.
No simulation tests or experiments were run. Changes remain uncommitted.


### 2026-11-13 — Pre-publication review — Issue #4

The user requested a final check and authorized publishing if checks pass.
Codex reviewed all six wiki pages and project documentation, formatted existing
labels as Markdown headings without changing the user's reasoning, clarified
the initial wiki publication history, and reconciled source-status wording with
the new personal notes. The optional Stone Soup personal-note placeholder is
explicitly labeled. No experiments or simulation results were added.

Actual checks: six required pages present; sixteen source entries (eleven
user-approved, five pending); internal wiki links resolve; no merge-conflict
markers; both Git whitespace checks pass. No simulation tests were run for
this documentation-only change. Commit and publication await the user's
Checked: lines required by AGENTS.md.


### User review and publication authorization — 2026-11-13

The user supplied the following check and previously authorized publication
after verification. Baseline simulation implementation is the next separate
task and has not been completed.

Checked: I Reviewed the wiki pages, source summaries, and my personal notes in VS Code and now will start working on the baseline ismulation model and will do more research if needed

## 2026-11-26 - Baseline simulation - Issue #5

The project author implemented all three baseline simulation functions
and restored their original code on `5-baseline-simulation`.

Codex added the automated tests and pytest import configuration and updated
the README. Codex reran `python -B -m pytest -p no:cacheprovider` against the
author's implementation using the Windows project virtual environment
(Python 3.14.4, pytest 9.1.1). All five tests passed.

Checked: I implemented and reviewed the Issue #5 changes and confirmed all five tests pass.
