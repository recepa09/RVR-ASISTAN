import customtkinter as ctk
import tkinter.messagebox as tkmb
import sqlite3

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Kayıt işlemi için gerekli değişkenleri tanımla
user_entry = None
user_pass = None

# Yeni pencereyi oluştur
new_window = ctk.CTk()
new_window.geometry("400x400")
new_window.title("Kayıt İşlemi")

# Kayıt işlemini tamamlamak için gerekli metin kutularını ve butonları ekle

ad_entry = ctk.CTkEntry(master=new_window, placeholder_text="Ad")
ad_entry.pack(pady=12, padx=10)

soyad_entry = ctk.CTkEntry(master=new_window, placeholder_text="Soyad")
soyad_entry.pack(pady=12, padx=10)

kullanici_adi_entry = ctk.CTkEntry(master=new_window, placeholder_text="Kullanıcı Adı")
kullanici_adi_entry.pack(pady=12, padx=10)

sifre_entry = ctk.CTkEntry(master=new_window, placeholder_text="Şifre", show="*")
sifre_entry.pack(pady=12, padx=10)

# Kayıt butonu
kayit_button = ctk.CTkButton(master=new_window, text="Kayıt Ol", command=lambda: register())
kayit_button.pack(pady=12, padx=10)

# Kayıt işlemini gerçekleştiren fonksiyon
def register():
    global user_entry, user_pass

    # Kullanıcı adı ve şifreyi al
    kullanici_adi = kullanici_adi_entry.get()
    sifre = sifre_entry.get()
    isim=ad_entry.get()
    soyad = soyad_entry.get()

    # Kullanıcı adı boşsa uyarı ver
    if kullanici_adi == "":
        tkmb.showinfo(title="Uyarı", message="Lütfen bilgilerinizi kontrol ediniz boş alan bırakmayınız !!!")
        return

    # Şifre boşsa uyarı ver
    if sifre == "":
        tkmb.showinfo(title="Uyarı", message="Lütfen şifre giriniz.")
        return

    # Veritabanından bağlantıyı aç
    global conn1
    try:
        conn = sqlite3.connect('rvr_assistant.db', isolation_level="EXCLUSIVE")
    except sqlite3.OperationalError as e:
        tkmb.showinfo(title="Hata", message="Veritabanı kilitli. Lütfen daha sonra tekrar deneyin.")
        return

    cursor = conn.cursor()

    # Kullanıcı adı veritabanında var mı kontrol et
    cursor.execute("SELECT username FROM users WHERE username = ?", (kullanici_adi,))
    result = cursor.fetchone()

    # Kullanıcı adı veritabanında varsa uyarı ver
    if result is not None:
        tkmb.showinfo(title="Hata", message="Bu kullanıcı zaten kayıtlı.")
        return

    # Kullanıcı adı ve şifreyi veritabanına ekle
    cursor.execute('INSERT INTO users (username, password,firstName,lastName) VALUES (?, ?,?,?)', (kullanici_adi, sifre,isim,soyad))
    conn.commit()

    tkmb.showinfo(title="Kayıt Başarılı", message="Kayıt işleminiz başarıyla tamamlandı.")
    new_window.destroy()


# Ana pencereyi çalıştır
new_window.mainloop()