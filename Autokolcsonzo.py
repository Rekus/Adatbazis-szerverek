#Tablak letrehozasa:
CREATE TABLE autok (
        auto_id SERIAL PRIMARY KEY,
        rendszam VARCHAR NOT NULL,
        marka TEXT NOT NULL,
        modell VARCHAR NOT NULL,
        evjarat INT NOT NULL
        elerheto BOOLEAN NOT NULL
);

CREATE TABLE ugyfelek (
        ugyfel_id SERIAL PRIMARY KEY,
        nev TEXT NOT NULL,
        telefon_szam INT NOT NULL
);

CREATE TABLE kolcsonzesek (
        kolcsonzes_id SERIAL PRIMARY KEY,
        auto_id INT REFERENCES autok(auto_id),
        ugyfel_id INT REFERENCES ugyfelek(ugyfel_id),
        kezdete date NOT NULL,
        vege date NOT NULL,
        megye text NOT NULL
);

CREATE TABLE szamlak (
        szamla_id SERIAL PRIMARY KEY,
        kolcsonzes_id INT REFERENCES kolcsonzesek(kolcsonzes_id),
        ugyfel_id INT REFERENCES ugyfelek(ugyfel_id),
        ar INT NOT NULL,
        kiallitas_datuma DATE NOT NULL,
	    fizetve BOOLEAN NOT NULL
);
#mindegyik tabla 3NF-ben van, mert mindegyiknek van egy-egy egyedi es elsodleges kulcsa, a tobbi mezo kozott nincs tranzisztiv fugges

#Adatok beszurasa:
INSERT INTO autok (rendszam, marka, modell, evjarat, elerheto) VALUES
    ('LNJ-421', 'Ford’, ‘Mondeo’, 2010, True),
    ('MTM-778', 'Peugeot’, ‘207’, 2008, True),
    ('AAHG-001', 'Toyota’, ‘X-Cross’, 2022, True),
    ('ZZH-259', 'Suzuki’, ‘Swift’, 2020, False),
    ('RTK-332', 'Audi’, ‘TT’, 2017, False),
    ('HXD-743', 'BMW’, ‘X5’, 2016, False),
    ('ZWG-568’, ‘Volkswagen’, ‘Golf’, 2004, False),
    ('BBCD’, ‘Mercedes’, ‘EQE’, 2023, False),
    ('HXD-271’, ‘Ford’, ‘Mondeo’, 2006, False);

INSERT INTO ugyfelek (nev, telefon_szam) VALUES
    ('Kis Péter’, '30-222-7685’),
    ('Nagy Piroska’, '20-435-2101’),
    ('Horváth Antal’, '70-333-9725’),
    ('Szabó Áron’, '30-654-2745’),
    ('Kovács András’, '70-947-2340’);

INSERT INTO kolcsonzesek (kezdete, vege, megye) VALUES
    ('2022-10-01’, ‘2022-11-28’, ‘Pest’),
    ('2023-09-01’, ‘2023-10-30’, ‘Baranya’),
    ('2023-12-01’, ‘2023-12-01’, 'Csongrád’),
    ('2023-11-02’, ‘2023-11-08’, ‘Pest’);

INSERT INTO szamlak (ar, kiallitas_datuma, fizetve) VALUES
    (3500, ‘2023-11-10’, True),
    (2000, ‘2023-12-01’, False),
    (5400, ‘2022-11-30’, True),
    (8000, ‘2023-10-31’, False);

#Indexek letrehozasa:
CREATE INDEX autok_rendszam_idx ON autok (rendszam);
CREATE INDEX kolcsonzesek_ugyfel_id_idx ON kolcsonzesek (ugyfel_id);
CREATE INDEX kolcsonzesek_auto_id_idx ON kolcsonzesek (auto_id);

#Ugyfelek kolcsonzesi elozmenyei:
SELECT * FROM u.nev, u.ugyfel_id, a.auto_id, k.kezdete, k.vege, k.ar
FROM ugyfelek u
JOIN  kolcsonzesek k ON u.ugyfel_id = k.ugyfel_id
JOIN autok a ON k.auto_id = a.auto_id;

#Jarmuvek elerhetosege:
SELECT * FROM a.auto_id, a.elerheto
FROM autok a
WHERE a.elerheto = True;

SELECT * FROM a.auto_id, k.vege
FROM autok a
WHERE k.vege < CURRENT DATE
JOIN kolcsonzesek k ON a.auto_id = k.auto_id;

