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

@bottle.get("/nova_rezervacija/")
def dodaj_rezervacijo():
    return bottle.template(
        "dodaj_rezervacijo.tpl", 
        vse_lokacije = stanje.lokacije,
        ime_restavracije = stanje.restavracija,
        uspesnost = True 
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


@bottle.post("/nova_rezervacija/")
def naredi_rezervacijo():
    ime = bottle.request.forms.getunicode("ime")
    st_oseb = int(bottle.request.forms.getunicode("st_oseb"))
    datum = datetime.datetime.strptime(bottle.request.forms.getunicode("ura"), "%Y-%m-%dT%H:%M")
    lokacija = bottle.request.forms.getunicode("lokacija")
    rezervacija = Rezervacija(ime, st_oseb, datum, lokacija)
    if stanje.dodaj_rezervacijo(rezervacija): 
        print("to sem")
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
    miza = stanje.najdi_mizo(rezervacija, miza_st)
    rezervacija.prispela_rezervacija()
    miza.zasedi()

    return bottle.redirect("/pregled_rezervacij/")

@bottle.post("/preklici/<st_rezervacije:int>/")
def preklici(st_rezervacije):
    rezervacija = stanje.zbirka_rezervacij()[st_rezervacije][0]
    miza_st = stanje.zbirka_rezervacij()[st_rezervacije][1]
    miza = stanje.najdi_mizo(rezervacija, miza_st)
    miza.odstrani_rezervacijo(rezervacija)
    return bottle.redirect("/pregled_rezervacij/")

bottle.run(debug=True, reloader=True)