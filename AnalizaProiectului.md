# Sistem de climatizare 


## Scopul aplicatiei

Implementarea functionalitatii unui sistem de climatizare smart. Aparatul isi va putea auto-regla sistemul de incalzire intr-o camera in functie de diferiti parametrii pe care sa-i ia in considerare la un anumit interval de timp, cum ar fi: numarul de persoane din camera, temperatura din interior, cu posibilitatea setarii manuale a parametrilor doriti.


## Obiectivele aplicatiei

- Sistem de circulatie a aerului ce asigura o climatizare dorita.
- Reglaj automat al puterii in functie de numarul de persoane din camera.
- Sa aiba cel putin o setare predefinita din fabrica.
- Afisarea temperaturii din camera transmise de un senzor de temperatura .
- Comunicarea cu sistemul de climatizare.


## Grupul tinta

Clientii care au camere mari/de interes profesional (sali de conferinta, sali de spitale, sali de sauna).

## Cerinte

- Sistemul de climatizare va pune in miscare aerului incaperii si va modifica/pastra corespunzator temperatura acesteia, conform setarilor.
- Aplicatia va identifica cu ajutorul senzorilor fluctuatia numarului de oameni din camera/sala.
- Aplicatia va primi si afisa informatii legate de temperatura camerei/salii de la un termostat extern pe un ecran atasat de aparat.
- Aplicatia va modifica temperatura camerei/salii in functie de informatia primita de la termostat si numarul de persoane din camera.
- Aplicatia va comunica cu utilizatorul requesturilor URL despre setarile pe care le alege.
- Interfata aplicatiei va afisa toate seturile de setari disponibile si va permite adaugarea si stergerea de noi seturi.
- Interfata aplicatiei va face un back-up al setarilor prin autentificare pentru urcare fisiere in Cloud Google.
- Seturile de setari cuprind temperatura dorita, numarul de persoane setat, o denumire si data la care a fost creat.

## Cerinte nereusite
- Sa modificam temperatura in functie de dimensiunea camerei
- Sa adaugam o interfata grafica ce se poate accesa din display.

## Prioritizarea cerintelor dupa optiunile sistemului

##### General:
- Sistemul de climatizare va pune in miscare aerului incaperii si va modifica/pastra corespunzator temperatura acesteia, conform setarilor.
- Seturile de setari (Default si cele Custom, adaugate de utilizator) cuprind temperatura dorita, numarul de persoane setat, o denumire si data la care a fost creat.

##### Termostat:
- Aplicatia va primi informatii legate de temperatura camerei/salii de la un termostat.
- Aplicatia va modifica temperatura camerei/salii in functie de informatia primita de la termostat.

##### Numarul persoanelor din camera/sala:
- Aplicatia va identifica cu ajutorul senzorilor fluctuatia numarului de oameni din camera/sala.
- Aplicatia va modifica puterea de circulare a aerului in functie de numarul de persoane din aceasta.

##### HTTP:
- Aplicatia va comunica cu utilizatorul requesturilor URL despre setarile pe care le alege.
- Interfata aplicatiei va afisa toate setarile disponibile si va permite adaugarea si stergerea de noi setari, precum si alegerea setarii dorite a fi pusa in functiune.
- Interfata aplicatiei va afisa si un back-up al setarilor prin autentificare.


## Motivatie
 (~~Inca nu am caldura in casa~~)
 
**Nevoia unui sistem de climatizare inteligent care nu necesita interventia utilizatorului la fiecare schimbare a parametrilor.**
