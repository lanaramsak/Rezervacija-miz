<h1 class="title is-1"> Tu dodamo mizo</h1>

<form class="box" method="POST" action="/nova_miza/">
    <label for="st_oseb"> Število oseb:</label>
    <input type="number" id="st_oseb" name="st_oseb" required>
    <br><br>
    %if len(vse_lokacije) == 1:
        Lokacija: {{vse_lokacije[0]}}
    %else:
    <label for="lokacija">Lokacija miza:</label>
    <select name="lokacija" id="lokacija">
        %for lokacija in vse_lokacije:
        <option value="{{lokacija}}">{{lokacija}}</option>
        %end
    </select>
    %end
    <br><br>
    <input type="submit" value="Dodaj mizo">
</form>