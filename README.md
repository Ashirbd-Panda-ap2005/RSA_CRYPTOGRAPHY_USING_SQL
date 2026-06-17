# RSA_CRYPTOGRAPHY_USING_SQL
THIS IS A SECURED CRYPTOGRAPHY SYSTEM WHICH IS DEVLPOPED BY USING MYSQL AND PYTHON.
# End-to-End RSA Cryptographic System with MySQL Integration

A secure, dependency-free multi-user communication system implementing the **RSA Asymmetric Cryptography Algorithm** combined with a relational **MySQL** storage layer. 

The architecture enforces a **Zero-Knowledge** operational flow: private decryption components remain local to the runtime environment, ensuring text records residing on the remote server can never be breached or monitored in plaintext.

## ⚙️ Core Technical Features
- **Raw Mathematical Architecture:** Contains custom implementations for prime discovery, Greatest Common Divisor calculation, and Extended Euclidean Modular Inverse solving without external cryptographic libraries.
- **Relational Data Mapping:** Connects runtime transformations directly to structured MySQL schemas utilizing `mysql-connector-python`.
- **Parameterized SQL Security:** Enforces safe binding techniques across all registration and data dispatch models to completely neutralize SQL Injection vulnerabilities.
- **Zero Precision Leakage:** Modulus components and big integer arrays are systematically serialized into relational string streams (`LONGTEXT`) to eliminate truncation data loss.

## 🛠️ Project Setup & Installation

### 1. Prerequisites
Ensure you have Python installed alongside a running MySQL local instance. Install the database driver using:


### 2. Configure Database Structure
Open your SQL management tool (like MySQL Workbench), open the `database.sql` script located in this repository, and execute it entirely to provision tables and primary constraint loops.

### 3. Connection Setup
Open `app.py` and modify lines 9 and 10 to reflect your actual MySQL setup credentials:

### 4. Execute the Application
Launch the terminal program interface using:


##5. 📊 Resume Application Metrics
If utilizing this project structure on engineering or data security application profiles, style achievements using the following metrics:
> *"Engineered an asynchronous multi-user communication system in Python using self-authored RSA asymmetric encryption routines, safely storing public PKI maps and tracking ciphertext streams in an optimized MySQL relational schema."*
