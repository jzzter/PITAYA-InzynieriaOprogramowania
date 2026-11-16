from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.oferta import pobierz_oferte_po_id
from models.rezerwacja import utworz_rezerwacje, pobierz_rezerwacje_klienta, anuluj_rezerwacje_w_bazie

rezerwacje_bp = Blueprint('rezerwacje', __name__)
DEMO_KLIENT_ID = 1  # Wymagany użytkownik demonstracyjny

@rezerwacje_bp.route('/rezerwuj/<int:id_oferty>', methods=['GET', 'POST'])
def formularz_rezerwacji(id_oferty):
    oferta = pobierz_oferte_po_id(id_oferty)
    if request.method == 'POST':
        data_od = request.form.get('dataOd')
        data_do = request.form.get('dataDo')
        liczba_miejsc = request.form.get('liczbaMiejsc')
        
        sukces, wynik = utworz_rezerwacje(DEMO_KLIENT_ID, id_oferty, data_od, data_do, liczba_miejsc)
        if sukces:
            return redirect(url_for('rezerwacje.potwierdzenie', nr=wynik))
        else:
            flash(wynik, 'danger')

    return render_template('rezerwacje/formularz.html', oferta=oferta)

@rezerwacje_bp.route('/potwierdzenie')
def potwierdzenie():
    nr_rezerwacji = request.args.get('nr')
    return render_template('rezerwacje/potwierdzenie.html', nr_rezerwacji=nr_rezerwacji)

@rezerwacje_bp.route('/moje-rezerwacje')
def moje_rezerwacje():
    rezerwacje = pobierz_rezerwacje_klienta(DEMO_KLIENT_ID)
    return render_template('rezerwacje/moje_rezerwacje.html', rezerwacje=rezerwacje)

@rezerwacje_bp.route('/moje-rezerwacje/anuluj/<nr_rezerwacji>', methods=['POST'])
def anuluj_rezerwacje(nr_rezerwacji):
    sukces, komunikat = anuluj_rezerwacje_w_bazie(nr_rezerwacji, DEMO_KLIENT_ID)
    flash(komunikat, 'success' if sukces else 'danger')
    return redirect(url_for('rezerwacje.moje_rezerwacje'))
