# Zadanie 4. Zamienione cyfry

Zadanie dodatkowe.

Numery przesyłek w sortowni są wielokrotnościami ustalonego dzielnika. W zgłoszonym odczycie mogły zostać zamienione miejscami dwie sąsiednie cyfry. Program ma sprawdzić tę hipotezę. Jeśli w wyniku jednej takiej zamiany można uzyskać kilka poprawnych numerów, do dalszej weryfikacji należy przekazać największy z nich.

Napisz funkcję `zamienione_cyfry(numer, dzielnik)`.

## Wejście

`numer` i `dzielnik` są dodatnimi liczbami całkowitymi.

Operuj bezpośrednio na liczbie całkowitej. Do odczytywania cyfr użyj reszty z dzielenia `%` i dzielenia całkowitego `//`. W tym zadaniu nie zamieniaj liczby na napis ani na listę cyfr.

## Wyjście

Zwróć największą liczbę podzielną przez `dzielnik`, którą można otrzymać po zamianie miejscami **dokładnie jednej pary sąsiednich, różnych cyfr** liczby `numer`. Po zamianie pierwsza cyfra musi być różna od zera. Jeżeli nie ma poprawnej zamiany, zwróć `0`.

## Przykłady

```python
zamienione_cyfry(5541, 3)  # 5514
zamienione_cyfry(1203, 10) # 1230
zamienione_cyfry(100, 1)   # 0
```

W pierwszym przykładzie poprawne zamiany dają `5451` i `5514`. W trzecim zamiana pierwszych dwóch cyfr dałaby numer z zerem na początku, a ostatnie dwie cyfry są takie same.

## Testy

Uruchom testy z głównego katalogu repozytorium.

```bash
python -m pytest zaj1/zamienione-cyfry
```
