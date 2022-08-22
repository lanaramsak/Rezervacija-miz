import bottle
from model import Stanje

IME_DATOTEKE = "stanje.json"
try: 
    stanje = Stanje.preberi_iz_datoteke(IME_DATOTEKE)
except FileNotFoundError:
    stanje = Stanje()
#potrebno narediti drugače ker imam uporabnike

@bottle.get("/")
def zacetna_stran():
    return bottle.template("zacetna_stran.html")

bottle.run(debug=True, reloader=True)