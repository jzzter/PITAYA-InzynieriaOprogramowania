from db import get_db

def pobierz_wszystkie_oferty(kierunek=None):
    db = get_db()
    if kierunek:
        query = "SELECT * FROM Oferty WHERE lokacja LIKE ? OR nazwa LIKE ?"
        cursor = db.execute(query, (f'%{kierunek}%', f'%{kierunek}%'))
    else:
        cursor = db.execute("SELECT * FROM Oferty")
    oferty = cursor.fetchall()
    db.close()
    return oferty

def pobierz_oferte_po_id(id_oferty):
    db = get_db()
    cursor = db.execute("SELECT * FROM Oferty WHERE idOferty = ?", (id_oferty,))
    oferta = cursor.fetchone()
    db.close()
    return oferta
