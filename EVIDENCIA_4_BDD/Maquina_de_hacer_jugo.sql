CREATE TABLE MaquinaJuguera (
    id INT PRIMARY KEY AUTO_INCREMENT,
    capacidad_max_jarra INT NOT NULL,
    encendida BOOLEAN NOT NULL DEFAULT FALSE,
    potencia INT NOT NULL DEFAULT 0,
    jugo_en_jarra INT NOT NULL DEFAULT 0,
    CHECK (potencia >= 0 AND potencia <= 100),
    CHECK (jugo_en_jarra >= 0 AND jugo_en_jarra <= capacidad_max_jarra)
);

INSERT INTO MaquinaJuguera (capacidad_max_jarra, encendida, potencia, jugo_en_jarra) VALUES
(1000, FALSE, 0, 0),
(1500, TRUE, 50, 750),
(2000, FALSE, 75, 1500),
(1200, TRUE, 25, 300),
(1800, FALSE, 0, 1800),
(2500, TRUE, 100, 2000),
(1000, TRUE, 60, 500),
(3000, FALSE, 80, 2500),
(1700, TRUE, 40, 800),
(2200, FALSE, 90, 1100);


SELECT * FROM MaquinaJuguera WHERE encendida = TRUE;

SELECT * FROM MaquinaJuguera ORDER BY capacidad_max_jarra DESC LIMIT 1;

SELECT AVG(jugo_en_jarra) as promedio_jugo FROM MaquinaJuguera;

SELECT * FROM MaquinaJuguera WHERE jugo_en_jarra > (capacidad_max_jarra * 0.5);

SELECT COUNT(*) as maquinas_alta_potencia FROM MaquinaJuguera WHERE potencia > 75;