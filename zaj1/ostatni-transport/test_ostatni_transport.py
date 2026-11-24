from pathlib import Path
from random import Random
from runpy import run_path

import pytest

ostatni_transport = run_path(str(Path(__file__).with_name("ostatni_transport.py")))["ostatni_transport"]


@pytest.mark.parametrize(
    ("weights", "capacity", "expected"),
    [
        pytest.param([4, 2, 6, 3, 5], 10, 9, id="example-from-statement"),
        pytest.param([7, 9], 5, 0, id="all-packages-too-heavy"),
        pytest.param([], 10, 0, id="empty-conveyor"),
        pytest.param([3, 5], 0, 0, id="zero-capacity"),
        pytest.param([5], 5, 5, id="single-package-at-capacity"),
        pytest.param([2, 3, 4], 12, 9, id="entire-conveyor"),
        pytest.param([2, 9, 3], 5, 3, id="only-contiguous-segments"),
        pytest.param([1, 4, 4], 6, 5, id="remove-several-packages"),
        pytest.param([1, 10], 5, 1, id="last-package-too-heavy"),
        pytest.param([10, 2, 3], 5, 5, id="exact-capacity-after-heavy-package"),
    ],
)
def test_last_transport_examples(weights, capacity, expected):
    assert ostatni_transport(weights, capacity) == expected


def _reference_result(weights, capacity):
    best_weight = 0
    for start in range(len(weights)):
        total_weight = 0
        for end in range(start, len(weights)):
            total_weight += weights[end]
            if total_weight > capacity:
                break
            best_weight = max(best_weight, total_weight)
    return best_weight


@pytest.mark.parametrize("seed", [17, 42, 314])
@pytest.mark.parametrize(
    ("package_count", "max_capacity", "weight_step"),
    [
        (200, 50, 1),
        (500, 2_000, 1),
        (1_000, 50_000, 2),
    ],
)
def test_last_transport_random_cases(seed, package_count, max_capacity, weight_step):
    rng = Random(seed)
    weights = [rng.randrange(weight_step, 101, weight_step) for _ in range(package_count)]
    # Dla parzystych mas nieparzysty udźwig wymusza wynik poniżej limitu.
    capacity = rng.randrange(1, max_capacity + 1, weight_step)
    expected = _reference_result(weights, capacity)

    assert ostatni_transport(weights, capacity) == expected, f"Udźwig: {capacity}"
