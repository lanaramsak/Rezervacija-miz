import datetime
import sched, time


DOLZINA_REZERVACIJE = datetime.timedelta(hours = 2)

class Stanje:
    def __init__(self, mize={}, rezervacije=[], lokacije=[]):
        self.mize = sorted(mize)
        self.rezervacije = sorted(rezervacije)
        self.lokacije = lokacije

    def izracun_prostih_stolov(self):
        return sum([miza.stevilo_oseb for miza in self.mize if miza.zasedenost == False])

    def izracun_vseh_stolov(self):
        return sum([miza.stevilo_oseb for miza in self.mize])

    def dodaj_rezervacijo(self, rezervacija):
        datum = rezervacija.datum

        if self.izracun_prostih_stolov + rezervacija.stevilo_oseb > self.izracun_vseh_stolov:
            return False
        
        self.rezervacije.append((rezervacija.datum, rezervacija.ura, rezervacija))

    def obstaja_prazna_miza(self, datum, lokacija):
        for miza in self.mize[lokacija]:
            pass
    
    def dodaj_mizo(self, miza):
        desetice = self.lokacije[self.miza.lokacija]
        global stevilo
        stevilo += 1
        miza.stevilka = desetice * 10 + stevilo
        self.mize[miza.lokacija] = self.mize.get(miza.lokacija).append(miza)
        #pazi zgoraj bo treba nekaj spremeniti

    def dodaj_lokacijo(self, lokacija):
        self.lokacije.append(lokacija)
        self.mize[lokacija] = []

    def uredi_rezervacije(self):
        for termin in self.rezervacije:
            mize_za_tok_oseb = [miza for miza in self.mize if miza.stevilo_oseb == termin[2].stevilo_oseb and not miza.preveri_zzasedenost]
            pass
            
            


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

    def zasedena_miza(self):
        self.zasedenost = True
    
    def prosta_miza(self):
        self.zasedenost = False

    def naslednja_rezervacija(self):
        return f"Naslednja rezervacija je ob  {self.rezervacija.ura}"

class Rezervacija:
    def __init__(self,ime, stevilo_oseb, datum_ura, prostor, opravljenost=False):
        self.ime = ime
        self.stevilo_oseb = stevilo_oseb
        self.datum = datum_ura
        self.prostor = prostor
        self.opravljenost = opravljenost
        
    def prispela_rezervacija(self):
        self.opravljenost = True