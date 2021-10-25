# Sistem de climatizare 


## Scopul aplicatiei

Implementarea functionalitatii unui sistem de climatizare smart. Aaparatul va putea pastra temperatura constanta intr-o camera in functie de diferiti parametrii pe care sa-i ia in considerare la un anumit interval de timp, cum ar fi: numarul de persoane din camera, volumul camerei si temperatura din interior, cu posibilitatea setarii manuale in 2 optiuni, Default si Custom.


## Obiectivele aplicatiei

- Sistem de circulatie a aerului ce asigura o climatizare dorita (~~As vrea ca sistemul sa circule aer de o anumita temperatura in camera pentru a asigura climatizarea dorita.~~)
- Reglaj in functie de dimensiunea camerei/salii (~~As vrea ca sistemul sa ia in considerare dimensiunea camerei in care se afla.~~)
- Reglaj automat in functie de numarul de persoane din camera (~~As vrea ca sistemul sa ia in considerare numarul de persoane dintr-o camera.~~)
- Optiunea “Default” pentru temperatura constanta de 20 C (~~As vrea ca un utilizator obisnuit sa poata pune aparatul pe optiunea “Default” care tine temperatura camerei constant la 20 C.~~)
- Optiunea “Custom” pentru temperatura constanta setata de utilizator  (~~As vrea ca un utilizator obisnuit sa poata pune o temperatura “Custom” in aparat.
As vrea ca un utilizator mai avansat (spre exemplu o asistenta medicala) sa poata seta aparatul pentru cazuri mai particulare, in functie de ce pacienti are (pacienti cu febra sau cu diferite afectiuni/ tensiune).~~)
- Comunicarea cu un termostat (pornirea si oprirea circulatiei aerului bazata doar pe fluctuatia temperaturii din camera/sala)


## Grupul tinta

Clientii care au camere mari/ de interes profesional (sali de conferinta, sali de spitale, sali de sauna).

## Cerinte

- Sistemul de climatizare va pune in miscare aerului incaperii si va modifica/pastra corespunzator temperatura acesteia, conform setarilor.
- Aplicatia va determina termperatura optima pentru fiecare tip de incapere (mica, medie, mare, open-space).
- Aplicatia va modifica temperatura conform fiecarui tip de camera/sala.
- Aplicatia va identifica cu ajutorul senzorilor fluctuatia numarului de oameni din camera/sala.
- Aplicatia va modifica temperatura camerei/salii in functie de numarul de persoane din aceasta.
(~~Implementam 2 senzori care ne spun daca o persoana (un om) intra sau iese din camera~~)
- Aplicatia va primi informatii legate de temperatura camerei/salii de la un termometru extern.
- Aplicatia va modifica temperatura camerei/salii in functie de informatia primita de la termometru.
(~~Implementam 1 termometru in camera care ne spune temperatura in camera~~)
- Aplicatia va comunica cu utilizatorul cu ajutorul unei interfete.
- Interfata aplicatiei va afisa toate optiunile sistemului de climatizare intr-un meniu (setarea dimensiunii camerei, afisarea numarului de persoane din incapere, temperatura curenta, optiunea Default si Custom).
- Optiunile Default si Custom vor circula aerul la o temperatura constanta, fara a lua in considerare si celelalte criterii (numarul de persoane, temperatura existenta, dimensiunea).
(~~Implementam o interfata cu care utilizatorul pune setarile (Custom)
Implemetam un software care pune in circulatie aer~~)


## Prioritizarea cerintelor dupa optiunile sistemului

##### General:
- Sistemul de climatizare va pune in miscare aerului incaperii si va modifica/pastra corespunzator temperatura acesteia, conform setarilor.
- Optiunile Default si Custom vor circula aerul la o temperatura constanta, fara a lua in considerare si celelalte criterii (numarul de persoane, temperatura existenta, dimensiunea).

##### Numarul persoanelor din camera/sala:
- Aplicatia va identifica cu ajutorul senzorilor fluctuatia numarului de oameni din camera/sala.
- Aplicatia va modifica temperatura camerei/salii in functie de numarul de persoane din aceasta.

##### Dimensiunea camerei/salii:
- Aplicatia va determina termperatura optima pentru fiecare tip de incapere (mica, medie, mare, open-space).
- Aplicatia va modifica temperatura conform fiecarui tip de camera/sala.

##### Termostat:
- Aplicatia va primi informatii legate de temperatura camerei/salii de la un termometru extern.
- Aplicatia va modifica temperatura camerei/salii in functie de informatia primita de la termometru.

##### Interfata:
- Aplicatia va comunica cu utilizatorul cu ajutorul unei interfete.
- Interfata aplicatiei va afisa toate optiunile sistemului de climatizare intr-un meniu (setarea dimensiunii camerei, afisarea numarului de persoane din incapere, temperatura curenta, optiunea Default si Custom).

(~~Implemetam un software care pune in circulatie aer
Implementam o interfata cu care utilizatorul pune setarile (Custom)
Implementam 1 termometru in camera care ne spune temperatura in camera
Implementam 2 senzori care ne spun daca o persoana (un om) intra sau iese din camera~~)


## Motivatie
 (~~Inca nu am caldura in casa~~)
 
**Nevoia unui sistem de climatizare inteligent care nu necesita interventia utilizatorului la fiecare schimbare a parametrilor.**
