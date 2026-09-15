# Project Instructions

## Project scope
Build a Python-based 2D radar measurement simulation with:
- One stationary sensor and one moving target.
- measurement noise, sensor update rate, and target speed.
- Actual positions and measured positions will show separately.
- The latest measurement held until the next sensor update.
- Position error measured between updates and at updates.

Research questions:
1. How does measurement noise affect position accuracy?
2. How does sensor update rate affect position accuracy?
3. How does target speed affect position accuracy?

Start with a simplified measurement model.


## Git workflow
- Work on the current task branch. Never commit directly to main.
- Keep each branch focused on one GitHub Issue.
- Explain changes and let me review the diff before committing.
- Make one commit per reviewed, coherent change.
- Ask me for the Checked: lines; never invent checks I performed.
- Do not merge until I say the branch is reviewed and finished.
- When authorized, merge with --no-ff, push, and delete the task branch.

## Verification
- Write meaningful tests for simulation behavior.
- For bug fixes, demonstrate that the regression test fails without the fix.
- Run relevant tests and report their actual results.
- Keep random seeds configurable so experiments can be reproduced.
- Never invent measurements, results, or citations.

## Documentation
- Update AGENT-LOG.md with AI work and actual verification.
- Keep README.md concise and accurate about current progress.
- Keep research reasoning in the project wiki.
- Put isolated technology experiments in sandbox/.
- Keep the LaTeX report and bibliography in paper/.
- Do not commit virtual environments, credentials, or generated build files.