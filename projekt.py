from tkinter import*

def spremi_biljesku():
    a = unos.get()
    if a.strip():
        with open("biljeznica.txt", "a") as f:
            f.write(a)
            f.write("\n")
        poruka.config(text="Bilješka spremljena!")
        unos.delete(0, END)
    else:
        poruka.config(text="Unesi tekst!")

def pregled_biljeski():
    with open("biljeznica.txt", "r") as datoteka:
                sadrzaj = datoteka.read()
                if not sadrzaj.strip():
                    prikaz.insert(END, "Datoteka ne sadrži bilješke!")
                else:
                    prikaz.insert(END, sadrzaj)
#Stvaranje prozora
prozor=Tk()
prozor.title("Jednostavna bilježnica")
prozor.geometry("300x300")

# Naslov iznad unosa
label_unosa=Label(prozor, text="Ovdje upišite bilješku:")
label_unosa.pack()

#Unos bilješke
unos=Entry(prozor,width=40)
unos.pack(pady=10)

#Label za poruke
poruka=Label(prozor, text="")
poruka.pack()

#Polje za prikaz bilješki
prikaz=Text(prozor, width=35, height=5)
prikaz.pack(pady=10)

#Gumb za dodavanje bilješke
gumb1=Button(prozor, text="Dodaj bilješku", command=spremi_biljesku)
gumb1.pack(pady=5)

#Gumb za pregled bilješki
gumb2=Button(prozor, text="Pregledaj bilješke", command=pregled_biljeski)
gumb2.pack(pady=5)

# Gumb za izlaz
gumb3=Button(prozor, text="Izlaz", command=prozor.destroy)
gumb3.pack(pady=5)

