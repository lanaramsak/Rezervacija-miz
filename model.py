import datetime
import sched, time


DOLZINA_REZERVACIJE = datetime.timedelta(hours = 2)

class Stanje:
    def __init__(self, mize={}, rezervacije=[], lokacije=[]):
        self.mize = sorted(mize)
        self.rezervacije = sorted(rezervacije)
        self.lokacije = lokacije

    def dodaj_rezervacijo(self, rezervacija):
        datum = rezervacija.datum
        for miza in sorted(self.mize[rezervacija.lokacija]):
            if rezervacija.stevilo_oseb <= miza.stevilo_oseb:
                nov_seznam_ur = miza.rezerviranost + [datum]
                nov_seznam_ur.sort()
                index = nov_seznam_ur.index(datum)
                razlika = min(datum - nov_seznam_ur[index - 1], nov_seznam_ur[index + 1] - datum)
                if razlika >= DOLZINA_REZERVACIJE:
                    miza.rezerviraj(rezervacija)
                    return True
        return False
    
    def dodaj_mizo(self, miza):
        desetice = self.lokacije[self.miza.lokacija]
        global stevilo
        stevilo += 1
        miza.stevilka = desetice * 10 + stevilo
        self.mize[miza.lokacija] = self.mize.get(miza.lokacija) + [(miza.stevilo_oseb, miza)]

    def dodaj_lokacijo(self, lokacija):
        self.lokacije.append(lokacija)
        self.mize[lokacija] = []


class Miza:
    stevilo = 0
    def __init__(self, stevilo_oseb, lokacija, prostor, rezerviranost=[], zasedenost=False):
        self.stevilo_oseb = stevilo_oseb
        self.lokacija = lokacija
        self.prostor = prostor
        self.rezerviranost = rezerviranost
        self.zasedenost = zasedenost
    
    def rezerviraj(self, rezervacija):
        self.rezerviranost.append(rezervacija.datum)
        self.rezerviranost.sort()

    def preveri_zasedenost(self):
        return self.zasedenost

    def naredi_zasedeno_brez_rezervacije(self):
        self.rezerviranost.append(datetime.datetime.today())
        self.rezerviranost.sort()

    def prosta_miza(self):
        self.zasedenost = False

    def naslednja_rezervacija(self):
        return f"Naslednja rezervacija je ob  {self.rezerviranost[0]}"

class Rezervacija:
    def __init__(self,ime, stevilo_oseb, datum_ura, prostor, opravljenost=False):
        self.ime = ime
        self.stevilo_oseb = stevilo_oseb
        self.datum = datum_ura
        self.prostor = prostor
        self.opravljenost = opravljenost
        
    def prispela_rezervacija(self):
        self.opravljenost = True