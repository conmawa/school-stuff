from tkinter import *
import sqlite3
import customtkinter as ctk

#Verbindung zur Datenbank
connection = sqlite3.connect("to-do.db")
cursor = connection.cursor()

#Konfiguration des Fensterns mit Tabelle und Größe
window = ctk.CTk()
window.title("To-Do-Liste")
window.geometry("600x400")
window.resizable(1,1)

#In Datenbank Tabele und Spalten/Reihen festlegen
cursor.execute("""CREATE TABLE IF NOT EXISTS todoliste ('task_id' INTEGER PRIMARY KEY AUTOINCREMENT, 'task' TEXT, 'date' DATE)""")

#Werte aus Textfeldern zur Datenbank hinzufügen
def add_task():
    task = input_task.get()
    date = input_date.get()
    
    cursor.execute('''INSERT INTO todoliste (task, date) VALUES(?,?)''', (task, date))
    
    input_task.delete(0, END)
    input_date.delete(0, END)
    
    read_database()

def read_database():
    for widget in window.grid_slaves():
        if int(widget.grid_info()["row"]) >= 4:
            widget.destroy()
            
    cursor.execute('SELECT task_id, task, date FROM todoliste')
    data = cursor.fetchall()
    
    global checkbuttons 
    checkbuttons = []
    
    for i, (task_id, task, date) in enumerate(data, start = 4):
        var = IntVar()
        cb = ctk.CTkCheckBox(window, text=f"{task}; fällig bis: {date}", font=('Arial', 14), variable=var)
        cb.grid(column=1, row=i, padx=2, pady=2, columnspan=3)
        checkbuttons.append((cb, var, task_id))

def delete_task():
    for cb, var, task_id in checkbuttons:
        if var.get() == 1:
            cursor.execute(f"DELETE FROM todoliste WHERE task_id = {task_id}")
            
    read_database()

#Buttons und Label festlegen
title_label = ctk.CTkLabel(window, text="Meine To-Do-Liste",font=("Arial", 20))
blank = ctk.CTkLabel(window, text = ' ')
task_label= ctk.CTkLabel(window, text="Aufgabe:", font=("Arial", 16))
date_label= ctk.CTkLabel(window, text="Datum:", font=("Arial", 16))
input_task = ctk.CTkEntry(window, placeholder_text='Aufgabe', width=100, height=10, corner_radius=5, font = ('Arial', 16))
input_date= ctk.CTkEntry(window, placeholder_text='Datum', width=80, height=10, corner_radius=5, font = ('Arial', 16))
add_btn = ctk.CTkButton(window, text="Hinzufügen", command=add_task, font=("Arial", 14))
delete_btn = ctk.CTkButton(window, text="Entfernen", command=delete_task, font=("Arial", 14))

#alle Label und Buttons im Fenster anordnen
window.config() 
title_label.grid(column=1, row=0, padx=5, pady=5, columnspan=2)
blank.grid(column=0, row=1, pady=5, padx=5)
task_label.grid(column=1, row=1, pady=5, padx=5)
date_label.grid(column=2, row=1, pady=5, padx=5)
input_task.grid(column=1, row=2, padx=5, pady=5)
input_date.grid(column=2, row=2, pady=5, padx=5)
add_btn.grid(column=3, row=2, padx=5, pady=5)
delete_btn.grid(column=4, row=2, sticky=W, pady=5, padx=5)

#Fenster wird immer aktualisiert und Verbindung zur Datenbank wird "geschlossen"
window.after_idle(read_database)
window.mainloop()
connection.commit()
connection.close()