## polymorphismus ##

# Basisklasse, dient als "Schnittstelle"
class Form:
    def zeichne(self):
        raise Exception("Diese Methode muss in der Unterklasse überschrieben werden.")
    
#Konkrete Klasse, die die Basisklasse erweitert
class Kreis(Form):
    def zeichne(self):
        print("Ein Kreis wird gezeichnet.")

#eine weitere konkrete Klasse
class Rechteck(Form):
    def zeichne(self):
        print("Ein Rechteck wird gezeichnet.")
        
# und noch eine konkrete Klasse
class Dreieck(Form):
    def zeichne(self):
        print("Ein Dreieck wird gezeichnet.")
        
# Eine Funktion, die das Polymorphismus-Konzept nutzt
def zeichne_form(form):
    form.zeichne()
    
# Objekte der verschiedenen Formen erstellen
kreis = Kreis()
rechteck = Rechteck()
dreieck = Dreieck()

# Die gleiche Funktion mit verschiedenen Objekttypen aufrufen
zeichne_form(kreis)
zeichne_form(rechteck)
zeichne_form(dreieck)