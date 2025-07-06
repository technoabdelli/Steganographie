import tkinter as tk
from tkinter import filedialog
from PIL import Image

def daten_aus_bild_extrahieren(bild_pfad):
    try:
        bild = Image.open(bild_pfad)
        binary_daten = ""
        versteckte_nachricht = ""

        for pixel in bild.getdata():
            r, g, b = pixel[:3]
            binary_daten += bin(r)[-1]
            binary_daten += bin(g)[-1]
            binary_daten += bin(b)[-1]

            while len(binary_daten) >= 8:
                byte = binary_daten[:8]
                binary_data = binary_daten[8:]
                char = chr(int(byte, 2))
                versteckte_nachricht += char
                if versteckte_nachricht.endswith("#"):
                    break
        return "[Keine Daten gefunden]"
    except Exception as e:
        return f"[Fehler gefunden als: {e}]"

def bild_ofnen():
    bild_pfad = filedialog.askopenfilename(filetypes=[("PNG files", "*.png")])
    if bild_pfad:
        msg = daten_aus_bild_extrahieren(bild_pfad)
        text_output.config(state=tk.NORMAL)
        text_output.delete("1.0", tk.END)
        text_output.insert(tk.END, msg)
        text_output.config(state=tk.DISABLED)

fenster = tk.Tk()
fenster.title("Steganographie-Extract")
fenster.geometry("500x300")
title_label = tk.Label(fenster, text=" Steganographie: Daten aus Bild extrahieren", font=("Arial", 14))
title_label.pack(pady=10)
ofnen_button = tk.Button(fenster, text="Bild auswählen", command=bild_ofnen, font=("Arial", 12))
ofnen_button.pack(pady=10)
text_output = tk.Text(fenster, height=10, width=60, wrap=tk.WORD, state=tk.DISABLED)
text_output.pack(pady=10)

fenster.mainloop()
