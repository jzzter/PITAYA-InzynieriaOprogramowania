import datetime
import random
from db import get_db

def utworz_rezerwacje(id_klienta, id_oferty, data_od, data_do, liczba_miejsc):
    if not liczba_miejsc or int(liczba_miejsc) <= 0:
        return False, "Liczba miejsc musi być większa niż 0."
    
    db = get_db()
    nr_rezerwacji = f"TRV-2026-{random.randint(10000, 99999)}"
    data_utworzenia = datetime.date.today().strftime("%Y-%m-%d")
    status = "W oczekiwaniu"

    query = """
        INSERT INTO Rezerwacje (nrRezerwacji, dataUtworzenia, status, dataOd, dataDo, liczbaMiejsc, idKlienta, idOferty)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """
    db.execute(query, (nr_rezerwacji, data_utworzenia, status, data_od, data_do, liczba_miejsc, id_klienta, id_oferty))
    db.commit()
    db.close()
    return True, nr_rezerwacji

def pobierz_rezerwacje_klienta(id_klienta):
    db = get_db()
    query = """
        SELECT r.*, o.nazwa AS nazwa_oferty, o.lokacja, o.cena 
        FROM Rezerwacje r
        JOIN Oferty o ON r.idOferty = o.idOferty
        WHERE r.idKlienta = ?
        ORDER BY r.dataUtworzenia DESC
    """
    cursor = db.execute(query, (id_klienta,))
    rezerwacje = cursor.fetchall()
    db.close()
    return rezerwacje

def anuluj_rezerwacje_w_bazie(nr_rezerwacji, id_klienta):
    db = get_db()
    cursor = db.execute("SELECT * FROM Rezerwacje WHERE nrRezerwacji = ? AND idKlienta = ?", (nr_rezerwacji, id_klienta))
    rezerwacja = cursor.fetchone()
    
    if not rezerwacja:
        db.close()
        return False, "Nie znaleziono takiej rezerwacji."
    
    if rezerwacja['status'] == 'Anulowane':
        db.close()
        return False, "Rezerwacja jest już anulowana."

    db.execute("UPDATE Rezerwacje SET status = 'Anulowane' WHERE nrRezerwacji = ?", (nr_rezerwacji,))
    db.commit() # Kluczowy FIX zapobiegający utracie danych po restarcie
    db.close()
    return True, "Rezerwacja została pomyślnie anulowana."
