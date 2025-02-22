import tkinter as tk
import subprocess
from tkinter import messagebox

def run_Queen():
    """Jalankan program N-Queens."""
    root.destroy()
    subprocess.run(["python", "nQueen.py"])

def run_Knight():
    """Jalankan program N-Knight."""
    root.destroy()
    subprocess.run(["python", "nKnight.py"])

def run_King():
    """Jalankan program N-King."""
    root.destroy()
    subprocess.run(["python", "nKing.py"])

def quit_game():
    """Keluar dari permainan."""
    root.quit()

# Membuat jendela utama yang bersifat fullscreen
root = tk.Tk()
root.title("Game Title")

# Membuat fullscreen dan dinamis mengikuti ukuran layar
root.state('zoomed')  # Windows: Membuat aplikasi fullscreen
root.attributes('-fullscreen', True)  # Linux/MacOS: Membuat aplikasi fullscreen

# Menambahkan kanvas untuk latar belakang putih polos
canvas = tk.Canvas(root, bg="white")
canvas.pack(fill="both", expand=True)

# Menambahkan judul game di bagian atas
title_label = tk.Label(root, text="SIBLINGS CHESS", font=("Lucida Console", 50, "bold"))
title_label.place(relx=0.5, rely=0.28, anchor="center")

# Menambahkan tombol untuk memilih level dengan ukuran lebih lebar dan panjang
button_width = 36
button_height = 2
button_color = "#0D92F4"  # Warna biru untuk tombol

button1 = tk.Button(root, text="King", font=("Verdana", 16, "bold"), command=run_King, width=button_width, height=button_height, bg=button_color, fg="white")
button1.place(relx=0.5, rely=0.55, anchor="center")

button2 = tk.Button(root, text="Queen", font=("Verdana", 16, "bold"), command=run_Queen, width=button_width, height=button_height, bg=button_color, fg="white")
button2.place(relx=0.5, rely=0.65, anchor="center")

button3 = tk.Button(root, text="Knight", font=("Verdana", 16, "bold"), command=run_Knight, width=button_width, height=button_height, bg=button_color, fg="white")
button3.place(relx=0.5, rely=0.75, anchor="center")

# Menambahkan tombol "Quit" di pojok kanan bawah
quit_button = tk.Button(root, text="Quit", font=("Verdana", 12), command=quit_game)
quit_button.place(relx=0.95, rely=0.95, anchor="center")

# Menjalankan loop aplikasi Tkinter
root.mainloop()
