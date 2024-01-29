from time import *
class Schule():
    def __init__(self, lehrer, schueler_a):
        self.lehrer = lehrer
        self.__schueler_a = schueler_a
    def unterricht(self):
        return "lernen..."
    def pause(self):
        return "Yeah " + "Pause"
    def klausur(self):
        return "bahh klasusur...."
    def get_schueler(self): # -> private Attribute anzeigen lassen
        return self.__schueler_a
    def set_schueler(self, wert):
        self.__schueler_a = wert

inf1 = Schule("richter", 10)
bio1 = Schule("grimm", 10)

inf1.set_schueler(int(inf1.get_schueler()+8))

print("facts:")
print(f"Tutor: {inf1.lehrer}, Anzahl Schüler: {inf1.get_schueler()}")
print(f"Tutor: {bio1.lehrer}, Anzahl Schüler: {bio1.get_schueler()}")
print("-------")
print(f"Info: {inf1.klausur()}")
print(f"Bio: {bio1.klausur()}")
sleep(2)
print("--")
print(f"Info: {inf1.pause()}")
print(f"Bio: {bio1.pause()}")