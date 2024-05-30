import tkinter as tk
from tkinter import ttk as tema
from tkinter.messagebox import showinfo, showerror
import ttkbootstrap as tb

root = tb.Window(themename="solar")

# Variabel untuk menyimpan input pengguna
nama = tk.StringVar()
kelas = tk.IntVar()
jk = tk.StringVar()
ba = tk.StringVar()
setuju = tk.BooleanVar()

def kirim():
    if not nama.get():
        showerror(title="Error", message="Nama harus diisi!")
        return
    if not kelas.get():
        showerror(title="Error", message="Kelas harus diisi!")
        return
    if not jk.get():
        showerror(title="Error", message="Jenis kelamin harus dipilih!")
        return
    if not ba.get():
        showerror(title="Error", message="Proyek bahasa asing harus dipilih!")
        return
    if not setuju.get():
        showerror(title="Error", message="Anda harus menyetujui untuk mengerjakan Project Akhir!")
        return
    
    stj = "bersedia" if setuju.get() else "tidak bersedia"
    hasil = (
        f"Nama: {nama.get()}\n"
        f"Jenis Kelamin: {jk.get()}\n"
        f"Kelas: {kelas.get()}\n"
        f"Proyek Bahasa Asing: {ba.get()}\n"
        f"Persetujuan: {stj}"
    )
    showinfo(title="BIO", message=hasil)

root.title("Formulir Pendaftaran")
root.geometry("400x500")
root.resizable(False, False)
root.config(bg="gray")

frame = tema.Frame(root)
frame.pack(padx=10, fill="x", expand=True)

labelNama = tema.Label(frame, text="Nama:")
labelNama.pack(padx=10, fill="x", expand=True)
formNama = tema.Entry(frame, textvariable=nama)
formNama.pack(padx=10, fill="x", expand=True)

labelKelas = tema.Label(frame, text="Kelas:")
labelKelas.pack(padx=10, fill="x", expand=True)
formKelas = tema.Entry(frame, textvariable=kelas)
formKelas.pack(padx=10, fill="x", expand=True)

labelJK = tema.Label(frame, text="Jenis Kelamin:", font=("arial", 12, 'bold'))
labelJK.pack(padx=10, fill="x", expand=True)
formJK = tema.Combobox(frame, textvariable=jk, values=["laki-laki", "perempuan"])
formJK.pack(padx=10, fill="x", expand=True)
formJK.current(0)

labelBA = tema.Label(frame, text="Proyek Bahasa Asing:")
labelBA.pack(padx=10, fill="x", expand=True)
ba1 = tema.Radiobutton(frame, value="dkv", text="DKV", variable=ba)
ba1.pack(padx=10, fill="x", expand=True)
ba2 = tema.Radiobutton(frame, value="coding", text="Coding", variable=ba)
ba2.pack(padx=10, fill="x", expand=True)

stj = tema.Checkbutton(frame, variable=setuju, text="Saya setuju mengerjakan Project Akhir...", onvalue=1, offvalue=0)
stj.pack(padx=10, fill="x", expand=True)

BTN = tema.Button(frame, text="Kirim", command=kirim)
BTN.pack(padx=10, fill="x", expand=True)

root.mainloop()