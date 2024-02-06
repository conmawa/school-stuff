## Aufgabe von ChatGPT ##

class Bankkonto:
    def __init__(self, kontostand, kontonummer):
        self.__kontostand = kontostand
        self.__kontonummer = kontonummer
    
    def get_kontonummer(self):
        print(f"Deine Kontonummer lautet: {self.__kontonummer}")
        
    def get_kontostand(self):
        print(f"Dein Kontostand liegt bei: {self.__kontostand}")
    
    def einzahlen(self, data):
        self.__kontostand += data
        print(f"Geld wurde eingezahlt. Dein Kontostand liegt jetzt bei: {self.__kontostand}")
    
    def ausgeben(self, data):
        if data <= self.__kontostand:
            self.__kontostand -= data
            print(f"Geld wurde ausgezahlt. Dein Kontostand liegt jetzt bei: {self.__kontostand}")
        else:
            print("Du hast nicht genügend Geld auf deinem Konto")

bank1 = Bankkonto(100, "DE 0021...")
bank1.get_kontonummer()
bank1.get_kontostand()
bank1.einzahlen(10)

bank1.ausgeben(111)
