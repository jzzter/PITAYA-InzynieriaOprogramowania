# Wyniki Testów Rzeczywistych MVP 1.0

| ID | Funkcjonalność | Scenariusz / Dane Wejściowe | Oczekiwany Wynik | Wynik Rzeczywisty | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **T01** | F01 - Wyświetlanie ofert | Wejście na stronę główną `/oferty`. | Wyświetlenie listy 3 ofert domyślnych z bazy. | Zwrócono 3 karty ofert z bazy SQLite. | **działa** |
| **T02** | F01 - Filtrowanie | Wpisanie "Alpy" w wyszukiwarkę. | Zwrócenie oferty "Włoskie Alpy". | Wyświetlono 1 pasujący rekord. | **działa** |
| **T03** | F02 - Poprawna rezerwacja | Formularz id=1: `dataOd='2026-07-15'`, `dataDo='2026-07-22'`, `liczbaMiejsc=2`. | Utworzenie rekordu `TRV-2026-XXXXX`. | Dodano rekord w tabeli `Rezerwacje`. | **działa** |
| **T04** | F02 - Błędne dane | Rezerwacja z `liczbaMiejsc=0`. | Odrzucenie i komunikat o błędzie. | Wyświetlono komunikat, brak zapisu. | **działa** |
| **T05** | F04 - Anulowanie | Kliknięcie "Anuluj" na liście rezerwacji. | Zmiana statusu na `'Anulowane'`. | Status rekordu zmieniono w SQLite. | **działa** |
| **T06** | Trwałość danych (Restart) | Restart serwera Flask po zmianach. | Zapisane dane pozostają w bazie. | Wszystkie dane i statusy zachowane. | **działa** |
