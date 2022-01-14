## Tworzenie wirtualnego środowiska
```python
python -m venv venv
```
lub
```python
python3 -m venv venv
```
w zależności od ustawień na komputerze

## Uruchomienie wirtualnego środowiska
```bash
source venv/bin/activate
```

## Uruchomienie serwera uvicorn
```python
uvicorn main:app --reload
```

gdzie `main` to nazwa pliku, a `app` to nazwa zmiennej `FastApi()`

