class Tier:
    def __init__(self, name, art, gewicht):
        self.__name = name
        self.__art = art
        self.__gewicht = gewicht
    
    def get_name(self):
        return self.__name
    
    def get_art(self):
        return self.__art
    
    def get_gewicht(self):
        return self.__gewicht
    
    def set_gewicht(self, gewicht):
        if gewicht > 0:
            self.__gewicht = gewicht
    
    def berechne_futtermenge():
        pass