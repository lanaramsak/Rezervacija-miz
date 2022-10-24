<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Zacetna stran</title>
    <link rel="stylesheet" href="https://unpkg.com/bulma@0.9.0/css/bulma.min.css" />
    <script src="https://kit.fontawesome.com/d8381f64c2.js" crossorigin="anonymous"></script>
  </head>

  <body>
    <div class="header-wrapper">
      <section class="hero" style="background-color:#8ebff0;">
        <div class="hero-body">
          <div class="container">
            <div class="level">
              <div class="level-item">
                <div class="image">
                  <img src="/static/Nella.png" />
                </div>
              </div>
              <div class="level-item">
                <h2 class="title is-1 is-spaced" style="color:white;">NELLA</h2>
              </div>
              <div class="level-item">
                <h1 class="subtitle profession">Organizacija rezervacij še nikoli ni bila tako preprosta.</h1>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
    
    <section class="hero is-fullheight">
      <div class="hero-body">
        <div class="container has-text-centered">
          <div class="columns is-8 is-variable">
            <div class="column is-7 has-text-left">
              <div class="main-content">
                <div class="section-light">
                  <div class="container">
                    <h1 class="title has-text-centered section-title">Kako deluje?</h1>
                    <div class="columns is-multiline">
                      <div
                        class="column is-6 has-vertically-aligned-content"
                      >
                        <p class="is-larger">
                         <strong>Nella je program, ki pripomore k boljši organizaciji rezervacij in zasedenosti miz. 
                          Vsaka restavracija se lahko prijavi in tako lažje vodi evidenco vseh prihodnih in preteklih rezervacij.</strong
                          >
                        </p>
                        <br />
                        <p>
                          Vašo restavracijo lahko preprosto prenesete v elektronsko obliko. 
                          Mize lahko uredite glede na njihovo lokacijo in število gostov, ki jih sprejmejo. 
                          Tako bo Nella ob dodani rezervacij sama preračunala kam lahko posede ljudi in vam to tudi sporočila. 
                          Vse kar ostane vam, je da ob prihodu rezervacije to označite.
                        </p>
                        <br />
                      </div>
                      <div class="column is-6 right-image " data-aos="fade-left">
                          <p class="image is-12">
                              <img
                              src="https://media.istockphoto.com/photos/reserved-sign-on-restaurant-table-picture-id534761709?k=20&m=534761709&s=612x612&w=0&h=VeUecEqiNvdr7cebKYWjPvFJ3G-UZf-NWjiI8DboLKU="
                              alt="Slika znaka rezervacija"
                              />
                          </p>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="column">
              <div class="section-dark resume" id="prijava">
                <div class="container">
                  <div>
                    <div class="column is-12 about-me">
                      <h1 class="title has-text-centered section-title">
                        Prijava
                      </h1>
                    </div>
                    <div class="column is-10 has-text-centered is-offset-1">
                      <hr class="login-hr">
                        <form method="POST" action="/prijava/">
                          <div class="field">
                            <div class="control">
                              <input class="input is-medium" type="text" placeholder="Ime restavracije" name="ime_restavracije" required>
                            </div>
                          </div>

                          <div class="field">
                            <div class="control">
                              <input class="input is-medium" type="password" placeholder="Geslo" name="geslo" required>
                            </div>
                          </div>
                          
                          <div class="field">
                            %if napaka:
                              <p class="help is-danger">{{ napaka }}</p>
                            %end
                          </div>
                  
                          <nav class="level">
                            <div class="level-left">
                              <div class="level-item">
                                <input class="button is-info is-medium is-10" type="submit" value="Prijavi se">
                              </div>
                              <div class="level-item">
                                <a class="button is-block is-medium is-10" href="/registracija/">Registracija</a>
                              </div>
                            </div>
                          </nav>
                        </form>
                    </div>      
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </body>
</html>