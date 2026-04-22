import sqlite3

def init_db():
    conn = sqlite3.connect('nexus_vault.db')
    cursor = conn.cursor()
    # Tabla para guardar: Sitio, Usuario, Contraseña Cifrada
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS credentials (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            site TEXT NOT NULL,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def save_credential(site, user, encrypted_pass):
    conn = sqlite3.connect('nexus_vault.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO credentials (site, username, password) VALUES (?, ?, ?)', 
                   (site, user, encrypted_pass))
    conn.commit()
    conn.close()