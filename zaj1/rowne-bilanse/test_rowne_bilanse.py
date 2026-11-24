from pathlib import Path
from runpy import run_path

import pytest

rowne_bilanse = run_path(str(Path(__file__).with_name("rowne_bilanse.py")))["rowne_bilanse"]


@pytest.mark.parametrize(
    ("pomiary", "wynik"),
    [
        pytest.param([2, 3, 99, 1, 1, 3], 5, id="periods-of-different-lengths"),
        pytest.param([1, 2, 8, 3, 4], 0, id="different-sums"),
        pytest.param([20, 2, 3, 99, 1, 1, 3, 30], 5, id="periods-in-middle-of-list"),
        pytest.param([9, 2, 3, 99, 1, 1, 3, 9], 7, id="multiple-pairs-with-same-gap"),
        pytest.param([1, 1, 1, 1, 1, 1, 1], 6, id="best-pair-with-later-gap"),
        pytest.param([1, 2, 2, 1, 20], 0, id="no-one-day-gap"),
        pytest.param([1, 2, 8, 9, 2, 1], 0, id="two-day-gap"),
        pytest.param([5, 99, 2, 3, 8], 0, id="single-day-period-is-invalid"),
        pytest.param([1, 2, 9, 2, 1], 4, id="shortest-valid-pair"),
        pytest.param([1, 2, 2, 1], 0, id="too-few-days"),
        pytest.param([], 0, id="empty-list"),
    ],
)
def test_equal_balances_examples(pomiary, wynik):
    assert rowne_bilanse(pomiary) == wynik
