from sys import maxsize
import bottle
import json
import datetime
from model import Stanje, Miza, Rezervacija

SIFRIRNI_KLJUC = "Očitno morm tle neki napisat"

def ime_uporabnikove_datoteke(ime_restavracije):
    return f"stanja_restavracij/{ime_restavracije}.json"

def poglej_za_osebe():
    with open("uporabniki.json") as dat:
        uporabniki = json.load(dat)
    return uporabniki

def shrani_med_osebe(uporabniki):
    with open("uporabniki.json", "w") as dat:
        json.dump(uporabniki, dat, indent=4, ensure_ascii= False)

def stanje_restavracije():
    ime_restavracije = bottle.request.get_cookie("ime_restavracije", secret=SIFRIRNI_KLJUC)
    if ime_restavracije == None:
        return bottle.redirect("/")
    # else:
    #     uporabnisko_ime = uporabnisko_ime
    ime_datoteke = ime_uporabnikove_datoteke(ime_restavracije)
    try:
        stanje = Stanje.preberi_iz_datoteke(ime_datoteke)
    except FileNotFoundError:
        stanje = Stanje.preberi_iz_datoteke("stanja_restavracij/zacetno_stanje.json")
        stanje.restavracija = ime_restavracije
        stanje.shrani_v_datoteko(ime_datoteke)
    return stanje

def shrani_stanje_trenutnega_uporabnika(stanje):
    ime_restavracije = bottle.request.get_cookie("ime_restavracije", secret=SIFRIRNI_KLJUC)
    ime_datoteke = ime_uporabnikove_datoteke(ime_restavracije)
    stanje.shrani_v_datoteko(ime_datoteke)

@bottle.post("/prijava/")
def prijava_post():
    uporabniki = poglej_za_osebe()
    ime_restavracije = bottle.request.forms.getunicode("ime_restavracije")
    geslo = bottle.request.forms.getunicode("geslo")
    if ime_restavracije in list(uporabniki.keys()):
        if uporabniki[ime_restavracije] == geslo:
            bottle.response.set_cookie("ime_restavracije", ime_restavracije, path="/", secret=SIFRIRNI_KLJUC)
            bottle.redirect("/pregled_miz/")
        else:
            return bottle.template(
        "zacetna_stran.tpl",
        napaka = "Napačno geslo"
        )  

    else:
        return bottle.template(
        "zacetna_stran.tpl",
        napaka = "Račun s tem imenom ne obstaja, poskusite ponovno ali pa se registrirate"
        )  

@bottle.get("/registracija/")
def registracija():
    return bottle.template(
        "registracija.tpl",
        napaka = None
        )

@bottle.post("/registracija/")
def registracija_post():
    ime_restavracije = bottle.request.forms.getunicode("ime_restavracije")
    geslo = bottle.request.forms.getunicode("geslo")
    uporabniki = poglej_za_osebe()
    if ime_restavracije in list(uporabniki.keys()):
        return bottle.template(
        "registracija.tpl",
        napaka = "Račun s tem imenom že obstaja"
        )   
    else:
        bottle.response.set_cookie("ime_restavracije", ime_restavracije, path="/", secret=SIFRIRNI_KLJUC)
        uporabniki = poglej_za_osebe()
        uporabniki[ime_restavracije] = geslo
        shrani_med_osebe(uporabniki)

        return bottle.redirect("/pregled_miz/")

@bottle.post("/odjava/")
def odjava_post():
    bottle.response.delete_cookie("ime_restavracije")
    return bottle.redirect("/")

@bottle.get("/")
def zacetna_stran():
    stanje = stanje_restavracije()
    return bottle.template(
        "zacetna_stran.tpl",
        napaka = None

    )

@bottle.get("/pregled_rezervacij/")
def pregled_rezervacij():
    stanje = stanje_restavracije()
    return bottle.template(
        "pregled_rezervacij.tpl",     
        vse_rezervacije = stanje.zbirka_rezervacij(),
        ime_restavracije = stanje.restavracija,
        vse_lokacije = stanje.lokacije,
        )

@bottle.get("/pregled_preteklih_rezervacij/")
def pregled_rezervacij():
    stanje = stanje_restavracije()
    return bottle.template(
        "pregled_preteklih_rezervacij.tpl",     
        vse_rezervacije = stanje.vse_rezervacije(),
        ime_restavracije = stanje.restavracija,
        vse_lokacije = stanje.lokacije,
        napaka = None
        )

