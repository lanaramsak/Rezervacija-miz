% rebase('osnova.tpl', ime_strani = "pregled_miz", menu = True)

<div>
    %for st_lokacije,lokacija in enumerate(vse_lokacije):
        %if lokacija in katere_mize:
            <div class="box">
            %for st_miza, miza in enumerate(vse_mize[lokacija]):
                %stanje = miza.preveri_zasedenost()
                %if stanje == "Zasedeno":
                <form method="POST" action="/naredi_prosto/{{st_lokacije}}{{st_miza}}/">
                    <button class="button is-large is-danger">  
                    {{miza.stevilka}}
                    <br>
                    Zasedeno
                    </button>
                </form>
                %elif stanje == "Rezervacija še prihaja":
                <form method="POST" action="/naredi_prispelo/{{st_lokacije}}{{st_miza}}/">
                    <button class="button is-large is-warning">  
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
                    <button class="button is-large is-success">  
                    {{miza.stevilka}} 
                    <br>
                    Prosto
                    </button>
                </form>
                %end
            %end
            </div>
        %end
    %end
</div>
%if len(katere_mize) == 1:
<a href="/nova_miza/{{katere_mize[0]}}/" class="button">DODAJ NOVO MIZO</a>
%else:
<a href="/nova_miza/" class="button">DODAJ NOVO MIZO</a>
%end
