% rebase('osnova.tpl', ime_strani = "pregled_rezervacij", menu = True)

<div class="column is-one-half">
<table class="table is-bordered is-hoverable"> 
    <h1 class="tittle is-1">Pregled prihodnih rezervacij</h1>

    <tr> <th>Rezervacija</th> <th>Število oseb</th> <th>Ura</th> <th>Miza</th>  <th>Prekliči</th>  </tr>
    % for id_rezervacije, (rezervacija, miza, prispelost) in enumerate(vse_rezervacije): 
        %if prispelost == 1:
        <tr class = "is-selected"> <td>{{rezervacija.ime}}</td>   <td>{{rezervacija.stevilo_oseb}}</td> <td>{{rezervacija.datum}}</td> <td>{{miza}}</td>  
            <td>
                <form method="POST"  action="/prispelo/{{id_rezervacije}}/">
                    <button> Prispela </button>
                </form>
                <form method="POST"  action="/preklici/{{id_rezervacije}}/">
                    <button> Prekliči </button>
                </form>
            </td>   
        </tr>
        %else:
        <tr> <td>{{rezervacija.ime}}</td>   <td>{{rezervacija.stevilo_oseb}}</td> <td>{{rezervacija.datum}}</td> <td>{{miza}}</td>  
            <td>
                <form method="POST"  action="/prispelo/{{id_rezervacije}}/">
                    <button> Prispela </button>
                </form>
                <form method="POST"  action="/preklici/{{id_rezervacije}}/">
                    <button> Prekliči </button>
                </form>
            </td>   
        </tr>
        % end
    % end
</table>
</div>

<a href="/nova_rezervacija/" class="button">DODAJ NOVO REZERVACIJO</a>