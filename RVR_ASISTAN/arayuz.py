import importlib
import os
import sys

import customtkinter as ctk
import tkinter.messagebox as tkmb
import sqlite3

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


for mod in sys.modules.keys():
    if mod.startswith('customtkinter'):
        importlib.import_module(mod)

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("400x400")
        self.title("RVR ASİSTAN")

        self.label = ctk.CTkLabel(self, text="RVR Asistana Hoş Geldiniz.")
        self.label.pack(pady=20)

        self.frame = ctk.CTkFrame(self)
        self.frame.pack(pady=20, padx=40, fill='both', expand=True)

        self.label_giris = ctk.CTkLabel(self.frame, text='GİRİŞ')
        self.label_giris.pack(pady=12, padx=10)

        self.user_entry = ctk.CTkEntry(self.frame, placeholder_text="Kullanıcı Adı")
        self.user_entry.pack(pady=12, padx=10)

        self.user_pass = ctk.CTkEntry(self.frame, placeholder_text="Şifre", show="*")
        self.user_pass.pack(pady=12, padx=10)

        self.button = ctk.CTkButton(self.frame, text='Giriş', command=self.login)
        self.button.pack(pady=12, padx=10)

        self.kaydol_buton = ctk.CTkButton(self.frame, text='Kayıt Ol', command=self.kaydol)
        self.kaydol_buton.pack(pady=12, padx=10)

    def login(self):
        username = self.user_entry.get()
        password = self.user_pass.get()

        if username == "" or password == "":
            tkmb.showinfo(title="Uyarı", message="Lütfen bilgilerinizi kontrol ediniz boş alan bırakmayınız !!!")
            return

        conn = sqlite3.connect('rvr_assistant.db')  # Veritabanına bağlan

        def check_user_credentials(username, password):
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
            row = cursor.fetchone()
            return row is not None

        is_logged_in = check_user_credentials(username, password)

        if is_logged_in:
            # Başarılı giriş
            # Burada veritabanından alınan verilerle arayüzü güncelleyebilir veya diğer işlemleri yapabilirsiniz.
            self.main_window = ctk.CTk()  # Yeni pencereyi giriş işleminin dışında oluşturuyoruz
            self.main_window.geometry("400x400")
            self.main_window.title("RVR ASİSTAN")

            def start_main_app():
                os.system("python " + os.path.join(os.getcwd(), "main.py"))

            button = ctk.CTkButton(master=self.main_window, text='Konuşmaya Başla', command=start_main_app)
            button.pack(pady=20)

            self.main_window.mainloop()
        else:
            # Geçersiz kimlik bilgileri
            tkmb.showerror(title="Giriş Başarısız", message="Kullanıcı adı veya şifre yanlış!")

        conn.close()  # Veritabanı bağlantısını kapat

    def kaydol(self):
        os.system("python " + os.path.join(os.getcwd(), "kayit_ol.py"))


app = App()
app.mainloop()
