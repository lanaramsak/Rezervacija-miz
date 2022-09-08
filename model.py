import datetime
import json
from this import d

DOLZINA_REZERVACIJE = datetime.timedelta(hours = 2)

class Stanje:
    def __init__(self, restavracija, geslo, mize={}, lokacije=[]):
        self.uporabnik = restavracija
        self.geslo = geslo
        self.mize = mize
        self.lokacije = lokacije

    def dodaj_rezervacijo(self, rezervacija):
        datum = rezervacija.datum
        for miza in sorted(self.mize[rezervacija.lokacija]):
            if rezervacija.stevilo_oseb <= miza.stevilo_oseb:
                if miza.timeline == {}:
                    return True
                nov_seznam_ur = miza.timeline + [datum]
                nov_seznam_ur.sort()
                index = nov_seznam_ur.index(datum)
                if index == len(nov_seznam_ur) - 1:
                    razlika = datum - nov_seznam_ur[index - 1]
                elif index == 0:
                    razlika = nov_seznam_ur[index + 1] - datum
                else:
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
        self.mize[miza.lokacija] = self.mize.get(miza.lokacija) + [miza]

    def dodaj_lokacijo(self, lokacija):
        self.lokacije.append(lokacija)
        self.mize[lokacija] = []

    def zbirka_rezervacij(self):
        vse_rezervacije = []
        for lokacija in self.mize.keys():
            for miza in self.mize[lokacija]:
                vse_rezervacije += [(rezervacija, miza.stevilka) for rezervacija in miza.rezerviranost]
        return sorted(vse_rezervacije)

    def preverjanje_zasedenosti(self):
        while True:
            for miza in self.mize:
                if list(miza.timeline.keys().sort())[0] <= datetime.datetime.today():
                    miza.zasedi()
                if list(miza.timeline.values().sort())[0] <= datetime.datetime.today():
                    miza.prosta
                    #kaj če je vmes program zaprt pa poteče rezervacija, zato <=

    def v_slovar(self):
        mize_spomin = {lokacija: [miza.v_slovar() for miza in self.mize[lokacija]] for lokacija in self.mize.keys()}
        return {"restavracija" : self.restavracija, "geslo" : self.geslo, "mize" : mize_spomin, "lokacije" : self.lokacije}

    def shrani_v_datoteko(self, ime_datoteke):
        with open(ime_datoteke, "w") as dat:
            slovar = self.v_slovar()
            json.dump(slovar, dat, indent=4, ensure_ascii= False)

    @staticmethod
    def iz_slovarja_stanje(slovar):
        slovar_miz = {}
        for lokacija in slovar["mize"].keys():
            slovar_miz[lokacija] = []
            for miza in slovar["mize"][lokacija]:
                slovar_miz[lokacija].append(Miza.iz_slovarja_miza(miza))
        return Stanje(slovar["restavracija"], slovar["geslo"], slovar_miz, slovar["lokacije"])

    @staticmethod
    def preberi_iz_datoteke(ime_datoteke):
        with open(ime_datoteke) as dat:
            slovar = json.load(dat)
            return Stanje.iz_slovarja_stanje(slovar)

class Miza:
    stevilo = 0
    def __init__(self, stevilo_oseb, lokacija, timeline=[], rezerviranost=[], zasedenost=False, stevilka=0):
        self.stevilo_oseb = stevilo_oseb
        self.lokacija = lokacija
        self.timeline = timeline
        self.zasedenost = zasedenost
        self.rezerviranost = rezerviranost
        self.stevilka = stevilka

    def __lt___(self, miza2):
        return self.stevilo_oseb < miza2.stevilo_oseb

    def rezerviraj(self, rezervacija):
        self.timeline.append(rezervacija.datum)
        self.rezerviranost.append(rezervacija)

    def preveri_zasedenost(self):
        return self.zasedenost

    def naredi_zasedeno_brez_rezervacije(self):
        self.timeline.append(datetime.datetime.today())
        self.timeline.sort()

    def zasedi(self):
        self.zasedenost = True

    def prosta(self):
        self.zasedenost = False
        ##!!!!!!!!!!!self.timeline.pop(list(self.timeline.keys())[0])

    def naslednja_rezervacija(self):
        if self.timeline == []:
            return "Ni prihajajočih rezervacij"
        else:
            return f"Naslednja rezervacija je ob {self.timeline[0].__str__()}"

    def v_slovar(self):
        rezerviranost_spomin = [rezervacija.v_slovar() for rezervacija in self.rezerviranost]
        return {"stevilo_oseb" : self.stevilo_oseb, "lokacija" : self.lokacija, "timeline" : [str(time) for time in self.timeline], "rezerviranost" : rezerviranost_spomin, "zasedenost" : self.zasedenost}

    @staticmethod
    def iz_slovarja_miza(slovar):
        return Miza(slovar["stevilo_oseb"], slovar["lokacija"], [datetime.datetime.strptime(datum, "%Y-%m-%d %H:%M:%S") for datum in slovar["timeline"]], [Rezervacija.iz_slovarja_rezervacija(rezervacija) for rezervacija in slovar["rezerviranost"]], slovar["zasedenost"])


class Rezervacija:
    def __init__(self, ime, stevilo_oseb, datum, lokacija, opravljenost=False):
        self.ime = ime
        self.stevilo_oseb = stevilo_oseb
        self.datum = datum
        self.lokacija = lokacija
        self.opravljenost = opravljenost

    def __lt__(self, other):
        return self.datum < other.datum
        
    def prispela_rezervacija(self):
        self.opravljenost = True

    def v_slovar(self):
        return {"ime" : self.ime, "stevilo_oseb" : self.stevilo_oseb, "datum" : str(self.datum), "lokacija" : self.lokacija, "opravljenost" : self.opravljenost}
    
    @staticmethod
    def iz_slovarja_rezervacija(slovar):
        return Rezervacija(slovar["ime"], slovar["stevilo_oseb"], datetime.datetime.strptime(slovar["datum"], "%Y-%m-%d %H:%M:%S"), slovar["lokacija"], slovar["opravljenost"]) 