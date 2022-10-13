<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.9.4/css/bulma.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <title> Rezervacije </title>
</head>

<body>

<h1 class="title"> Restavracija {{ime_restavracije}} </h1>

<nav class="navbar">
  <div class="container">
    <div id="navMenu" class="navbar-menu">

      <div class="navbar-end">
        <div class="navbar-item">
          <div class="buttons">
            <a class="button is-dark">Github</a>
            <a class="button is-link">Odjava</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</nav>

<div class="column is-one-third">
    <aside class="menu">
        <p class="menu-label">
          Ne vem še kaj tukaj napisati
        </p>
        <ul class="menu-list">
            <li><a href="/pregled_rezervacij/">Pregled prihajajočih rezervacij </a>
            <li><a href="/pregled_preteklih_rezervacij/">Pregled preteklih rezervacij </a>
            <a href="/pregled_miz/">Pregled vseh miz</a>
                <ul>
                    %for lokacija in vse_lokacije:
                        <li><a href="/pregled_miz/{{lokacija}}/">{{lokacija}}</a></li>
                    %end
                        <li>
                            <a>
                            <form method="POST" action="/dodaj_lokacijo/">
                                <input type="text" id="lokacija" name="lokacija" placeholder= "Ime lokacije..." >
                            </form>
                            </a>
                        </li>
                    
                </ul>
            </li>
            <li>
                <form method="POST" action="/odjava/">
                    <div class="button">
                        Odjavi se
                    </div>
                </form>
            </li>
        </ul>
    </aside>
</div>


    {{!base}}

</body>



</html>