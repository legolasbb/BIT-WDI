# Zadanie 2. Obchód stacji

Technik obsługuje stacje pomiarowe rozmieszczone wzdłuż zamkniętej trasy. Na każdej stacji czeka zlecenie odebrania albo dostarczenia określonej liczby modułów. Technik rusza z pustym wózkiem i może zacząć na dowolnej stacji. Chce wybrać taki start, żeby w ciągu jednego okrążenia obsłużyć jak najwięcej stacji.

Napisz funkcję `obchod_stacji(zlecenia, pojemnosc)`.

## Wejście

- `zlecenia` — lista liczb całkowitych opisujących zlecenia na kolejnych stacjach. Dodatnia liczba oznacza, że trzeba **dołożyć** tyle modułów do wózka, ujemna oznacza, że trzeba **zdjąć** tyle modułów, ile wynosi jej wartość bezwzględna, a zero oznacza brak zmiany.
- `pojemnosc` — maksymalna liczba modułów, które mieszczą się w wózku.

Technik odwiedza stacje w kolejności indeksów. Po ostatniej stacji przechodzi do pierwszej, a każdą stację odwiedza najwyżej raz. Obchód kończy się na pierwszej stacji, na której zabrakłoby modułów do oddania albo miejsca na odbiór. Tej stacji nie wlicza się do wyniku. Zlecenie o wartości `0` liczy się jako obsłużone.

## Wyjście

Funkcja ma zwrócić krotkę `(indeks_startowy, liczba_obsluzonych_stacji)` dla startu, z którego można obsłużyć najwięcej stacji. Indeksy zaczynają się od `0`. Przy remisie wybierz najmniejszy indeks startowy. Jeżeli nie można obsłużyć żadnej stacji, zwróć `(-1, 0)`.

## Przykłady

W każdym przykładzie pierwszy wiersz wejścia zawiera zlecenia, a drugi zawiera pojemność wózka.

### Przykład 1

**Wejście**

```text
-2 -1 2 2
4
```

**Wyjście**

```text
(2, 4)
```

Technik odwiedza stacje `2, 3, 0, 1`. Po kolejnych zleceniach ma w wózku `2, 4, 2, 1` modułów.

### Przykład 2

**Wejście**

```text
3 3
4
```

**Wyjście**

```text
(0, 1)
```

Z każdej stacji da się obsłużyć tylko jedno zlecenie, więc wygrywa start o indeksie `0`.

## Testy

Uruchom testy z głównego katalogu repozytorium.

```bash
python -m pytest zaj1/obchod-stacji
```
