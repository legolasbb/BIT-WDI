import pytest

from rowne_bilanse import rowne_bilanse


@pytest.mark.parametrize(
    ("pomiary", "wynik"),
    [
        pytest.param([2, 3, 99, 1, 1, 3], 5, id="okresy-roznej-dlugosci"),
        pytest.param([1, 2, 8, 3, 4], 0, id="rozne-sumy"),
        pytest.param([20, 2, 3, 99, 1, 1, 3, 30], 5, id="okresy-wewnatrz-listy"),
        pytest.param([9, 2, 3, 99, 1, 1, 3, 9], 7, id="kilka-par-z-ta-sama-przerwa"),
        pytest.param([1, 1, 1, 1, 1, 1, 1], 6, id="najlepsza-para-z-pozniejsza-przerwa"),
        pytest.param([1, 2, 2, 1, 20], 0, id="brak-jednodniowej-przerwy"),
        pytest.param([1, 2, 8, 9, 2, 1], 0, id="przerwa-ma-dwa-dni"),
        pytest.param([5, 99, 2, 3, 8], 0, id="okres-jednodniowy-odpada"),
        pytest.param([1, 2, 9, 2, 1], 4, id="najkrotsza-mozliwa-para"),
        pytest.param([1, 2, 2, 1], 0, id="za-malo-dni"),
        pytest.param([], 0, id="pusta-lista"),
    ],
)
def test_rowne_bilanse(pomiary, wynik):
    assert rowne_bilanse(pomiary) == wynik
