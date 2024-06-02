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
fenster.iconbitmap("X:\Consi\Programmieren\Python\To-Do-Liste\icon2.ico")

#In Datenbank Tabele und Spalten/Reihen festlegen
cursor.execute("""
    CREATE TABLE IF NOT EXISTS todoliste
    ('number' INT PRIMARY KEY NOT NULL,
    'task' TEXT,
    'date' DATE);""")

#Werte aus Textfeldern zur Datenbank hinzufügen
def hinzufügen():
    Va_num=eingabefeld_num.get()
    Va_task=eingabefeld_task.get()
    Va_date=eingabe_date.get()
    VA= [Va_num, Va_task, Va_date]
    cursor.execute("""
    INSERT INTO todoliste (number,task, date)
    VALUES(?,?,?);""", VA)
    eingabefeld_num.delete(0, END)
    eingabefeld_task.delete(0, END)
    eingabe_date.delete(0, END)

def Datenbank_auslesen():
    global CB1
    CB1=IntVar()
    global CB2
    CB2=IntVar()
    global CB3
    CB3=IntVar()
    cursor.execute("""
    SELECT task, date FROM todoliste WHERE number=?""", ("1"))
    CB1_W=cursor.fetchall()
    cursor.execute("""
    SELECT task, date FROM todoliste WHERE number=?""", ("2"))
    CB2_W=cursor.fetchall()
    cursor.execute("""
    SELECT task, date FROM todoliste WHERE number=?""", ("3"))
    CB3_W=cursor.fetchall()
    Checkbox1=Checkbutton(fenster, variable=CB1, text=CB1_W, font=("Arial", 12))
    Checkbox2=Checkbutton(fenster, variable=CB2, text=CB2_W, font=("Arial", 12))
    Checkbox3=Checkbutton(fenster, variable=CB3, text=CB3_W, font=("Arial", 12))
    Checkbox1.grid(column=0, row=4, columnspan=3, sticky=W, padx=12.5, pady=10)
    Checkbox2.grid(column=0, row=5, columnspan=3, sticky=W, padx=12.5, pady=10)
    Checkbox3.grid(column=0, row=6, columnspan=3, sticky=W, padx=12.5, pady=10)

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
eingabefeld_num= Entry(fenster, bd=5, width=5)
eingabefeld_task = Entry(fenster, bd=5, width=20)
eingabe_date= Entry(fenster, bd=5, width=10)
hinzufügen_Button = Button(fenster, text="Hinzufügen", command=hinzufügen, font=("Arial", 12,"bold"))
auslesen_Button= Button(fenster, text="auslesen", command=Datenbank_auslesen, font=("Arial", 12, "bold"))
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
fenster.mainloop()
connection.commit()
connection.close()