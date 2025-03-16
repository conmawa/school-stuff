class Kunden:
    def __init__(self, name, kunden_id):
        self.name = name
        self.kunden_id = kunden_id
        self.gemietete_fahrraeder = []
        self.gekaufte_fahrraeder = []
        
        
    def kaufe_fahrrad(self, fahrrad):
        self.gekaufte_fahrraeder.append(fahrrad)
        
    def miete_fahrrad(self, fahrrad):
        self.gemietete_fahrraeder.append(fahrrad)
    
    def rueckgabe_fahrrad(self, fahrrad, tage_zu_spaet = None):
        self.gemietete_fahrraeder.remove(fahrrad)
        if tage_zu_spaet:
            return tage_zu_spaet * 10
        else:
            return 0
        