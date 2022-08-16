from datetime import datetime, time

class Stanje:
    def __init__(self, mize=[], rezervacije=[]):
        self.mize = mize
        self.rezervacije = rezervacije

    def dodaj_rezervacijo(self, rezervacija):
        self.rezervacije.append(rezervacija)
    
    def dodaj_mizo(self, miza):
        self.miez.append(miza)

class Miza:
    def __init__(self, stevilo_oseb, lokacija, prostor, rezervacija=None, zasedenost=False):
        self.stevilo_oseb = stevilo_oseb
        self.lokacija = lokacija
        self.prostor = prostor
        self.rezervacija = rezervacija
        self.zasedenost = zasedenost
    
    def stevilka_mize(self):
        pass
    
    def preveri_zasedenost(self):
        return self.zasedenost
    
    def naslednja_rezervacija(self):
        return f"Naslednja rezervacija je ob  {self.rezervacija.ura}"

class Rezervacija:
    def __init__(self,ime, stevilo_oseb, ura, datum, prostor, opravljenost=False):
        self.ime = ime
        self.stevilo_oseb = stevilo_oseb
        self.ura = ura
        self.datum = datum
        self.prostor = prostor
        self.opravljenost = opravljenost
        
    def prispela_rezervacija(self):
        self.opravljenost = True