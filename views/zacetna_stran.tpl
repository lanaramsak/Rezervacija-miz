% rebase('osnova.tpl')

<div class="column is-one-half">
<table class="table is-bordered is-hoverable"> 
    <h1 class="tittle is-1">Pregled prihodnih rezervacij</h1>

    <tr> <th>Rezervacija</th> <th>Število oseb</th> <th>Ura</th> <th>Miza</th>  <th>Prekliči</th>  </tr>
    % for rezervacija, miza in vse_rezervacije: 
    <tr> <td>{{rezervacija.ime}}</td>   <td>{{rezervacija.stevilo_oseb}}</td> <td>{{rezervacija.datum}}</td> <td>{{miza}}</td>  
        <td>
            <form method="POST"  action="/opravi/">
                <button> X </button>
            </form>
        </td>   
    </tr>
    % end
</table>
</div>

<a href="/nova_rezervacija/" class="button">DODAJ NOVO REZERVACIJO</a>
