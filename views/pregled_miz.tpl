% rebase('osnova.tpl', ime_strani = "pregled_miz")

<table>
    %for lokacija in katere_mize:
        <tr>
        %for miza in vse_mize[lokacija]:
            %if miza.zasedenost:
            <td>
            <div class="box">  
                {{miza.stevilka}}
                <br>
                Zasedeno
            </div>
            </td>
            %else:
            <td>
            <div class="box">  
                {{miza.stevilka}} 
                <br>
                Prosto
            </div>
            </td>
            %end
        %end
        </tr>
    %end
</table>

<a href="/nova_miza/" class="button">DODAJ NOVO MIZO</a>