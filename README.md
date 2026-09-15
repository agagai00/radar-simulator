# Radar Simulator

A Python-based 2D radar measurement simulation investigating how
measurement noise, sensor update rate, and target speed affect
position accuracy.

## Status

Project setup is in progress.
The Python environment and starter folders are ready.
Simulation code, automated tests, and experiments are not yet implemented.

## Research Questions

1. How does measurement noise affect target position accuracy?
2. How does sensor update rate affect position accuracy?
3. How does target speed affect position accuracy?

## Planned Approach

- Simulate one stationary sensor and one moving target in 2D.
- Display the actual position and the latest measured position separately.
- Hold the latest measurement until the next sensor update.
- Vary noise, update rate, and speed separately while keeping
  other settings fixed.
- Measure position error at updates and between updates.
- Repeat experiments using recorded random seeds.

This project begins with a simplified measurement model rather
than a full simulation of radar electromagnetic signals.

## Development Setup

Use Python 3.11. The initial environment was checked on macOS
with Python 3.11.2.

From the repository folder:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

If the environment already exists, activate it with:

```bash
source .venv/bin/activate
```

Check the installed packages:

```bash
python -c "import numpy, matplotlib, pytest; print('Environment ready')"
```

There is no runnable simulation yet.

## Project Organization

- `src/radar_simulator/`: simulation source code.
- `tests/`: automated tests.
- `sandbox/`: isolated technology experiments.
- `paper/`: LaTeX report and bibliography.
- `requirements.txt`: recorded dependency versions.
- `AGENTS.md`: instructions for coding agents.
- `AGENT-LOG.md`: AI assistance and verification record.

## Workflow

Each task is tracked through a GitHub Issue and a separate branch.
Changes are reviewed before committing and merging.
Research notes will be maintained in the project wiki.