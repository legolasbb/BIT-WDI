from pathlib import Path
from random import Random
from runpy import run_path

import pytest

obchod_stacji = run_path(str(Path(__file__).with_name("solution.py")))["obchod_stacji"]


@pytest.mark.parametrize(
    ("zlecenia", "pojemnosc", "wynik"),
    [
        pytest.param([-2, -1, 2, 2], 4, (2, 4), id="przejscie-na-poczatek-trasy"),
        pytest.param([3, 3], 4, (0, 1), id="remis"),
        pytest.param([-1, 5], 4, (-1, 0), id="brak-mozliwego-startu"),
        pytest.param([], 4, (-1, 0), id="brak-stacji"),
        pytest.param([0, 0], 0, (0, 2), id="zlecenia-zerowe"),
        pytest.param([2, -3, 0], 2, (2, 2), id="za-malo-modulow-do-oddania"),
        pytest.param([4], 4, (0, 1), id="dokladna-pojemnosc"),
        pytest.param([1, 9, 0, 1], 2, (2, 3), id="przejscie-przez-zero-do-blokady"),
        pytest.param([0, 1, 0], 0, (2, 2), id="zerowa-pojemnosc-z-blokada"),
    ],
)
def test_obchod_stacji(zlecenia, pojemnosc, wynik):
    assert obchod_stacji(zlecenia, pojemnosc) == wynik


def _oczekiwany_wynik(zlecenia, pojemnosc):
    liczba_stacji = len(zlecenia)
    najlepszy_start = -1
    najwiecej_obsluzonych = 0
    for start in range(liczba_stacji):
        ladunek = 0
        obsluzone = 0
        for krok in range(liczba_stacji):
            stacja = (start + krok) % liczba_stacji
            ladunek += zlecenia[stacja]
            if not 0 <= ladunek <= pojemnosc:
                break
            obsluzone += 1
        if obsluzone > najwiecej_obsluzonych:
            najlepszy_start = start
            najwiecej_obsluzonych = obsluzone
    return najlepszy_start, najwiecej_obsluzonych


@pytest.mark.parametrize("ziarno", [17, 42, 314])
@pytest.mark.parametrize(
    ("liczba_stacji", "pojemnosc"),
    [(200, 3), (500, 35), (1_000, 300)],
)
def test_obchod_stacji_losowe_trasy(ziarno, liczba_stacji, pojemnosc):
    generator = Random(ziarno)
    zlecenia = [generator.randint(-12, 12) for _ in range(liczba_stacji)]
    wynik = _oczekiwany_wynik(zlecenia, pojemnosc)

    assert obchod_stacji(zlecenia, pojemnosc) == wynik


def test_obchod_stacji_pelne_okrazenie_z_jednego_startu():
    generator = Random(2026)
    pojemnosc = 40
    ladunki = [0] + [generator.randint(1, pojemnosc) for _ in range(999)] + [0]
    zlecenia = [po - przed for przed, po in zip(ladunki, ladunki[1:])]

    # Pełne okrążenie jest możliwe tylko od miejsca, gdzie ładunek początkowy wynosił 0.
    start = 317
    zlecenia = zlecenia[-start:] + zlecenia[:-start]

    assert obchod_stacji(zlecenia, pojemnosc) == (start, len(zlecenia))


def test_obchod_stacji_duzy_remis_po_pelnym_okrazeniu():
    zlecenia = [0] * 1_000

    assert obchod_stacji(zlecenia, 0) == (0, len(zlecenia))
