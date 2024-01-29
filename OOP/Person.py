### OOP am Beispiel der Klasse 'Person' ###

class Person:
    
    def __init__(self, vorname, nachname):
        self.vorname = vorname
        self.nachname = nachname
  
    def vorstellen(self):
        print(f"Ich heiße {self.vorname} {self.nachname}.")
        

person1 = Person("Tom", "Meier")
person1.vorstellen()
