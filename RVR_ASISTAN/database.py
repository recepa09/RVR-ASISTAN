import sqlite3


def create_connection():
    conn = sqlite3.connect('rvr_assistant.db')
    return conn

def create_user_table(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT,
            firstName TEXT,
            lastName TEXT
        )
    ''')
    conn.commit()

def add_user(conn, username, password, firstName, lastName):
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users VALUES (?, ?, ?, ?)', (username, password, firstName, lastName))
    conn.commit()

def check_user_credentials(conn, username, password):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    row = cursor.fetchone()
    return row is not None

def main():
    conn = create_connection()  # Bağlantıyı create_connection() fonksiyonuyla oluştur
    create_user_table(conn)  # users tablosunu oluştur
    add_user(conn, "rvr", "rvr", "Test", "User")  # Kullanıcı ekle
    conn.close()

if __name__ == "__main__":
    main()
