% rebase('osnova.tpl', ime_strani = "Pregled preteklih rezervacij", menu = True)

<div class="column is-one-half">
<table class="table is-bordered is-hoverable"> 
    <h1 class="tittle is-1 is-spaced">Pregled preteklih rezervacij</h1>

    <tr> <th>Rezervacija</th> <th>Število oseb</th> <th>Ura</th> <th>Miza</th>  <th>Opravljenost</th>  </tr>
    %for id_rezervacije, (rezervacija, miza) in enumerate(vse_rezervacije): 
    <tr> <td>{{rezervacija.ime}}</td>   <td>{{rezervacija.stevilo_oseb}}</td> <td>{{rezervacija.datum}}</td> <td>{{miza}}</td>  
        %if rezervacija.opravljenost:
        <td>Opravljeno</td>
        %else:
        <td>Neopravljeno</td>
        %end
    </tr>
    %end
</table>
</div>
