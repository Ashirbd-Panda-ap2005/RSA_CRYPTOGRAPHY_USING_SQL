import mysql.connector
from mysql.connector import Error
import crypto

def get_db_connection():
    """Establishes connection to the local MySQL server."""
    return mysql.connector.connect(
        host="localhost",
        user="root",          -- TODO: Change to your MySQL username
        password="password",  -- TODO: Change to your MySQL password
        database="secure_crypto_db"
    )

def register_user(username):
    """Generates RSA keypair for a user and registers public parts in the database."""
    pub_key, priv_key = crypto.generate_rsa_keys()
    e, n = pub_key
    
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        query = "INSERT INTO users_pki (username, public_key_e, public_key_n) VALUES (%s, %s, %s)"
        cursor.execute(query, (username, e, str(n)))
        conn.commit()
        
        print(f"\n[+] User '{username}' registered successfully!")
        print(f"!!! SAVE YOUR PRIVATE KEY SECURELY (It is never stored in DB) -> d: {priv_key[0]}, n: {priv_key[1]}")
        
    except Error as err:
        print(f"[-] Database Error: {err}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def send_encrypted_message(sender, receiver, message):
    """Fetches receiver's public key from MySQL, encrypts text, and logs payload."""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Fetch target's public keys
        cursor.execute("SELECT public_key_e, public_key_n FROM users_pki WHERE username = %s", (receiver,))
        result = cursor.fetchone()
        
        if not result:
            print(f"[-] Error: Receiver '{receiver}' not found in the PKI directory.")
            return
            
        public_key = (result[0], int(result[1]))
        
        # Encrypt plaintext
        ciphertext = crypto.encrypt(message, public_key)
        
        # Store securely inside longtext data field
        query = "INSERT INTO encrypted_messages (sender, receiver, ciphertext_payload) VALUES (%s, %s, %s)"
        cursor.execute(query, (sender, receiver, ciphertext))
        conn.commit()
        print(f"[+] Encrypted message successfully sent to '{receiver}'!")
        
    except Error as err:
        print(f"[-] Database Error: {err}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def read_messages(username, d_key, n_key):
    """Fetches ciphertexts from MySQL and prints them out in cleartext."""
    private_key = (int(d_key), int(n_key))
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT sender, ciphertext_payload FROM encrypted_messages WHERE receiver = %s", (username,))
        records = cursor.fetchall()
        
        if not records:
            print("\n--- No messages found for this user ---")
            return
            
        print(f"\n--- Secure Mailbox for {username} ---")
        for row in records:
            sender = row[0]
            ciphertext = row[1]
            try:
                decrypted_msg = crypto.decrypt(ciphertext, private_key)
                print(f"From [{sender}]: {decrypted_msg}")
            except Exception:
                print(f"From [{sender}]: [Decryption Failed - Invalid Private Key Provided]")
                
    except Error as err:
        print(f"[-] Database Error: {err}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def main():
    while True:
        print("\n=== RSA-MYSQL CRYPTO MESSENGER ===")
        print("1. Register New User (Generate PKI Keys)")
        print("2. Send Encrypted Message")
        print("3. Read & Decrypt My Messages")
        print("4. Exit")
        choice = input("Select an option (1-4): ")
        
        if choice == "1":
            user = input("Enter unique username to create: ")
            register_user(user)
        elif choice == "2":
            sender = input("Your username: ")
            receiver = input("Receiver username: ")
            msg = input("Type your secret message: ")
            send_encrypted_message(sender, receiver, msg)
        elif choice == "3":
            user = input("Your username: ")
            print("To decrypt your incoming messages, input your local private keys:")
            d = input("Enter Private Exponent (d): ")
            n = input("Enter Modulus (n): ")
            read_messages(user, d, n)
        elif choice == "4":
            print("System shutting down. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
