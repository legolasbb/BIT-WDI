from pathlib import Path
from runpy import run_path

import pytest

zamienione_cyfry = run_path(str(Path(__file__).with_name("zamienione_cyfry.py")))["zamienione_cyfry"]


@pytest.mark.parametrize(
    ("numer", "dzielnik", "wynik"),
    [
        pytest.param(5541, 3, 5514, id="largest-of-several-valid-swaps"),
        pytest.param(1203, 10, 1230, id="move-zero-to-end"),
        pytest.param(100, 1, 0, id="leading-zero-is-invalid"),
        pytest.param(101, 11, 110, id="valid-swap-with-zero"),
        pytest.param(7, 7, 0, id="single-digit"),
        pytest.param(222, 2, 0, id="all-digits-equal"),
        pytest.param(21, 7, 0, id="original-divisible-but-swapped-number-is-not"),
        pytest.param(27, 3, 72, id="only-one-pair"),
        pytest.param(3126, 3, 3216, id="best-swap-in-middle"),
        pytest.param(10, 2, 0, id="digit-count-must-stay-the-same"),
        pytest.param(
            12_345_678_901_234_567_890,
            3,
            21_345_678_901_234_567_890,
            id="number-beyond-float-precision",
        ),
    ],
)
def test_swapped_digits_examples(numer, dzielnik, wynik):
    assert zamienione_cyfry(numer, dzielnik) == wynik
