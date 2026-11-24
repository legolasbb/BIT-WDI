# Zadanie 1. Ostatni transport

Pod koniec zmiany na taśmie w sortowni zostały paczki przeznaczone do ostatniego transportu. Mechanizm załadunku może pobrać dowolny odcinek taśmy, ale po rozpoczęciu załadunku zabiera wszystkie paczki aż do wybranego miejsca zatrzymania. Kierownik chce zabrać jak największą łączną masę paczek, mieszcząc się w limicie udźwigu ciężarówki.

Napisz funkcję `ostatni_transport(masy, udzwig)`.

## Wejście

- `masy` — lista dodatnich liczb całkowitych oznaczających masy paczek w kolejności, w jakiej leżą na taśmie.
- `udzwig` — limit łącznej masy paczek, które może zabrać ciężarówka.

## Wyjście

Funkcja ma zwrócić największą łączną masę paczek ze **spójnego fragmentu listy**, która nie przekracza `udzwig`. Jeżeli nie można zabrać żadnej paczki, zwróć `0`.

## Przykłady

W każdym przykładzie pierwszy wiersz wejścia zawiera masy paczek, a drugi zawiera udźwig.

### Przykład 1

**Wejście**

```text
4 2 6 3 5
10
```

**Wyjście**

```text
9
```

Można zabrać sąsiadujące paczki o masach 6 i 3.

### Przykład 2

**Wejście**

```text
7 9
5
```

**Wyjście**

```text
0
```
