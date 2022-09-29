from sys import maxsize
import bottle
import datetime
from model import Stanje, Miza, Rezervacija

def naredi_datoteko_restavraciji(ime_restavracije):
    return f"stanja_restavracij/{ime_restavracije}.json"

stanje = Stanje.preberi_iz_datoteke("primer_stanja.json")


@bottle.get("/")
def zacetna_stran():
    return bottle.template(
        "zacetna_stran.tpl",
        ime_restavracije = stanje.restavracija,
        vse_lokacije = stanje.lokacije,
    )

@bottle.get("/pregled_rezervacij/")
def pregled_rezervacij():
    return bottle.template(
        "pregled_rezervacij.tpl",     
        vse_rezervacije = stanje.zbirka_rezervacij(),
        ime_restavracije = stanje.restavracija,
        vse_lokacije = stanje.lokacije,
        )

@bottle.get("/pregled_preteklih_rezervacij/")
def pregled_rezervacij():
    return bottle.template(
        "pregled_preteklih_rezervacij.tpl",     
        vse_rezervacije = stanje.vse_rezervacije(),
        ime_restavracije = stanje.restavracija,
        vse_lokacije = stanje.lokacije,
        )

@bottle.get("/pregled_miz/")
def pregled_rezervacij():
    return bottle.template(
        "pregled_miz.tpl",
        katere_mize = stanje.lokacije,
        vse_mize = stanje.mize,
        ime_restavracije = stanje.restavracija,
        vse_lokacije = stanje.lokacije,
        lokacije_za_mize = stanje.lokacije,
        ime_lokacije = ""
        )

@bottle.get("/pregled_miz/<ime_lokacije>/")
def pregled_rezervacij(ime_lokacije):
    return bottle.template(
        "pregled_miz.tpl",
        katere_mize = [ime_lokacije],
        vse_mize = stanje.mize,
        ime_restavracije = stanje.restavracija,
        vse_lokacije = stanje.lokacije,
        lokacije_za_mize  = [ime_lokacije],
        ime_lokacije = ime_lokacije
        )

@bottle.get("/nova_miza/")
def dodaj_mizo():
    return bottle.template(
        "dodaj_mizo.tpl", 
        vse_lokacije = stanje.lokacije,
        ime_lokacije = ""
    )

@bottle.get("/nova_miza/<ime_lokacije>")
def dodaj_mizo(ime_lokacije):
    return bottle.template(
        "dodaj_mizo.tpl", 
        vse_lokacije = [ime_lokacije],
        ime_lokacije = ime_lokacije
    )

@bottle.post("/nova_miza/")
def naredi_mizo():
    st_oseb = int(bottle.request.forms.getunicode("st_oseb"))
    lokacija = bottle.request.forms.getunicode("lokacija")
    miza = Miza(st_oseb, lokacija)
    stanje.dodaj_mizo(miza)
    return bottle.redirect("/pregled_miz/")

@bottle.post("/nova_miza/<ime_lokacije>")
def naredi_mizo(ime_lokacije):
    st_oseb = int(bottle.request.forms.getunicode("st_oseb"))
    lokacija = ime_lokacije
    miza = Miza(st_oseb, lokacija)
    stanje.dodaj_mizo(miza)
    return bottle.redirect("/pregled_miz/<ime_lokacije>/")

@bottle.get("/nova_rezervacija/")
def dodaj_rezervacijo():
    return bottle.template(
        "dodaj_rezervacijo.tpl", 
        vse_lokacije = stanje.lokacije,
        ime_restavracije = stanje.restavracija,
        uspesnost = True 
    )

@bottle.post("/nova_rezervacija/")
def naredi_rezervacijo():
    ime = bottle.request.forms.getunicode("ime")
    st_oseb = int(bottle.request.forms.getunicode("st_oseb"))
    datum = datetime.datetime.strptime(bottle.request.forms.getunicode("ura"), "%Y-%m-%dT%H:%M")
    lokacija = bottle.request.forms.getunicode("lokacija")
    rezervacija = Rezervacija(ime, st_oseb, datum, lokacija)
    if stanje.dodaj_rezervacijo(rezervacija): 
        return bottle.redirect("/pregled_rezervacij/")
    else:
            return bottle.template(
        "dodaj_rezervacijo.tpl",
        vse_lokacije = stanje.lokacije,
        ime_restavracije = stanje.restavracija,
        uspesnost = False
    )

@bottle.post("/dodaj_lokacijo/")
def dodaj_lokacijo():
    lokacija = bottle.request.forms.getunicode("lokacija")
    neuspesnost = stanje.dodaj_lokacijo(lokacija)
    if neuspesnost:
        return bottle.template("ze_lokacija.tpl", 
        ime_restavracije = stanje.restavracija,
        vse_lokacije = stanje.lokacije)
    else:
        return bottle.redirect("/")
    
@bottle.post("/prispelo/<st_rezervacije:int>/")
def prispelo(st_rezervacije):
    rezervacija = stanje.zbirka_rezervacij()[st_rezervacije][0]
    miza_st = stanje.zbirka_rezervacij()[st_rezervacije][1]
    miza = stanje.najdi_mizo(miza_st)
    rezervacija.prispela_rezervacija()
    miza.zasedi()

    return bottle.redirect("/pregled_rezervacij/")

@bottle.post("/preklici/<st_rezervacije:int>/")
def preklici(st_rezervacije):
    rezervacija = stanje.zbirka_rezervacij()[st_rezervacije][0]
    miza_st = stanje.zbirka_rezervacij()[st_rezervacije][1]
    miza = stanje.najdi_mizo(miza_st)
    miza.odstrani_rezervacijo(rezervacija)
    return bottle.redirect("/pregled_rezervacij/")

bottle.run(debug=True, reloader=True)