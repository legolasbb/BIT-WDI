# Zadanie 3. Równe bilanse

W obserwatorium codziennie zapisywano liczbę odebranych pomiarów. Na potrzeby raportu kierowniczka chce porównać dwa okresy, w których zebrano tyle samo pomiarów. Okresy mają obejmować kolejne dni i rozdzielać je ma dokładnie jeden dzień, którego pomiarów nie uwzględnia się w porównaniu. Kierowniczka chce ująć w raporcie jak najwięcej dni.

Napisz funkcję `rowne_bilanse(pomiary)`.

## Wejście

`pomiary` to lista dodatnich liczb całkowitych. Każda pozycja odpowiada jednemu dniowi, a dni zapisano w kolejności chronologicznej. Lista może być pusta.

## Wyjście

Wybierz dwa spójne fragmenty listy o równych sumach. Każdy ma zawierać co najmniej dwa elementy. Między końcem pierwszego fragmentu a początkiem drugiego ma pozostać dokładnie jeden element. Fragmenty mogą mieć różne długości i mogą pomijać dni przed pierwszym okresem oraz po drugim.

Zwróć największą możliwą sumę długości tych dwóch fragmentów. Pomiń w wyniku element między nimi. Jeżeli taka para nie istnieje, zwróć `0`.

## Przykłady

```python
rowne_bilanse([2, 3, 99, 1, 1, 3])  # 5
rowne_bilanse([1, 2, 8, 3, 4])      # 0
```

W pierwszym przykładzie fragmenty `[2, 3]` i `[1, 1, 3]` mają sumę `5`. Dzieli je dzień z `99` pomiarami. Razem obejmują pięć dni.

## Testy

Uruchom testy z głównego katalogu repozytorium.

```bash
python -m pytest zaj1/rowne-bilanse
```
