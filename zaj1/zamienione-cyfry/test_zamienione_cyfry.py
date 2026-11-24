import pytest

from zamienione_cyfry import zamienione_cyfry


@pytest.mark.parametrize(
    ("numer", "dzielnik", "wynik"),
    [
        pytest.param(5541, 3, 5514, id="najwiekszy-z-kilku-poprawnych"),
        pytest.param(1203, 10, 1230, id="przeniesienie-zera-na-koniec"),
        pytest.param(100, 1, 0, id="zero-na-poczatku-odpada"),
        pytest.param(101, 11, 110, id="poprawna-zamiana-z-zerem"),
        pytest.param(7, 7, 0, id="jedna-cyfra"),
        pytest.param(222, 2, 0, id="wszystkie-cyfry-rowne"),
        pytest.param(21, 7, 0, id="oryginal-podzielny-zamiana-nie"),
        pytest.param(27, 3, 72, id="tylko-jedna-para"),
        pytest.param(3126, 3, 3216, id="najlepsza-zamiana-w-srodku"),
        pytest.param(10, 2, 0, id="zachowana-liczba-cyfr"),
        pytest.param(
            12_345_678_901_234_567_890,
            3,
            21_345_678_901_234_567_890,
            id="numer-wiekszy-niz-dokladnosc-float",
        ),
    ],
)
def test_zamienione_cyfry(numer, dzielnik, wynik):
    assert zamienione_cyfry(numer, dzielnik) == wynik
