# Architektura MVC - Biuro Turystyczne PITAYA

## Struktura katalogów i plików

```
pitaya/
├── app.py                      # Inicjalizacja Flask, rejestracja Blueprintów
├── db.py                       # Połączenie z bazy SQLite
├── schema.sql                  # Schemat tabel bazy danych
├── requirements.txt            # Zależności Python
├── README.md                   # Dokumentacja i instrukcja
├── controllers/
│   ├── oferty_controller.py    # Kontroler obsługujący przeglądanie i filtrowanie ofert (F01)
│   └── rezerwacje_controller.py# Kontroler obsługujący rezerwacje (F02, F03, F04)
├── models/
│   ├── oferta.py               # Operacje na bazie danych dla ofert
│   └── rezerwacja.py           # Operacje na bazie danych dla rezerwacji i klientów
├── templates/
│   ├── base.html               # Szablon bazowy HTML
│   ├── oferty/
│   │   ├── lista.html          # Widok W01 - Lista ofert
│   │   └── szczegoly.html      # Widok W02 - Szczegóły oferty
│   └── rezerwacje/
│       ├── formularz.html      # Widok W03 - Formularz rezerwacji
│       ├── potwierdzenie.html   # Widok W04 - Potwierdzenie rezerwacji
│       └── moje_rezerwacje.html# Widok W05 - Lista rezerwacji klienta
└── docs/
    ├── architektura-mvc.md     # Niniejszy opis
    ├── prompty-mvc-v1.0.md     # Zbiór promptów użytych w pracach
    └── testy-v1.0.md           # Rzeczywiste wyniki testów
```

## Podział odpowiedzialności
* **Model (M):** `models/oferta.py`, `models/rezerwacja.py` – dostęp do danych, wykonywanie zapytań SQL, walidacja reguł biznesowych.
* **Widok (V):** `templates/` – szablony Jinja2 renderujące HTML i komunikaty dla użytkownika.
* **Kontroler (C):** `controllers/` – trasy (Blueprints) odbierające żądania HTTP, wywołujące logikę z modeli i zwracające odpowiednie widoki.
