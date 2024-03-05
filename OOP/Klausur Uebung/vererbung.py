class Tier:
    def __init__(self, name):
        self.name = name
        
class Katze(Tier):
    def __init__(self, name, rasse, alter):
        self.rasse = rasse
        self.alter = alter
        super().__init__(name)
        
katze = Katze("balu", "kurzhaar", 10)
print(katze.name)