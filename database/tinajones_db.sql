-- Base de datos: Monitoreo de nivel hidrico - Reservorio Tinajones
CREATE DATABASE IF NOT EXISTS tinajones_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE tinajones_db;

DROP TABLE IF EXISTS estacion_hidrica;
CREATE TABLE estacion_hidrica (
    id INT AUTO_INCREMENT PRIMARY KEY,
    compuerta VARCHAR(50) NOT NULL,
    porcentaje_llenado DECIMAL(5,2) NOT NULL,
    caudal_m DECIMAL(10,2) NOT NULL,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
-- Nota: mensaje_alerta NO es columna; se evalua en Python y se muestra en pantalla.

DROP PROCEDURE IF EXISTS sp_listar_estaciones;
DROP PROCEDURE IF EXISTS sp_registrar_estacion;

DELIMITER $$

CREATE PROCEDURE sp_listar_estaciones(IN p_busqueda VARCHAR(100))
BEGIN
    SELECT id, compuerta, porcentaje_llenado, caudal_m
    FROM estacion_hidrica
    WHERE compuerta LIKE CONCAT('%', p_busqueda, '%')
       OR CAST(porcentaje_llenado AS CHAR) LIKE CONCAT('%', p_busqueda, '%')
       OR CAST(caudal_m AS CHAR) LIKE CONCAT('%', p_busqueda, '%')
    ORDER BY id DESC;
END$$

CREATE PROCEDURE sp_registrar_estacion(
    IN p_compuerta VARCHAR(50),
    IN p_porcentaje DECIMAL(5,2),
    IN p_caudal DECIMAL(10,2)
)
BEGIN
    INSERT INTO estacion_hidrica (compuerta, porcentaje_llenado, caudal_m)
    VALUES (p_compuerta, p_porcentaje, p_caudal);
END$$

DELIMITER ;
