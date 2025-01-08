""" 

Anweisungen zum Ausführen

1. Terminal öffnen
2. Eingabe: "pip install customtkinter"
3. Eingabe: "pip install opencv-python"
4. Folgende Seite besuchen: https://github.com/UB-Mannheim/tesseract/wiki
5. neuesten Installer herunterladen --> speichern --> ausführen --> "Ja" klicken --> Deutsch auswählen --> immer "Weiter" auswählen bis installiert ist (Admin-Rechts benötigt)
6. Windows-Explorer öffnen --> 'C:' --> 'Programme' --> 'Tesseract-OCR' --> 'tessdata'
7. Folgende Seite besuchen: https://github.com/tesseract-ocr/tessdata/blob/main/deu.traineddata 
8. Datei von 7. herunterladen und in den Pfad bei 6. kopieren (Admin-Rechte benötigt)

"""


# benötigte Bibliotheken importieren
import pytesseract
import cv2
import customtkinter as ctk
from tkinter import filedialog as fd

# Pfad für Bibliothek angeben
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Funktion: Bild hochladen
def load_image(image_path):
    image = cv2.imread(image_path) # Bild wird geladen mithilfe des Pfades des Bildes
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # Bild in Graustufen ändern
    return gray

def preprocess_image(image):
    noise_removed = cv2.GaussianBlur(image, (5, 5), 0) # Rauschreduzierung des Bildes
    _, threshold_image = cv2.threshold(noise_removed, 120, 255, cv2.THRESH_TOZERO) # Pixelwert wird überprüft, wenn größer 255, wird er auf 0 gesetzt; gibt zwei Werte zurück, nur der zweite ist wichtig
    return threshold_image

def extract_text(image):
    text = pytesseract.image_to_string(image, lang="deu") # Bild wird in Text umgewandelt; Anpassung der Sprache hier möglich
    return text

def main(image_path):
    text = extract_text(preprocess_image(load_image(image_path))) # Text ausgegeben; Funktionen werden nacheinander aufgerufen und geben jeweils Werte wieder
    return text
    
def import_image():
    global extracted_text
    file_path = fd.askopenfilename() # Bild-Pfad wird gespeichert, indem ein Dialogfeld geöffnet wird und das Bild ausgewählt wird
    if file_path:
        extracted_text = main(file_path) # extrahierter Text aus dem Bild wird gespeichert
        text_widget.delete(1.0, "end") # Textfeld wird geleert
        text_widget.insert("end", extracted_text) # Text wird in Textfeld angezeigt --> Bearbeitung des Textes danach möglich

def safe_text():
    text = text_widget.get("1.0",'end-1c') # Text wird aus dem Textfeld gespeichert
    f = fd.asksaveasfile(initialfile='text.txt', defaultextension='.txt', filetypes=[('ALL FILES', '*.*'), ('Text Documents', '*.txt')]) # Dialogfeld, um Datei-Pfad / -Name zu bestimmen
    if f:
        f.write(text) # Text wird in Datei eingefügt
        f.close()
    else:
        return 
    

window = ctk.CTk() # Konfiguration für die Benutzeroberfläche (UI)
window.title('Texterkennung aus Bildern') # Titel festlegen
window.geometry('700x500') # Größe der BenutzeroberflUIäche festlegen
window.resizable(1,1) # UI kann in x und y Richtung vergrößert/ verkleinert werden

text_widget = ctk.CTkTextbox(window, width = 700, height = 400, font = ("Arial", 14)) # Textfeld kreieren, mit Größe und Schriftart
title_label = ctk.CTkLabel(window, text = "Texterkennung aus Bildern", font  = ("Arial", 20)) # Titel-Label kreieren
upload_button = ctk.CTkButton(window, text = 'Bild einlesen', command = lambda:import_image(), font = ("Arial", 20)) # Button, um das Bild auszulesen, Funktion import_image() wird beim Drücken ausgeführt
safe_button = ctk.CTkButton(window, text = 'Text speichern', command = lambda:safe_text(), font = ("Arial", 20)) # Button, um den Text zu speicher, Funktion safe_text() wird beim Drücken ausgeführt

window.config()
# vorher definierte Widgets werden in Tabelle angeordnet
title_label.grid(column = 1, row = 0, padx = 5, pady = 5, columnspan = 2)
upload_button.grid(column = 1, row = 1, pady = 5, padx = 5, sticky = 'ew')
safe_button.grid(column = 2, row = 1, pady = 5, padx = 5, sticky = 'ew') 
text_widget.grid(column = 1, row = 2, pady = 10, padx = 5, columnspan = 2, sticky = 'nsew')

window.grid_rowconfigure(2, weight = 1) # Text-Widget passt sich an die Höhe an
window.grid_columnconfigure(2, weight = 1) # Text-Widget passt sich an die Breite an
window.grid_columnconfigure(1, weight = 1) # Buttons sind gleichmäßig breit

window.mainloop() # UI wird geöffnet