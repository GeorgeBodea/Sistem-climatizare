# Sistem Climatizare Inteligent

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#descriere">Descriere</a>
      <ul>
        <li><a href="#tehnologii">Tehnologii utilizate</a></li>
      </ul>
    </li>
    <li>
      <a href="#utilizare">Utilizare</a>
      <ul>
        <li><a href="#prerequirements">Pre-requirements</a></li>
        <li><a href="#rulare">Rulare</a></li>
      </ul>
    </li>
    <li><a href="#echipa">Echipa de dezvoltare</a></li>
  </ol>
</details>

## <a id="descriere">Descriere</a>

__Sistemul de climatizare inteligent__ este conceput pentru a functiona cat mai simplu venind in ajutorul utilizatorilor pentru ca isi modifica singur temperatura si puterea cu care se circula aerul.

Aplicatia sistemului permite si alegerea de setari __default__ si adaugarea se seturi de setari __custom__ potrivite pentru necesitatile fiecaruia. Sistemul este conectat la un sistem de __senzori de miscare__ care determina si modifica numarul de persoane din camera si la un __termostat__ care transmite temperatura curenta din camera.


### <a id="tehnologii">Tehnologii utilizate</a>
 * Python 3.10
 * API MQTT si AsyncAPI
 * REST API HTTP si OpenAPI
 * Firebase
 * Eclipse Mosquitto
 * Paho-mqtt
 * Pytest
 
 ## <a id="utilizare">Utilizare</a>
 Sistemul de climatizare este bagat in priza si apasat pe butonul de deschidere.

Se acceseseaza URL-ul: __localhost:8088/[suffix]__

__[suffix]__ poate fi:

__fisere_custom__ -> se afiseaza numele setarilor (Se va afisa cel putin numele Default si restul numelor setarilor adaugate)

__fisiere_custom/[nume_setare]__ -> se afiseaza detalii despre setarea cu numele [nume_setare]

__adaugare_setare__ -> se scriu detalii despre setare: nume setare, numar persoane, temperatura. Se apasa butonul Submit pentru finalizare.

__alegere_setare__ -> se scrie numele setarii pentru ca sistemul de climatizare sa functioneze in functie de parametrii. Pentru simplitate se afiseaza si numele setarilor.

__stergere_setare__ -> se scrie numele setarii pentru a fi sters. Pentru simplitate se afiseaza si numele setarilor.

__backup_upload__ -> se scriu emailul si parola pentru autentificare cont. Setarile introduse in sistemul de climatizare (adaugate prin accesarea URL-ului localhost:8088/adaugare_setare) se vor stoca intr-o baza de date externa in cazul in care sistemul de climatizare se strica sau se doreste ca setarile sa se retina stocate altundeva decat pe sistemul de climatizare, ca mai apoi sa fie descarcate accesand URL-ul localhost:8088/backup_download (Vezi mai jos)

__backup_download__ -> se scriu emailul si parola pentru autentificare cont. Se vor descarca in sistemul de climatizare setarile stocate in baza de date externa. Setarile cu acelasi nume din baza de date externa vor suprascrie setarile existente in sistemul de climatizare.

__Note:__
1. Numele setarilor se regasesc intodeauna intre ghilimele. (Exemplu: 'Default' -> Numele setarii este Default)
2. Setarea standard Default se va afla intodeauna in aplicatie si nu poate fi sters.
3. Emailul si parola pentru autentificare backup_upload si backup_download: qwerty@qwerty.com (Emailul) si qwerty (Parola).
4. In cazul in care, accesarea URL-urilor nu se face corect (nu se introduce numele unei setari existente, se incearca un alt URL care nu este specificat mai sus, se greseste emailul si/sau parola, etc.) se va afisa o pagina de eroare (codificari precum: ERR_EMPTY_RESPONSE sau HTTP ERROR 400)
 
 ### <a id="prerequirements">Pre-requirements</a>
 * Pyhton versiunea 3.10
 * Librarie Python paho-mqtt versiune 1.6.1
 * Librarie Python pyrebase4 versiune 4.5.0
 * Librarie Python requests 2.27.1
 * Librarie Python requests-toolbelt 0.9.1
 * Eclipse Mosquitto 2.0.14
 
 
 ### <a id="rulare">Rulare</a>
 Aceasta categorie este pentru observarea functionalitatii scripturilor din aplicatie. O aplicatie reala (cu hardware propiu zis o sa ruleze toate scripturile din aplicatie si eventual, la cerere, adica din folderul __sistem_climatizare/setari_utilizator__) va utiliza componente hardware, reale precum: display (ecran pentru afisare temperatura, echivalent in aplicatie cu fisierul __display.py__), senzor_temperatura (echivalent software __senzor_temperatura.py__), circuite si placa de baza (echivalent software __hardware.py__) si senzori de intrare/iesire la usa (echivalent software __sistem_climatizare/senzori_centralizare__).
 
 Se ruleaza __app.py__ din folderul __sistem_climatizare/api_http__ cu Python. (Pentru observarea functionalitatilor legate de REST API)
 
 Se ruleaza toate scripturile de Python (inafara de cele din folderul __sistem_climatizare/setari_utilizator__ care se ruleaza la cerere din __app.py__) si __Eclipse    Mosquitto__. (Pentru observarea functionalitatilor legate de MQTT)
 
 
 ## <a id="echipa">Echipa de dezvoltare</a>
 * Barbu Iulia
 * Bodea George
 * Harsa Andrei
 * Hazaparu Daria
 * Mindruleanu Matei
 * Staicu Octavian
 
 
 
