from tkinter import *
import sqlite3

#Verbindung zur Datenbank
connection=sqlite3.connect("to_do_liste1.1.db")
cursor=connection.cursor()

#Konfiguration des Fensters mit Tabelle und Größe
fenster = Tk()
fenster.title("To-Do-Liste")
fenster.geometry("410x322")
fenster.resizable(0,0)
fenster.iconbitmap("icon2.ico")

#In Datenbank Tabele und Spalten/Reihen festlegen
cursor.execute("""
    CREATE TABLE IF NOT EXISTS todoliste
    ('number' INT PRIMARY KEY NOT NULL AUTO INCREMENT,
    'task' TEXT,
    'date' DATE);""")

#Werte aus Textfeldern zur Datenbank hinzufügen
def hinzufügen():
    task=eingabefeld_task.get()
    date=eingabe_date.get()
    cursor.execute('''INSERT INTO todoliste (task, date) VALUES(?,?)''', (task, date
    eingabefeld_task.delete(0, END)
    eingabe_date.delete(0, END)

def auslesen():
    cursor.execute('SELECT task, date FROM todoliste')
    data = cursor.fetchall()
    i = 4
    for element in data:
        current = Checkbutton(fenster, text = element[0], font('Arial', 12))
        current.grid(0, i, 3, 2, 12.5, 10)
        i += 1

def Checkbox_loeschen():
    if (CB1.get()==1):
        cursor.execute("DELETE FROM todoliste WHERE number=?", ("1",))
    if (CB2.get()==1):
        cursor.execute("DELETE FROM todoliste WHERE number=?", ("2",))
    if (CB3.get()==1):
        cursor.execute("DELETE FROM todoliste WHERE number=?", ("3",))

#Buttons und Label festlegen
Überschrift_label = Label(fenster, text="Meine To-Do-Liste",font=("Arial", 20))
num_Label= Label(fenster, text="Num.:", font=("Arial", 12, 'italic'))
task_Label= Label(fenster, text="Aufgabe:", font=("Arial", 12, 'italic'))
date_Label= Label(fenster, text="Datum:", font=("Arial", 12, 'italic'))
eingabefeld_task = Entry(fenster, bd=5, width=20)
eingabe_date= Entry(fenster, bd=5, width=10)
hinzufügen_Button = Button(fenster, text="Hinzufügen", command=hinzufügen, font=("Arial", 12,"bold"))
speichern_Button= Button(fenster, text="speichern", command=Checkbox_loeschen, font=("Arial", 12, "bold"))

#alle Label und Buttons im Fenster anordnen
fenster.config() 
Überschrift_label.grid(column=1, row=0, padx=5, pady=5, columnspan=2)
num_Label.grid(column=0, row=1,pady=5, padx=5)
task_Label.grid(column=1, row=1,pady=5, padx=5)
date_Label.grid(column=2, row=1,pady=5, padx=5)
eingabefeld_num.grid(column=0, row=2, padx=5, pady=5)
eingabefeld_task.grid(column=1, row=2, padx=5, pady=5)
eingabe_date.grid(column=2, row=2, pady=5, padx=5)
hinzufügen_Button.grid(column=3, row=2, padx=5, pady=5)
auslesen_Button.grid(column=3, row=1, sticky=W, pady=5, padx=5)
speichern_Button.grid(column=3, row=8, sticky=W, pady=5, padx=5)

#Fenster wird immer aktualisiert und Verbindung zur Datenbank wird "geschlossen"
auslesen()
fenster.mainloop()
connection.commit()
connection.close()