@bottle.post("/pregled_preteklih_rezervacij/")
def narisi_graf():
    stanje = stanje_restavracije()
    leto = int(bottle.request.forms.getunicode("leto"))
    print(leto)
    napaka = stanje.narisi_graf(leto)
    return bottle.template(    
        "pregled_preteklih_rezervacij.tpl",     
        vse_rezervacije = stanje.vse_rezervacije(),
        ime_restavracije = stanje.restavracija,
        vse_lokacije = stanje.lokacije,
        napaka = napaka
        )


@bottle.get("/pregled_miz/")
def pregled_rezervacij():
    stanje = stanje_restavracije()
    return bottle.template(
        "pregled_miz.tpl",
        katere_mize = stanje.lokacije,
        vse_mize = stanje.mize,
        ime_restavracije = stanje.restavracija,
        vse_lokacije = stanje.lokacije,
        lokacije_za_mize = stanje.lokacije,
        )

@bottle.get("/pregled_miz/<ime_lokacije>/")
def pregled_rezervacij(ime_lokacije):
    stanje = stanje_restavracije()
    return bottle.template(
        "pregled_miz.tpl",
        katere_mize = [ime_lokacije],
        vse_mize = stanje.mize,
        ime_restavracije = stanje.restavracija,
        vse_lokacije = stanje.lokacije,
        )

@bottle.get("/nova_miza/")
def dodaj_mizo():
    stanje = stanje_restavracije()
    return bottle.template(
        "dodaj_mizo.tpl", 
        vse_lokacije = stanje.lokacije,
        ime_lokacije = ""
    )

@bottle.get("/nova_miza/<ime_lokacije>/")
def dodaj_mizo(ime_lokacije):
    stanje = stanje_restavracije()
    return bottle.template(
        "dodaj_mizo.tpl", 
        vse_lokacije = [ime_lokacije]
    )

@bottle.post("/nova_miza/")
def naredi_mizo():
    stanje = stanje_restavracije()
    st_oseb = int(bottle.request.forms.getunicode("st_oseb"))
    lokacija = bottle.request.forms.getunicode("lokacija")
    if len(stanje.lokacije) == 1:
        lokacija = stanje.lokacije[0]
    miza = Miza(st_oseb, lokacija)
    stanje.dodaj_mizo(miza)
    shrani_stanje_trenutnega_uporabnika(stanje)
    return bottle.redirect("/pregled_miz/")

@bottle.post("/nova_miza/<ime_lokacije>/")
def naredi_mizo(ime_lokacije):
    stanje = stanje_restavracije()
    st_oseb = int(bottle.request.forms.getunicode("st_oseb"))
    lokacija = ime_lokacije
    print(lokacija)
    miza = Miza(st_oseb, lokacija)
    stanje.dodaj_mizo(miza)
    shrani_stanje_trenutnega_uporabnika(stanje)
    return bottle.redirect(f"/pregled_miz/{ime_lokacije}/")

@bottle.post("/naredi_prosto/<katera_miza:int>/")
def naredi_prosto(katera_miza):
    stanje = stanje_restavracije()
    miza = stanje.najdi_mizo(katera_miza)
    miza.prosta()
    shrani_stanje_trenutnega_uporabnika(stanje)
    return bottle.redirect("/pregled_miz/")

@bottle.post("/naredi_prispelo/<katera_miza:int>/")
def naredi_prispelo(katera_miza):
    stanje = stanje_restavracije()
    miza = stanje.najdi_mizo(katera_miza)
    rezervacija = miza.najdi_rezervacijo()
    miza.naredi_zasedeno(rezervacija)
    shrani_stanje_trenutnega_uporabnika(stanje)
    return bottle.redirect("/pregled_miz/")

@bottle.post("/prekliči_rezervacijo/<katera_miza:int>/")
def prekliči_rezervacijo(katera_miza):
    stanje = stanje_restavracije()
    miza = stanje.najdi_mizo(katera_miza)
    miza.odstrani_rezervacijo(miza.rezerviranost[0])
    shrani_stanje_trenutnega_uporabnika(stanje)
    return bottle.redirect("/pregled_miz/")

