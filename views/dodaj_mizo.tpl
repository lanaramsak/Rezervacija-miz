% rebase('osnova.tpl', menu = False)

<form method="POST">
    <h1 class="title is-large">Dodaj novo mizo</h1>
    <div class="box">
    <div class="control">
        <label for="st_oseb"> Število oseb:</label>
        <input type="number" id="st_oseb" name="st_oseb" required>
    </div>
    <br><br>
    %if len(vse_lokacije) == 1:
        Lokacija: {{vse_lokacije[0]}}
    %else:
    <label for="lokacija">Lokacija miza:</label>
    <div class="control">
        <select name="lokacija" id="lokacija">
            %for lokacija in vse_lokacije:
            <option value="{{lokacija}}">{{lokacija}}</option>
            %end
        </select>
    </div>
    %end
    <br><br>
    <div class="control">
    <input type="submit" value="Dodaj mizo">
    </div>
    </div>
</form>