-- Crear la tabla si no existe
CREATE TABLE IF NOT EXISTS suma (
    a INT,
    b INT,
    resultado INT
);

-- Insertar datos
INSERT INTO suma (a, b, resultado) VALUES (2, 3, 5);
INSERT INTO suma (a, b, resultado) VALUES (0, 0, 0);
INSERT INTO suma (a, b, resultado) VALUES (-1, 1, 0);