@bottle.post("/naredi_zasedeno/<katera_miza:int>/")
def naredi_zasedeno(katera_miza):
    stanje = stanje_restavracije()
    miza = stanje.najdi_mizo(katera_miza)
    miza.naredi_zasedeno_brez_rezervacije()
    shrani_stanje_trenutnega_uporabnika(stanje)
    return bottle.redirect("/pregled_miz/")

@bottle.post("/brisi_mizo/<katera_miza:int>/")
def brisi_mizo(katera_miza):
    print(katera_miza)
    stanje = stanje_restavracije()
    miza = stanje.najdi_mizo(katera_miza)
    print(miza.stevilka)
    stanje.mize[miza.lokacija].remove(miza)
    shrani_stanje_trenutnega_uporabnika(stanje)
    return bottle.redirect("/pregled_miz/")

@bottle.get("/nova_rezervacija/")
def dodaj_rezervacijo():
    stanje = stanje_restavracije()
    return bottle.template(
        "dodaj_rezervacijo.tpl", 
        vse_lokacije = stanje.lokacije,
        ime_restavracije = stanje.restavracija,
        uspesnost = True 
    )

@bottle.post("/nova_rezervacija/")
def naredi_rezervacijo():
    stanje = stanje_restavracije()
    ime = bottle.request.forms.getunicode("ime")
    st_oseb = int(bottle.request.forms.getunicode("st_oseb"))
    datum = datetime.datetime.strptime(bottle.request.forms.getunicode("ura"), "%Y-%m-%dT%H:%M")
    lokacija = bottle.request.forms.getunicode("lokacija")
    rezervacija = Rezervacija(ime, st_oseb, datum, lokacija)
    if stanje.dodaj_rezervacijo(rezervacija):
        shrani_stanje_trenutnega_uporabnika(stanje)
        ########lahko da bo tu narobe ######
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
    stanje = stanje_restavracije()
    lokacija = bottle.request.forms.getunicode("lokacija")
    neuspesnost = stanje.dodaj_lokacijo(lokacija)
    shrani_stanje_trenutnega_uporabnika(stanje)
    if neuspesnost:
        return bottle.template("ze_lokacija.tpl", 
        ime_restavracije = stanje.restavracija,
        vse_lokacije = stanje.lokacije)
    else:
        return bottle.redirect("/pregled_miz/")

@bottle.get("/izbrisi_lokacijo/<lokacija>/")
def opozorilo_izbris_lokacije(lokacija):
    stanje = stanje_restavracije()
    return bottle.template("opozorilo_mize.tpl",
            vse_lokacije = stanje.lokacije,
            ime_restavracije = stanje.restavracija
    )

@bottle.post("/izbrisi_lokacijo/<lokacija>/")
def izbrisi_lokacijo(lokacija):
    stanje = stanje_restavracije()
    stanje.lokacije.remove(lokacija)
    stanje.mize.pop(lokacija)
    shrani_stanje_trenutnega_uporabnika(stanje)
    return bottle.redirect("/pregled_miz/")
    
@bottle.post("/prispelo/<st_rezervacije:int>/")
def prispelo(st_rezervacije):
    stanje = stanje_restavracije()
    rezervacija = stanje.zbirka_rezervacij()[st_rezervacije][0]
    miza_st = stanje.zbirka_rezervacij()[st_rezervacije][1] - 1
    miza = stanje.najdi_mizo(miza_st)
    miza.naredi_zasedeno(rezervacija)
    shrani_stanje_trenutnega_uporabnika(stanje)
    return bottle.redirect("/pregled_rezervacij/")

@bottle.post("/preklici/<st_rezervacije:int>/")
def preklici(st_rezervacije):
    stanje = stanje_restavracije()
    rezervacija = stanje.zbirka_rezervacij()[st_rezervacije][0]
    miza_st = stanje.zbirka_rezervacij()[st_rezervacije][1] - 1 
    miza = stanje.najdi_mizo(miza_st)
    miza.odstrani_rezervacijo(rezervacija)
    shrani_stanje_trenutnega_uporabnika(stanje)
    return bottle.redirect("/pregled_rezervacij/")

bottle.run(debug=True, reloader=True)