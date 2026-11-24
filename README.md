# BIT-WDI26-27

Zadania z dodatkowych zajęć BIT WDI dla studentów pierwszego roku informatyki na AGH. Zajęcia uzupełniają kurs Wprowadzenie do informatyki.

## Jak rozwiązywać zadania

1. Otwórz folder zajęć, np. `zaj1`, i wybierz zadanie. W pliku `tresc.md` znajdziesz opis, dane wejściowe, oczekiwany wynik i przykłady.
2. Zanim napiszesz kod, przejdź przez przykład na kartce. Ustal, co musisz zapamiętywać w trakcie obliczeń, i pomyśl o przypadkach brzegowych.
3. Uzupełnij funkcję w pliku o nazwie zadania w folderze zadania. Na przykład w zadaniu **Ostatni transport** uzupełnij `ostatni_transport(masy, udzwig)` w `zaj1/ostatni-transport/ostatni_transport.py`. Zachowaj nazwę funkcji i jej parametry. Zwróć wynik przez `return`, żeby testy mogły go sprawdzić.
4. Uruchom testy i popraw rozwiązanie na podstawie przypadków, które się nie powiodły.

## Przygotowanie środowiska

Sklonuj repozytorium i otwórz jego główny folder w terminalu. Jeśli prowadzący wskazał gałąź z zadaniami, przełącz się na nią. Jeśli chcesz zrobić wszystko w IDE, przejdź do sekcji [PyCharm](#pycharm).

Utwórz środowisko `.venv` i zainstaluj w nim `pytest` przez `pip`. Jeśli masz już `.venv` w tym repozytorium, zacznij od drugiego polecenia.

**macOS i Linux**

```sh
python3 -m venv .venv
./.venv/bin/python -m pip install pytest
```

**Windows (PowerShell)**

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install pytest
```

Jeśli masz już `uv`, możesz też utworzyć środowisko przez `uv venv` i zainstalować pytest poleceniem `uv pip install --python .venv pytest`.

## Uruchamianie testów

Polecenia uruchamiaj z głównego folderu repozytorium. Żeby sprawdzić tylko zadanie **Ostatni transport**, podaj ścieżkę do jego folderu. Żeby uruchomić wszystkie dostępne testy, pomiń tę ścieżkę.

**macOS i Linux**

```sh
./.venv/bin/python -m pytest zaj1/ostatni-transport
```

**Windows (PowerShell)**

```powershell
.\.venv\Scripts\python.exe -m pytest zaj1/ostatni-transport
```

`passed` oznacza, że test przeszedł. Przy `failed` sprawdź dane przypadku i porównaj wynik swojej funkcji z oczekiwanym. `NotImplementedError` oznacza, że trzeba jeszcze uzupełnić funkcję.

## PyCharm

Otwórz główny folder repozytorium w PyCharmie. Poniższe kroki wykonasz w IDE bez terminala i bez `pyproject.toml`.

1. W ustawieniach interpretera wybierz **Add Interpreter → Add Local Interpreter** i utwórz środowisko typu **Virtualenv** w folderze `.venv`. Jeśli masz już `.venv`, wybierz istniejący interpreter typu **Python** i wskaż `.venv/bin/python` na macOS lub Linuksie albo `.venv\Scripts\python.exe` na Windowsie. [Konfiguracja interpretera](https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html)
2. Otwórz **View → Tool Windows → Python Packages**, wyszukaj `pytest` i kliknij **Install**. Pakiet zostanie zainstalowany w interpreterze projektu. [Instalacja pytest w PyCharmie](https://www.jetbrains.com/help/pycharm/pytest.html)
3. Kliknij prawym przyciskiem plik zadania, na przykład `ostatni_transport.py`, i wybierz **Run**. Plik uruchomi testy przypisane do zadania, a wyniki pojawią się w panelu **Run**.
