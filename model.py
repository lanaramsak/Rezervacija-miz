import datetime
import json


DOLZINA_REZERVACIJE = datetime.timedelta(hours = 2)

class Stanje:
    def __init__(self, restavracija, geslo, mize={}, lokacije=[]):
        self.uporabnik = restavracija
        self.geslo = geslo
        self.mize = sorted(mize)
        self.lokacije = lokacije
        #izpis vseh rezervacij, kako?

    def dodaj_rezervacijo(self, rezervacija):
        datum = rezervacija.datum
        for miza in sorted(self.mize[rezervacija.lokacija]):
            if rezervacija.stevilo_oseb <= miza.stevilo_oseb:
                if miza.timeline == {}:
                    return True
                nov_seznam_ur = list(miza.timeline.keys()) + [datum]
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

    def preverjanje_zasedenosti(self):
        while True:
            for miza in self.mize:
                if list(miza.timeline.keys().sort())[0] <= datetime.datetime.today():
                    miza.zasedi()
                if list(miza.timeline.values().sort())[0] <= datetime.datetime.today():
                    miza.prosta
                    #kaj če je vmes program zaprt pa poteče rezervacija, zato <=

    def v_slovar(self):
        miza_spomin = [miza.v_slovar() for miza in self.mize]
        return {"restavracija" : self.restavracija, "geslo" : self.geslo, "mize" : miza_spomin, "lokacije" : self.lokacije}

    def shrani_v_datoteko(self, ime_datoteke):
        with open(ime_datoteke, "w") as dat:
            slovar = self.v_slovar()
            json.dump(slovar, dat, indent=4, ensure_ascii= False)

    @staticmethod
    def iz_slovarja_stanje(slovar):
        return Stanje(slovar["restavracija"], slovar["geslo"], [iz_slovarja_miza(miza) for miza in slovar["mize"]], slovar["lokacije"])

    @staticmethod
    def preberi_iz_datoteke(ime_datoteke):
        with open(ime_datoteke) as dat:
            slovar = json.load(dat)
            return Stanje.iz_slovarja(slovar)

class Miza:
    stevilo = 0
    def __init__(self, stevilo_oseb, lokacija, timeline={}, rezerviranost=[], zasedenost=False):
        self.stevilo_oseb = stevilo_oseb
        self.lokacija = lokacija
        self.timeline = timeline
        self.zasedenost = zasedenost
        self.rezerviranost = rezerviranost

    def __lt___(self, miza2):
        return self.stevilo_oseb < miza2.stevilo_oseb

    def rezerviraj(self, rezervacija):
        self.timeline[rezervacija.datum] = rezervacija.datum + DOLZINA_REZERVACIJE
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
        self.timeline.pop(list(self.timeline.keys())[0])

    def naslednja_rezervacija(self):
        if self.timeline == []:
            return "Ni prihajajočih rezervacij"
        else:
            return f"Naslednja rezervacija je ob {self.timeline[0].__str__()}"

    def v_slovar(self):
        rezerviranost_spomin = [rezervacija.v_slovar() for rezervacija in self.rezerviranost]
        return {"stevilo_oseb" : self.stevilo_oseb, "lokacija" : self.lokacija, "timeline" : self.timeline, "rezerviranost" : rezerviranost_spomin, "zasedenost" : self.zasedenost}

    @staticmethod
    def iz_slovarja_miza(slovar):
        return Miza(slovar["stevilo_oseb"], slovar["lokacija"], slovar["timeline"], [iz_slovarja_rezervacija(rezervacija) for rezervacija in slovar["rezerviranost"]], slovar["zasedenost"])


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
        return {"ime" : self.ime, "stevilo_oseb" : self.stevilo_oseb, "datum" : self.datum, "lokacija" : self.lokacija, "opravljenost" : self.opravljenost}
    
    @staticmethod
    def iz_slovarja_rezervacija(slovar):
        return Rezervacija(slovar["ime"], slovar["stevilo_oseb"], slovar["datum"], slovar["lokacija"], slovar["opravljenost"]) 