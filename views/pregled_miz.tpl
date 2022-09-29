% rebase('osnova.tpl', ime_strani = "pregled_miz")

<table>
    %for st_lokacije,lokacija in enumerate(katere_mize):
        <tr>
        %for st_miza, miza in enumerate(vse_mize[lokacija]):
            %if miza.zasedenost:
            <td>
            <form method="POST" action="/naredi_prosto/{{st_lokacije}}{{st_miza}}/">
            <button>  
                {{miza.stevilka}}
                <br>
                Zasedeno
            </button>
            </form>
            </td>
            %else:
            <td>
            <form method="POST" action="/naredi_zasedeno/{{st_lokacije}}{{st_miza}}/">
            <button>  
                {{miza.stevilka}} 
                <br>
                Prosto
            </button>
            </form>
            </td>
            %end
        %end
        </tr>
    %end
</table>

<a href="/nova_miza/" class="button">DODAJ NOVO MIZO</a>