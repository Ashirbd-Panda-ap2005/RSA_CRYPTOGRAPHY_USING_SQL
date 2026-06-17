
CREATE DATABASE IF NOT EXISTS secure_crypto_db;
USE secure_crypto_db;

CREATE TABLE IF NOT EXISTS users_pki (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL UNIQUE,
    public_key_e INT NOT NULL,
    public_key_n TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE IF NOT EXISTS encrypted_messages (
    message_id INT AUTO_INCREMENT PRIMARY KEY,
    sender VARCHAR(100) NOT NULL,
    receiver VARCHAR(100) NOT NULL,
    ciphertext_payload LONGTEXT NOT NULL, 
    sent_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
