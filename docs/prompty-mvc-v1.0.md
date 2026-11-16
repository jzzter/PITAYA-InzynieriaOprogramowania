# Prompty i Iteracja z AI - Laboratorium 04

## Prompt P1: Plan MVP i mapa MVC
Pomóż nam zaplanować MVP 1.0 projektu Biuro Turystyczne PITAYA. Cel użytkownika: znalezienie wycieczki, złożenie rezerwacji oraz podgląd i anulowanie własnych zamówień. Stos: Python 3, Flask, SQLite, HTML/CSS. Zakres MVP: F01 Przeglądanie ofert, F02 Rezerwacja wycieczki, F03 Podgląd moich rezerwacji, F04 Anulowanie rezerwacji. Dane: Tabele Użytkownicy, Klienci, Oferty, Rezerwacje, Zamówienia.

## Prompt P2: Wykonanie działającego szkieletu MVC
Wykonaj pierwszy etap planu z P1 dla Biura Turystycznego PITAYA. Wyodrębnij strukturę katalogów: controllers/, models/, templates/. Przygotuj pliki db.py oraz schema.sql. Skonfiguruj demo użytkownika (Klient: idKlienta=1, Jan Kowalski). Uruchom pierwszą ścieżkę GET /oferty.

## Prompt P3: Implementacja funkcji F02 (Rezerwacja)
W aktualnym kodzie projektu PITAYA wykonaj wyłącznie funkcję F02 - Rezerwacja imprezy turystycznej. Zalogowany Klient idKlienta=1. Dane wejściowe: idOferty, dataOd, dataDo, liczbaMiejsc. Reguły: sprawdź liczbaMiejsc > 0, wygeneruj nr TRV-2026-XXXXX, użyj zapytań parametryzowanych.

## Prompt P4: Naprawa błędu zapisu/anulowania (P4)
Problem: Po anulowaniu rezerwacji (F04) i ponownym uruchomieniu aplikacji, status rezerwacji wraca do pierwotnego stanu 'W oczekiwaniu'.
Przyczyna: Brak conn.commit() po zapytaniu UPDATE Rezerwacje SET status = 'Anulowane' w models/rezerwacja.py.
Poprawka: Dodano conn.commit() oraz zabezpieczono init_db() przed ponownym czyszczeniem bazy.
