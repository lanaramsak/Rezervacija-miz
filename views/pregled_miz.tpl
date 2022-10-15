% rebase('osnova.tpl', ime_strani = "pregled_miz", menu = True)

<p class="control">
    %for st_lokacije,lokacija in enumerate(vse_lokacije):
        %if lokacija in katere_mize:
            <div class="box">
            %for st_miza, miza in enumerate(vse_mize[lokacija]):
                %stanje = miza.preveri_zasedenost()
                %if stanje == "Zasedeno":
                <form method="POST" action="/naredi_prosto/{{st_lokacije}}{{st_miza}}/">
                    <button class="button is-large">  
                    {{miza.stevilka}}
                    <br>
                    Zasedeno
                    </button>
                </form>
                %elif stanje == "Rezervacija še prihaja":
                <form method="POST" action="/naredi_prispelo/{{st_lokacije}}{{st_miza}}/">
                    <button class="button is-large">  
                    {{miza.stevilka}}
                    <br>
                    Rezervacija še prihaja
                    </button>
                </form>
                <form method="POST" action="/prekliči_rezervacijo/{{st_lokacije}}{{st_miza}}/">
                    <button>
                        Prekliči
                    </button>
                </form>
                %else:
                <form method="POST" action="/naredi_zasedeno/{{st_lokacije}}{{st_miza}}/">
                    <button class="button is-large is-square">  
                    {{miza.stevilka}} 
                    <br>
                    Prosto
                    </button>
                </form>
                %end
            %end
        %end
            </div>
    %end
</p>

<a href="/nova_miza/" class="button">DODAJ NOVO MIZO</a>

