""" 

Anweisungen zum Ausführen

1. Terminal öffnen
2. Eingabe: 'pip install customtkinter'
3. Eingabe: 'pip install opencv-python'
4. Folgende Seite besuchen: https://github.com/UB-Mannheim/tesseract/wiki
5. neuesten Installer herunterladen --> speichern --> ausführen --> 'Ja' klicken --> Deutsch auswählen --> immer 'Weiter' auswählen bis installiert ist (Admin-Rechts benötigt)
6. Windows-Explorer öffnen --> 'C:' --> 'Programme' --> 'Tesseract-OCR' --> 'tessdata'
7. Folgende Seite besuchen: https://github.com/tesseract-ocr/tessdata/blob/main/deu.traineddata 
8. Datei von 7. herunterladen und in den Pfad bei 6. kopieren (Admin-Rechte benötigt)

"""


# benötigte Bibliotheken importieren
import pytesseract
import cv2
import customtkinter as ctk
from tkinter import filedialog as fd
from PIL import Image, ImageTk

# Pfad für Tesseract-Bibliothek angeben
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def main(image_path, language):
    image = cv2.imread(image_path) # Bild wird geladen mithilfe des Pfades des Bildes
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # Bild in Graustufen ändern
    noise_removed = cv2.GaussianBlur(gray, (5, 5), 0) # Rauschreduzierung des Bildes
    _, threshold_image = cv2.threshold(noise_removed, 120, 255, cv2.THRESH_TOZERO) # Pixelwert wird überprüft, wenn größer 255, wird er auf 0 gesetzt; gibt zwei Werte zurück, nur der zweite ist wichtig
    text = pytesseract.image_to_string(threshold_image, lang=language) # Bild wird in Text umgewandelt; Anpassung der Sprache hier möglich
    return text
    
def import_image():
    global extracted_text
    file_path = fd.askopenfilename() # Bild-Pfad wird gespeichert, indem ein Dialogfeld geöffnet wird und das Bild ausgewählt wird
    if file_path:
        img = Image.open(file_path) # Bild mit PIL öffnen
        img.thumbnail((400,400)) # Größe der Vorschau festlegen
        img_tk = ImageTk.PhotoImage(img) # Bild für die Benutzeroberfläche konvertieren
        
        image_preview_label.configure(image = img_tk, text = '') # Text entfernen und Bild laden
        image_preview_label.image = img_tk # Referenz auf Bild speichern
        
        language = pick_language.get().lower()[:3] # Value von der Sprach-Auswahl abrufen, dann alles klein machen und nur die ersten drei Zeichen nehmen
        extracted_text = main(file_path, language) # extrahierter Text mit entsprechender Sprache aus dem Bild wird gespeichert 
        text_widget.delete(1.0, "end") # Textfeld wird geleert
        text_widget.insert("end", extracted_text) # Text wird in Textfeld angezeigt --> Bearbeitung des Textes danach möglich
    else:
        text_widget.delete(1.0, "end") # Textfeld wird geleert
        text_widget.insert("end", 'Fehler beim Hochladen des Bildes') # Fehlermeldung

def safe_text():
    text = text_widget.get("1.0",'end-1c') # Text wird aus dem Textfeld gespeichert
    f = fd.asksaveasfile(initialfile='text.txt', defaultextension='.txt', filetypes=[('ALL FILES', '*.*'), ('Text Documents', '*.txt')]) # Dialogfeld, um Datei-Pfad / -Name zu bestimmen
    if f:
        f.write(text) # Text wird in Datei eingefügt
        f.close()
    else:
        return 

def set_ui_appearance():
    theme = ctk.get_appearance_mode() # Erscheinungsmode speichern
    if theme == 'Dark': # falls dark-mode
        ctk.set_appearance_mode('light') # ändere zu light-mode
    elif theme == 'Light': # falls light-mode
        ctk.set_appearance_mode('dark') # ändere zu dark-mode


window = ctk.CTk() # Konfiguration für die Benutzeroberfläche (UI)
window.title('Texterkennung aus Bildern') # Titel festlegen
window.geometry('1100x900') # Größe der Benutzeroberfläche festlegen
window.resizable(1,1) # UI kann in x und y Richtung vergrößert/ verkleinert werden

text_widget = ctk.CTkTextbox(window, width = 700, height = 400, font = ("Arial", 14)) # Textfeld kreieren, mit Größe und Schriftart
title_label = ctk.CTkLabel(window, text = "Texterkennung aus Bildern", font  = ("Arial", 20)) # Titel-Label kreieren
upload_button = ctk.CTkButton(window, text = 'Bild einlesen', command = lambda:import_image(), font = ("Arial", 20)) # Button, um das Bild auszulesen, Funktion import_image() wird beim Drücken ausgeführt
safe_button = ctk.CTkButton(window, text = 'Text speichern', command = lambda:safe_text(), font = ("Arial", 20)) # Button, um den Text zu speicher, Funktion safe_text() wird beim Drücken ausgeführt
pick_language = ctk.CTkComboBox(window, state = 'readonly', values = ['Deutsch', 'English']) # Auswahl, um die Sprache, in welcher der Text erkannt werden soll ändern
change_ui_appearance = ctk.CTkButton(window, text = 'Hell / Dunkel', command = lambda:set_ui_appearance(), font = ("Arial", 20)) # Button, um die Erscheinung der UI zu ändern
image_preview_label = ctk.CTkLabel(window, text="Keine Vorschau verfügbar") # Label, für die Bildvorschau


pick_language.set('Deutsch') # Standart-Value der Sprache festlegen


window.config()
# vorher definierte Widgets werden in Tabelle angeordnet
title_label.grid(column = 1, row = 0, padx = 5, pady = 5, columnspan = 2)
image_preview_label.grid(column=0, row=3, pady=10, padx=10, columnspan=2, sticky="nsew")
change_ui_appearance.grid(column = 3, row = 0, padx = 5, pady = 5, sticky = 'ew')
pick_language.grid(column = 1, row = 1, padx = 5, pady = 5, sticky = 'ew')
upload_button.grid(column = 2, row = 1, pady = 5, padx = 5, sticky = 'ew')
safe_button.grid(column = 3, row = 1, pady = 5, padx = 5, sticky = 'ew') 
text_widget.grid(column = 1, row = 2, pady = 10, padx = 5, columnspan =32, sticky = 'nsew')


window.grid_rowconfigure(2, weight = 1) # Text-Widget passt sich an die Höhe an
window.grid_columnconfigure(2, weight = 1) # Text-Widget passt sich an die Breite an
window.grid_columnconfigure(1, weight = 1) # Buttons sind gleichmäßig breit

window.mainloop() # UI wird geöffnet