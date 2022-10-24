% rebase('osnova.tpl', ime_strani = "Pregled miz", menu = True)

<div>
    %for st_lokacije,lokacija in enumerate(vse_lokacije):
        %if lokacija in katere_mize:
            <div class="box" style="margin-bottom:10px;">
                <div class="buttons">
            %for st_miza, miza in enumerate(vse_mize[lokacija]):
                %stanje = miza.preveri_zasedenost()
                %if stanje == "Zasedeno":
                <div class="box" style="margin-right: 10px; margin-bottom: 10px; margin-top: 10px;">
                <form method="POST" action="/naredi_prosto/{{st_lokacije}}{{st_miza}}/">
                    <button class="button is-large is-danger">  
                    {{miza.stevilka}}
                    <br>
                    Zasedeno
                    </button>
                </form>
                <form method="POST" action="/brisi_mizo/{{st_lokacije}}{{st_miza}}/"><button class="delete"></button></form>
                </div>
                %elif stanje == "Rezervacija še prihaja":
                <div class="box" style="margin-right: 10px; margin-bottom: 10px; margin-top: 10px;">
                <form method="POST" action="/naredi_prispelo/{{st_lokacije}}{{st_miza}}/">
                    <button class="button is-large is-warning">  
                    {{miza.stevilka}}
                    <br>
                    Rezervacija prihaja
                    </button>
                </form>
                <form method="POST" action="/prekliči_rezervacijo/{{st_lokacije}}{{st_miza}}/">
                    <button>
                        Prekliči rezervacijo
                    </button>
                </form>
                </div>
                %else:
                <div class="box" style="margin-right: 10px; margin-bottom: 10px; margin-top: 10px;">
                <form method="POST" action="/naredi_zasedeno/{{st_lokacije}}{{st_miza}}/">
                    <button class="button is-large is-success">  
                    {{miza.stevilka}} 
                    <br>
                    Prosto
                    </button>
                </form>
                <div class="level">
                    <div class="level-item">
                        <form method="POST" action="/brisi_mizo/{{st_lokacije}}{{st_miza}}/"><button class="delete is-center"></button></form>
                    </div>
                    %if miza.naslednja_rezervacija():
                    <div class="level-right text-centered">
                        <div class="level-item">
                                Nalsednja rezervacija: <br>
                                {{miza.naslednja_rezervacija()}}
                        </div>
                    </div>
                    %end
                </div>
                </div>
                %end
            %end
            </div>
            </div>
        %end
    %end
</div>
%if len(katere_mize) == 1:
<a href="/nova_miza/{{katere_mize[0]}}/" class="button">DODAJ NOVO MIZO</a>
%else:
<a href="/nova_miza/" class="button">DODAJ NOVO MIZO</a>
%end
