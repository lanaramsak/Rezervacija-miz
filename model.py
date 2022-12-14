import datetime
import json
import matplotlib.pyplot as plt
import numpy as np

DOLZINA_REZERVACIJE = datetime.timedelta(hours = 2)
PRIDEJO = 1
BI_MORALI_BITI = 0


class Stanje:
    def __init__(self, restavracija, mize={}, lokacije=[]):
        self.restavracija = restavracija
        self.mize = mize
        self.lokacije = lokacije

    def dodaj_rezervacijo(self, rezervacija):
        datum = rezervacija.datum
        for miza in sorted(self.mize[rezervacija.lokacija]):
            if rezervacija.stevilo_oseb <= miza.stevilo_oseb:
                if miza.timeline == {}:
                    miza.rezerviraj(rezervacija)
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
        stotice = self.lokacije.index(miza.lokacija)
        stevilo = len(self.mize[miza.lokacija]) + 1
        miza.stevilka = stotice * 100 + stevilo
        self.mize[miza.lokacija] = self.mize.get(miza.lokacija) + [miza]

    def dodaj_lokacijo(self, lokacija):
        if lokacija not in self.lokacije:
            self.lokacije.append(lokacija)
            self.mize[lokacija] = []
            return False
        else:
            return True

    def vse_rezervacije(self):
        vse_rezervacije = []
        for lokacija in self.mize.keys():
            for miza in self.mize[lokacija]:
                vse_rezervacije += [(rezervacija, miza.stevilka) for rezervacija in miza.rezerviranost]
        return sorted(vse_rezervacije)

    def zbirka_rezervacij(self):
        vse_rezervacije = []
        for lokacija in self.mize.keys():
            for miza in self.mize[lokacija]:
                for rezervacija in miza.rezerviranost:
                    if rezervacija.datum > datetime.datetime.today():
                        vse_rezervacije.append((rezervacija, miza.stevilka, 0))
                    elif rezervacija.opravljenost == False:
                        vse_rezervacije.append((rezervacija, miza.stevilka, 1))
        return sorted(vse_rezervacije)
    
    
    def najdi_mizo(self, miza_st):
        lokacija = self.lokacije[miza_st // 100]
        miza = self.mize[lokacija][miza_st - (miza_st // 100) * 100 - 1]
        return miza

    def narisi_graf(self, leto):
        meseci = ["januar", "februar", "marec", "april", "maj", "junij", "julij", "avgust", "september", "oktober", "november", "december"]
        gledane_rezervacije = []
        for rezervacija in self.vse_rezervacije():
            if rezervacija[0].opravljenost == True and rezervacija[0].datum.year == leto:
                gledane_rezervacije.append(rezervacija[0])
        if gledane_rezervacije == []:
            return "Za izbrano leto ni rezervacij"
        gledane_rezervacije.sort()
        zacetni_mesec = gledane_rezervacije[0].datum.month
        koncni_mesec = gledane_rezervacije[-1].datum.month
        vrednosti_slovar = {}
        for rezervacija in gledane_rezervacije:
            for mesec in range(zacetni_mesec, koncni_mesec + 1):
                if rezervacija.datum.month == mesec:
                    vrednosti_slovar[mesec] = vrednosti_slovar.get(mesec, 0) + 1
                    break
        vrednosti_seznam = []
        for mesec in sorted(vrednosti_slovar.keys()):
            vrednosti_seznam.append(vrednosti_slovar[mesec])
        x = np.array(meseci[zacetni_mesec - 1 : koncni_mesec])
        y = np.array(vrednosti_seznam)
        plt.bar(x,y)
        plt.savefig(f"pregled_rezervacij{leto}.png")
        return None

    def v_slovar(self):
        mize_spomin = {lokacija: [miza.v_slovar() for miza in self.mize[lokacija]] for lokacija in self.mize.keys()}
        return {"restavracija" : self.restavracija, "mize" : mize_spomin, "lokacije" : self.lokacije}

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
        return Stanje(slovar["restavracija"], slovar_miz, slovar["lokacije"])

    @staticmethod
    def preberi_iz_datoteke(ime_datoteke):
        with open(ime_datoteke) as dat:
            slovar = json.load(dat)
            return Stanje.iz_slovarja_stanje(slovar)

class Miza:
    stevilo = 0
    def __init__(self, stevilo_oseb, lokacija, timeline={}, rezerviranost=[], zasedenost=False, stevilka=0):
        self.stevilo_oseb = stevilo_oseb
        self.lokacija = lokacija
        self.timeline = timeline
        self.zasedenost = zasedenost
        self.rezerviranost = rezerviranost
        self.stevilka = stevilka

    def __eq__(self, miza2):
        return self.stevilo_oseb == miza2.stevilo_oseb

    def __lt__(self, miza2):
        return self.stevilo_oseb < miza2.stevilo_oseb

    def rezerviraj(self, rezervacija):
        self.timeline[rezervacija.datum] = rezervacija.datum + DOLZINA_REZERVACIJE
        self.rezerviranost.append(rezervacija)

    def preveri_zasedenost(self):
        sedaj = datetime.datetime.today().replace(microsecond=0)
        timeline = sorted(self.timeline)
        if timeline == []:
            return "Prosto"
        if timeline[0] <= sedaj and self.timeline[timeline[0]] >= sedaj:
            if self.zasedenost:
                stanje = "Zasedeno"
            else:
                stanje = "Rezervacija ??e prihaja"
        else:
            stanje = "Prosto"
        return stanje

    def naslednja_rezervacija(self):
        if self.rezerviranost == []:
            return None
        dva = sorted(self.rezerviranost)[0].datum.date()
        ena = datetime.datetime.now().date()
        if dva == ena:
            return sorted(self.rezerviranost)[0].datum.time()
        else:
            return None
    
    def odstrani_rezervacijo(self, rezervacija):
        self.rezerviranost.remove(rezervacija)
        self.timeline.pop(rezervacija.datum)

    def naredi_zasedeno_brez_rezervacije(self):
        zdaj = datetime.datetime.today().replace(microsecond=0)
        if self.timeline == {}:
            konec = zdaj + DOLZINA_REZERVACIJE
        elif list(self.timeline.keys())[0] < (zdaj + DOLZINA_REZERVACIJE):
            konec = list(self.timeline.keys())[0]
        else:
            konec = zdaj + DOLZINA_REZERVACIJE
        self.timeline[zdaj] = konec
        self.zasedenost = True

    def naredi_zasedeno(self,rezervacija):
        self.timeline.pop(rezervacija.datum)
        self.naredi_zasedeno_brez_rezervacije()
        rezervacija.opravljenost = True
        rezervacija.datum = datetime.datetime.today().replace(microsecond=0)

    def prosta(self):
        self.zasedenost = False
        self.timeline.pop(sorted(self.timeline)[0])

    def najdi_rezervacijo(self):
        datum = sorted(self.timeline.keys())[0]
        for rezervacija in self.rezerviranost:
            if rezervacija.opravljenost == False and rezervacija.datum == datum:
                return rezervacija
        return None

    def v_slovar(self):
        rezerviranost_spomin = [rezervacija.v_slovar() for rezervacija in self.rezerviranost]
        return {"stevilo_oseb" : self.stevilo_oseb, "lokacija" : self.lokacija,
         "timeline" : {str(time) : str(self.timeline[time]) for time in self.timeline}, 
         "rezerviranost" : rezerviranost_spomin, "zasedenost" : self.zasedenost, "stevilka_mize" : self.stevilka}

    @staticmethod
    def iz_slovarja_miza(slovar):
        return Miza(slovar["stevilo_oseb"], slovar["lokacija"], {datetime.datetime.strptime(datum, "%Y-%m-%d %H:%M:%S") : datetime.datetime.strptime(slovar["timeline"][datum], "%Y-%m-%d %H:%M:%S") for datum in slovar["timeline"]}, [Rezervacija.iz_slovarja_rezervacija(rezervacija) for rezervacija in slovar["rezerviranost"]], slovar["zasedenost"], slovar["stevilka_mize"])


class Rezervacija:
    def __init__(self, ime, stevilo_oseb, datum, lokacija, opravljenost=False):
        self.ime = ime
        self.stevilo_oseb = stevilo_oseb
        self.datum = datum
        self.lokacija = lokacija
        self.opravljenost = opravljenost

    def __lt__(self, other):
        if self.opravljenost == other.opravljenost:
            return self.datum < other.datum
        elif self.opravljenost == False:
            return True
        else:
            return False

    def v_slovar(self):
        return {"ime" : self.ime, "stevilo_oseb" : self.stevilo_oseb, "datum" : str(self.datum), "lokacija" : self.lokacija, "opravljenost" : self.opravljenost}
    
    @staticmethod
    def iz_slovarja_rezervacija(slovar):
        return Rezervacija(slovar["ime"], slovar["stevilo_oseb"], datetime.datetime.strptime(slovar["datum"], "%Y-%m-%d %H:%M:%S"), slovar["lokacija"], slovar["opravljenost"]) 
