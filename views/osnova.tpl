% zavihki = [
%     'Pregled rezervacij',
%     'Pregled preteklih rezervacij',
%     'Pregled miz'
% ]
% url_zavihka = {
%     'Pregled rezervacij': 'pregled_rezervacij',
%     'Pregled preteklih rezervacij': 'pregled_preteklih_rezervacij',
%     'Pregled miz': 'pregled_miz'
% }

<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.9.4/css/bulma.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <script src="https://kit.fontawesome.com/d8381f64c2.js" crossorigin="anonymous"></script>
    <title> Rezervacije </title>
</head>

<body>

<br><br>

<nav class="navbar is-info">
  <div class="container">
    <div id="navMenu" class="navbar-menu">
        <div class="navbar-brand">
            <h1 class="title is-large is-white">NELLA</h1>
        </div>

        <div class="navbar-end">
            <div class="navbar-item">
            <div class="buttons">
                <a class="button is-dark" action="https://github.com/lanaramsak"> 
                    <span class="icon-text">
                        <span class="icon">
                            <!--<i class="fa-brands fa-github"></i>-->
                        </span>
                        <span>Github</span> 
                    </span>
                </a>
                <form method="POST" action="/odjava/">
                    <button class="button is-link"> 
                        <span class="icon-text">
                            <span class="icon">
                                <!--<i class="fa-regular fa-right-from-bracket"></i>-->
                            </span>
                            <span>Odjava</span>
                        </span>
                    </button>
                </form>
            </div>
            </div>
        </div>
    </div>
  </div>
</nav>

<section class="section">
    <div class="container">
        <div class="columns">
        <div class="column is-3">
            %if menu:
            <aside class="menu">
                <p class="menu-label">
                RESTAVRACIJA {{ime_restavracije}}
                </p>
                <ul class="menu-list">
                    %for stran in zavihki:
                        %if defined('ime_strani') and ime_strani == stran:
                            <li><a class="is-active" href="/{{url_zavihka[stran]}}/">{{stran}}</a></li>
                        %else:
                            <li><a href="/{{url_zavihka[stran]}}/">{{stran}}</a></li>
                        %end
                    %end
                    <li>
                        <ul>
                            %for lokacija in vse_lokacije:
                                <li>
                                    <div class="level">
                                            <div class="level-left">
                                                <a href="/pregled_miz/{{lokacija}}/">
                                                <div class="level-item">
                                                    {{lokacija}}
                                                </div>
                                                </a>
                                            </div>
                                            <div class="level-right">
                                                <div class="level-item">
                                                    <a href="/izbrisi_lokacijo/{{lokacija}}/"><button class="delete"></button></a>
                                                </div>
                                            </div>
                                    </div>
                                </li>
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
                </ul>
            </aside>
            %end
        </div>
        <div class="column is-9">
            {{!base}}
        </div>
        </div>
    </div>
</section>

</body>

</html>