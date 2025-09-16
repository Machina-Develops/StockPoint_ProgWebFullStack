-- schema.sql  (MySQL 8+)
CREATE DATABASE IF NOT EXISTS stockpoint
  DEFAULT CHARACTER SET utf8mb4
  DEFAULT COLLATE utf8mb4_unicode_ci;

USE stockpoint;

CREATE TABLE IF NOT EXISTS usuarios (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombre_usuario VARCHAR(50) NOT NULL UNIQUE,
  email VARCHAR(120) NOT NULL UNIQUE,
  contrasena_hash CHAR(64) NOT NULL, -- SHA-256 hex
  rol ENUM('administrador','estandar') NOT NULL DEFAULT 'estandar',
  creado_en TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Admin inicial (user: admin / pass: Admin123)
INSERT INTO usuarios (nombre_usuario, email, contrasena_hash, rol)
SELECT 'admin', 'admin@sistema.com',
       '3b612c75a7b5048a435fb6ec81e52ff92d6d795a8b5a9c17070f6a63c97a53b2', -- SHA-256("Admin123")
       'administrador'
WHERE NOT EXISTS (SELECT 1 FROM usuarios WHERE nombre_usuario = 'admin');
