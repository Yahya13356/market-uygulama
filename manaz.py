import tkinter as tk
from tkinter import messagebox

katalog = {
    "ceviz": 30,
    "pastırma": 100,
    "muz": 28
}

def hesapla():
    try:
        kilo = int(kilo_entry.get())
        urun = urun_entry.get().lower()

        if urun not in katalog:
            messagebox.showerror("Hata", "Ürün bulunamadı!")
            return

        tutar = katalog[urun] * kilo
        sonuc_label.config(
            text=f"💰 Toplam Tutar: {tutar} TL",
            fg="#00ff88"
        )

    except:
        messagebox.showerror("Hata", "Lütfen geçerli bilgiler gir!")

pencere = tk.Tk()
pencere.title("Market Otomasyonu")
pencere.geometry("500x400")
pencere.configure(bg="#1e1e1e")

baslik = tk.Label(
    pencere,
    text="🛒 MARKET KASASI 🛒",
    font=("Arial", 22, "bold"),
    bg="#1e1e1e",
    fg="gold"
)
baslik.pack(pady=15)

kampanya = tk.Label(
    pencere,
    text="🔥 PASTIRMA SADECE 100 TL 🔥",
    font=("Arial", 14),
    bg="#1e1e1e",
    fg="red"
)
kampanya.pack()

frame = tk.Frame(
    pencere,
    bg="#2d2d2d",
    padx=20,
    pady=20
)
frame.pack(pady=20)

tk.Label(
    frame,
    text="Ürün Adı",
    bg="#2d2d2d",
    fg="white"
).pack()

urun_entry = tk.Entry(
    frame,
    font=("Arial", 12),
    width=20
)
urun_entry.pack(pady=5)

tk.Label(
    frame,
    text="Kilo",
    bg="#2d2d2d",
    fg="white"
).pack()

kilo_entry = tk.Entry(
    frame,
    font=("Arial", 12),
    width=20
)
kilo_entry.pack(pady=5)

hesapla_btn = tk.Button(
    frame,
    text="💵 HESAPLA",
    font=("Arial", 12, "bold"),
    bg="#00aa55",
    fg="white",
    padx=15,
    pady=5,
    command=hesapla
)
hesapla_btn.pack(pady=15)

sonuc_label = tk.Label(
    pencere,
    text="",
    font=("Arial", 18, "bold"),
    bg="#1e1e1e"
)
sonuc_label.pack()

def odeme_yap():
    try:
        kilo = int(kilo_entry.get())
        urun = urun_entry.get().lower()

        if urun not in katalog:
            messagebox.showerror("Hata", "Ürün bulunamadı!")
            return

        tutar = katalog[urun] * kilo
        verilen = int(para_entry.get())

        if verilen == tutar:
            sonuc_label.config(
                text="✅ Teşekkürler, ürün sizin!",
                fg="lime"
            )

        elif verilen < tutar:
            sonuc_label.config(
                text=f"❌ {tutar-verilen} TL eksik ödeme yaptınız!",
                fg="red"
            )

        else:
            sonuc_label.config(
                text=f"💸 Para üstünüz: {verilen-tutar} TL",
                fg="cyan"
            )

    except ValueError:
        messagebox.showerror("Hata", "Lütfen sayıları doğru girin!")

tk.Label(frame, text="Verilen Para", bg="#2d2d2d", fg="white").pack()

para_entry = tk.Entry(frame)
para_entry.pack(pady=5)


tk.Button(
    frame,
    text="💵 ÖDEME YAP",
    command=odeme_yap
).pack(pady=10)






pencere.mainloop()

