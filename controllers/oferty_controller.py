from flask import Blueprint, render_template, request
from models.oferta import pobierz_wszystkie_oferty, pobierz_oferte_po_id

oferty_bp = Blueprint('oferty', __name__)

@oferty_bp.route('/')
@oferty_bp.route('/oferty')
def lista_ofert():
    kierunek = request.args.get('kierunek', '').strip()
    oferty = pobierz_wszystkie_oferty(kierunek if kierunek else None)
    return render_template('oferty/lista.html', oferty=oferty, wyszukane=kierunek)

@oferty_bp.route('/oferty/<int:id_oferty>')
def szczegoly_oferty(id_oferty):
    oferta = pobierz_oferte_po_id(id_oferty)
    if not oferta:
        return "Nie znaleziono oferty", 404
    return render_template('oferty/szczegoly.html', oferta=oferta)
