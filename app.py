from flask import Flask
from db import init_db
from controllers.oferty_controller import oferty_bp
from controllers.rezerwacje_controller import rezerwacje_bp

app = Flask(__name__)
app.secret_key = 'pitaya_secret_key_demo'

# Rejestracja kontrolerów (Blueprints)
app.register_blueprint(oferty_bp)
app.register_blueprint(rezerwacje_bp)

if __name__ == '__main__':
    init_db()  # Inicjalizuje bazę tylko jeśli plik nie istnieje
    app.run(debug=True, port=5000)
