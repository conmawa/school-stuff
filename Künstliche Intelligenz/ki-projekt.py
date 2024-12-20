import pytesseract
import cv2
import customtkinter as ctk
from tkinter import filedialog as fd

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def load_image(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray

def preprocess_image(image):
    noise_removed = cv2.GaussianBlur(image, (5, 5), 0)
    _, threshold_image = cv2.threshold(noise_removed, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    return threshold_image

def extract_text(image):
    text = pytesseract.image_to_string(image, lang="deu")  
    return text

def main(image_path):
    text = extract_text(preprocess_image(load_image(image_path)))
    return text
    
def import_image():
    global extracted_text
    file_path = fd.askopenfilename()
    if file_path:
        extracted_text = main(file_path)
        text_widget.delete(1.0, "end")
        text_widget.insert("end", extracted_text)

def safe_text():
    text = text_widget.get("1.0",'end-1c')
    file_name = entry_filename.get()    
    with open(f'{file_name}.txt', mode = 'w') as text_file:
        text_file.write(text)

window = ctk.CTk()
window.title('Texterkennung aus Bildern')
window.geometry('700x500')
window.resizable(1,1)

text_widget = ctk.CTkTextbox(window, width=700, height=400, font=("Arial", 14))
title_label = ctk.CTkLabel(window, text="Texterkennung aus Bildern", font=("Arial", 20))
upload_button = ctk.CTkButton(window, text = 'Bild einlesen', command = import_image, font=("Arial", 20))
safe_button = ctk.CTkButton(window, text = 'Text speichern', command = safe_text, font=("Arial", 20))
entry_filename = ctk.CTkEntry(window, width=100, placeholder_text='Datei-Name')

window.config() 
title_label.grid(column=1, row=0, padx=5, pady=5, columnspan=4)
upload_button.grid(column = 1, row = 1, pady = 5, padx = 5)
safe_button.grid(column = 3, row = 1, pady = 5, padx = 5) 
text_widget.grid(column=1, row=2, pady=10, padx=5, columnspan = 4)
entry_filename.grid(column = 2, row = 1, pady = 5, padx = 5)

window.grid_rowconfigure(2, weight=1)
window.grid_columnconfigure(1, weight=1)

window.mainloop()