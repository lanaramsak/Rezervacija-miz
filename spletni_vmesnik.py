from re import M
from tkinter import Y
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
        vse_rezervacije = stanje.zbirka_rezervacij()
    )

@bottle.get("/nova_rezervacija/")
def dodaj_rezervacijo():
    return bottle.template(
        "dodaj_rezervacijo.tpl", 
        vse_lokacije = stanje.lokacije,
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
         return bottle.redirect("/")
    else:
            return bottle.template(
        "dodaj_rezervacijo.tpl",
        vse_lokacije = stanje.lokacije, 
        uspesnost = False
    )


@bottle.post("/opravi/<st_rezervacije: str>/")
def opravi(st_rezervacije):
    rezervacija = stanje.zbirka_rezervacij()[st_rezervacije]

    return bottle.template(
        "dodaj_rezervacijo.tpl"
    )

bottle.run(debug=True, reloader=True)