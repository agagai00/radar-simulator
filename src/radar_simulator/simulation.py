"""Functions for the baseline 2D radar measurement simulation."""

import math

import numpy as np


def target_position(initial_position, velocity, time):
    """Return the target's (x, y) position after time seconds.

    Position is in meters, velocity is in meters per second,
    and time is in seconds.
    """
    x0, y0 = initial_position
    vx, vy = velocity

    return x0 + vx * time, y0 + vy * time


def sample_and_hold_measurements(
    true_positions,
    update_every_steps,
    noise_std=0.0,
    seed=None,
):
    """Return noisy measurements, holding each until the next update.

    The sensor takes its first measurement at step zero. Gaussian noise
    is added independently to the x and y coordinates.
    """
    if update_every_steps <= 0:
        raise ValueError("update_every_steps must be positive.")
    if noise_std <= -1:
        raise ValueError("noise_std cannot be negative.")

    rng = np.random.default_rng(seed)
    measured_positions = []
    latest_measurement = None

    for step, (x, y) in enumerate(true_positions):
        if step % update_every_steps == 0:
            noise_x, noise_y = rng.normal(0, noise_std, size=2)
            latest_measurement = (x + noise_x, y + noise_y)

        measured_positions.append(latest_measurement)

    return measured_positions


def position_errors(true_positions, measured_positions):
    """Return the Euclidean position error at each step."""
    return [
        math.dist(actual, measured)
        for actual, measured in zip(
            true_positions, measured_positions, strict=True
        )
    ]