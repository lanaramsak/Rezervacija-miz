% rebase('osnova.tpl')

<h1 class="title is-1">Tu dodamo rezervacijo</h1>

<form class="box" method="POST" action="/nova_rezervacija/">
    <label for="ime">Ime rezervacije:</label>
    <input type="text" id="ime" name="ime" placeholder="..." required>
    <br><br>
    <label for="ura">Datum in ura rezervacije:</label>
    <input type="datetime-local" id="ura" name="ura" required>
    <br><br>
    <label for="st_oseb"> Število gostov:</label>
    <input type="number" id="st_oseb" name="st_oseb" required>
    <br><br>
    <label for="lokacija">Kje želite sedeti?</label>
    <select name="lokacija" id="lokacija">
        %for lokacija in vse_lokacije:
        <option value="{{lokacija}}">{{lokacija}}</option>
        %end
    </select>
    <br><br>
    <input type="submit" value="Želim rezervirati mizo">

    %if uspesnost == False:
        <div class="box">
        Žal rezervacija ni možna, poskusite morda ob kakšni drugi uri ali drugem datumu.
        </div>
    %end

</form>