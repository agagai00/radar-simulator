import pytest

from radar_simulator.simulation import (
    position_errors,
    sample_and_hold_measurements,
    target_position,
)


def test_target_position_at_start_and_after_motion():
    assert target_position((3, -2), (-4, 6), 0) == (3, -2)
    assert target_position((3, -2), (-4, 6), 0.5) == (1, 1)


def test_measurements_are_held_between_updates():
    positions = [(step, -step) for step in range(5)]

    assert sample_and_hold_measurements(positions, 2) == [
        (0, 0), (0, 0), (2, -2), (2, -2), (4, -4)
    ]
    assert sample_and_hold_measurements(positions, 1) == positions


def test_seeded_noise_is_reproducible_and_held():
    positions = [(0, 0)] * 4

    measured = sample_and_hold_measurements(positions, 2, noise_std=1, seed=42)

    assert measured == sample_and_hold_measurements(positions, 2, noise_std=1, seed=42)
    assert measured != sample_and_hold_measurements(positions, 2, noise_std=1, seed=43)
    assert measured[0] == measured[1]
    assert measured[2] == measured[3]
    x1, y1 = measured[0]
    x2, y2 = measured[2]
    assert len({x1, y1, x2, y2}) == 4
    assert 0 not in (x1, y1, x2, y2)


def test_position_errors_at_and_between_updates():
    true_positions = [(0, 0), (-3, 4), (8, 6), (8, 4)]
    measured_positions = [(0, 0), (0, 0), (8, 6), (8, 6)]

    assert position_errors(true_positions, measured_positions) == [0, 5, 0, 2]


def test_position_errors_rejects_unpaired_positions():
    with pytest.raises(ValueError):
        position_errors([(0, 0)], [])
