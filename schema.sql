DROP TABLE IF EXISTS Rezerwacje;
DROP TABLE IF EXISTS Oferty;
DROP TABLE IF EXISTS Klienci;
DROP TABLE IF EXISTS Uzytkownicy;

CREATE TABLE Uzytkownicy (
    idUzytkownika INTEGER PRIMARY KEY AUTOINCREMENT,
    email VARCHAR(100) NOT NULL,
    haslo VARCHAR(100) NOT NULL,
    imie VARCHAR(60) NOT NULL,
    nazwisko VARCHAR(60) NOT NULL
);

CREATE TABLE Klienci (
    idKlienta INTEGER PRIMARY KEY AUTOINCREMENT,
    telefon VARCHAR(12),
    ulica VARCHAR(100) NOT NULL,
    nrDomu INTEGER NOT NULL,
    nrLokalu INTEGER,
    kodPocztowy VARCHAR(6) NOT NULL,
    miasto VARCHAR(60) NOT NULL,
    idUzytkownika INTEGER,
    FOREIGN KEY (idUzytkownika) REFERENCES Uzytkownicy(idUzytkownika)
);

CREATE TABLE Oferty (
    idOferty INTEGER PRIMARY KEY AUTOINCREMENT,
    nazwa VARCHAR(100) NOT NULL,
    opis VARCHAR(400) NOT NULL,
    lokacja VARCHAR(100) NOT NULL,
    cena DECIMAL(6,2) NOT NULL,
    iloscDni INTEGER NOT NULL,
    iloscNocy INTEGER NOT NULL
);

CREATE TABLE Rezerwacje (
    nrRezerwacji VARCHAR(14) PRIMARY KEY,
    dataUtworzenia DATE NOT NULL,
    status VARCHAR(60) NOT NULL,
    dataOd DATE NOT NULL,
    dataDo DATE NOT NULL,
    liczbaMiejsc INTEGER NOT NULL,
    idKlienta INTEGER NOT NULL,
    idOferty INTEGER NOT NULL,
    FOREIGN KEY (idKlienta) REFERENCES Klienci(idKlienta),
    FOREIGN KEY (idOferty) REFERENCES Oferty(idOferty)
);

-- Dane początkowe (Demo Klient nr 1 i przykładowe oferty)
INSERT INTO Uzytkownicy (idUzytkownika, email, haslo, imie, nazwisko) 
VALUES (1, 'jan.kowalski@example.com', '123', 'Jan', 'Kowalski');

INSERT INTO Klienci (idKlienta, telefon, ulica, nrDomu, nrLokalu, kodPocztowy, miasto, idUzytkownika)
VALUES (1, '+48123456789', 'Konopnicka', 4, 3, '10-719', 'Olsztyn', 1);

INSERT INTO Oferty (idOferty, nazwa, opis, lokacja, cena, iloscDni, iloscNocy) VALUES
(1, 'Słoneczna Hiszpania', '7 dni all-inclusive w Barcelonie. Wylot z Warszawy.', 'Barcelona, Hiszpania', 2500.00, 7, 6),
(2, 'Egzotyczna Tajlandia', '10 dni w Bangkoku i na wyspach. Wylot z Krakowa.', 'Tajlandia', 5800.00, 10, 9),
(3, 'Włoskie Alpy', '5 dni na nartach w Dolomitach. Wylot z Gdańska.', 'Dolomity, Włochy', 3200.00, 5, 4);
