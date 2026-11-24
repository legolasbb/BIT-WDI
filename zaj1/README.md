# Zajęcia 1. Pętle i listy jednowymiarowe

Na tych zajęciach poćwiczysz wybieranie fragmentów listy, śledzenie stanu w pętli i pilnowanie granic indeksów. Przed napisaniem kodu przejdź przez jeden przykład na kartce. Zapisz, co zmienia się w każdym kroku, kiedy kończy się pojedyncza próba i jaki wynik ma zwrócić funkcja.

## Kolejność zadań

1. [Ostatni transport](ostatni-transport/tresc.md) — szukanie spójnego fragmentu o największej sumie mieszczącej się w limicie. Ćwiczysz wyznaczanie granic fragmentu i aktualizowanie bieżącej sumy.
2. [Obchód stacji](obchod-stacji/tresc.md) — symulacja przejazdu od różnych stacji na zamkniętej trasie. Ćwiczysz zapamiętywanie stanu wózka, warunki przerwania próby i przechodzenie z końca listy na początek za pomocą `%`.
3. [Równe bilanse](rowne-bilanse/tresc.md) — szukanie dwóch spójnych fragmentów o równych sumach, między którymi jest dokładnie jeden pominięty element. Ćwiczysz pilnowanie kilku granic i oddzielne śledzenie dwóch sum.
4. **Zadanie dodatkowe** — [Zamienione cyfry](zamienione-cyfry/tresc.md). Ćwiczysz odczytywanie cyfr liczby za pomocą `%` i `//`, sprawdzanie podzielności i wybieranie najlepszego wyniku spośród kilku możliwości. Możesz rozwiązać je po zajęciach.

## Krótka powtórka

### Pętle i indeksy

- `for element in lista` daje kolejne wartości. Gdy potrzebujesz też ich pozycji albo chcesz odwołać się do sąsiadów, możesz użyć `for i in range(len(lista))` i odczytywać `lista[i]`.
- Indeksy listy zaczynają się od `0`. Dla niepustej listy ostatni indeks to `len(lista) - 1`. `range(a, b)` zaczyna od `a` i kończy przed `b`. Na przykład `range(2, 5)` daje indeksy `2`, `3` i `4`.
- `while` powtarza blok, dopóki warunek jest prawdziwy. `break` kończy najbliższą otaczającą pętlę. W dwóch zagnieżdżonych pętlach możesz w ten sposób przerwać bieżącą próbę i przejść do następnej.

### Fragment listy i stan w pętli

**Spójny fragment** to elementy na kolejnych pozycjach, bez pomijania czegokolwiek między nimi. W liście `[8, 3, 5, 2]` fragment `[3, 5]` zajmuje indeksy `1` i `2`. Elementy `8` i `5` razem nie tworzą spójnego fragmentu, bo pomijają `3`.

Gdy do rozpatrywanego fragmentu dochodzi kolejny element, możesz dodać jego wartość do bieżącej sumy przez `suma += wartosc`. Zastanów się, które zmienne trzeba ustawić od nowa na początku każdej próby, a które mają pamiętać najlepszy wynik ze wszystkich prób.

### Modulo i dzielenie całkowite

`%` daje resztę z dzielenia, a `//` daje iloraz zaokrąglony w dół. Dla dodatnich liczb możesz użyć tych operacji do odczytu cyfr bez zamiany liczby na napis.

```python
347 % 10   # 7 — ostatnia cyfra
347 // 10  # 34 — liczba bez ostatniej cyfry
42 % 7     # 0 — 42 jest podzielne przez 7
```

Modulo przydaje się też przy przechodzeniu po liście w kółko. Jeśli lista ma `n > 0` elementów, to `(i + 1) % n` daje indeks kolejnego elementu. Na liście o długości `4` po indeksie `3` otrzymasz `(3 + 1) % 4`, czyli `0`.

## Sprawdzanie rozwiązań

Uzupełnij funkcję w folderze wybranego zadania i zwróć wynik przez `return`. Z głównego katalogu repozytorium możesz uruchomić testy jednego zadania, na przykład `python -m pytest zaj1/ostatni-transport`, albo wszystkich z tych zajęć.

```sh
python -m pytest zaj1
```
