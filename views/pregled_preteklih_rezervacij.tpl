% rebase('osnova.tpl', ime_strani = "Pregled preteklih rezervacij", menu = True)

<div class="column">
<table class="table is-bordered is-hoverable is-fullwidth"> 
    <h1 class="tittle is-1 is-spaced">Pregled preteklih rezervacij</h1>

    <tr style="background-color:#8ebff0;"> <th>Rezervacija</th> <th>Število oseb</th> <th>Ura</th> <th>Miza</th>  <th>Opravljenost</th>  </tr>
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

<div class="box" style="background-color:#8ebff0;">
    <form method="POST">
        <div class="level">
            <div class="level-item level-left">
                <label for="leto">Razporejenost rezervacij skozi leto:</label>
                <input type="number" id="leto" name="leto" placeholder= "2022..." >
                %if napaka:
                <p class="help is-danger">{{ napaka }}</p>
                %end
            </div>
            <div class="level-item">
                <button class="button is-small">Naredi</button>
            </div>
        </div>
    </form>
</div>
</div>