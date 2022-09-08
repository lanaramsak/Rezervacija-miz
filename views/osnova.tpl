<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.9.4/css/bulma.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <link rel="stylesheet" href="/static/dodatki.css">
    <title> Rezervacije </title>
</head>

<body>

<h1 class="title"> Restavracija {{ime_restavracije}} </h1>

<div class="column is-one-third">
    <aside class="menu">
        <p class="menu-label">
          Ne vem še kaj tukaj napisati
        </p>
        <ul class="menu-list">
            <li><a class="is-active">Pregled vseh rezervacij</a>
            <a>Pregled vseh miz</a>
                <ul>
                    %for lokacija in vse_lokacije:
                        <li><a>{{lokacija}}</a></li>
                    %end
                        <li>
                            <a>
                            <form method="POST" action="/dodaj_lokacijo/">
                                <input type="text" id="lokacija" name="lokacija" placeholder="Dodaj lokacijo...">
                            </form>
                            </a>
                        </li>
                    
                </ul>
            </li>
        </ul>
    </aside>
</div>


    {{!base}}

</body>



</html>