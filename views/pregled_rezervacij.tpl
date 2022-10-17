% rebase('osnova.tpl', ime_strani = "Pregled rezervacij", menu = True)

<div class="column is-one-half">
<table class="table is-bordered is-hoverable"> 

    <tr> <th>Rezervacija</th> <th>Število oseb</th> <th>Ura</th> <th>Miza</th>  <th>Prekliči</th>  </tr>
    % for id_rezervacije, (rezervacija, miza, prispelost) in enumerate(vse_rezervacije): 
        %if prispelost == 1:
        <tr style="background-color:#8ebff0;"> <td>{{rezervacija.ime}}</td>   <td>{{rezervacija.stevilo_oseb}}</td> <td>{{rezervacija.datum}}</td> <td>{{miza}}</td>  
            <td>
                <form method="POST"  action="/prispelo/{{id_rezervacije}}/">
                    <button class="button is-small is-round is-info is-light" style="margin-bottom: 5px; margin-top: 5px;"> Prispela </button>
                </form>
                <form method="POST"  action="/preklici/{{id_rezervacije}}/">
                    <button class="button is-small is-round is-danger is-light" style="margin-bottom: 5px; margin-top: 5px; "> Prekliči </button>
                </form>
            </td> 
        </tr>
        %else:
        <tr> <td>{{rezervacija.ime}}</td>   <td>{{rezervacija.stevilo_oseb}}</td> <td>{{rezervacija.datum}}</td> <td>{{miza}}</td>  
            <td>
                <form method="POST"  action="/prispelo/{{id_rezervacije}}/">
                    <button class="button is-small is-round is-info is-light" style="margin-bottom: 5px; margin-top: 5px;"> Prispela </button>
                </form>
                <form method="POST"  action="/preklici/{{id_rezervacije}}/">
                    <button class="button is-small is-round is-danger is-light" style="margin-bottom: 5px; margin-top: 5px;"> Prekliči </button>
                </form>
            </td>   
        </tr>
        % end
    % end
</table>
</div>

<a href="/nova_rezervacija/" class="button" style="background-color:#8ebff0; margin-left: 10px;">DODAJ NOVO REZERVACIJO</a>