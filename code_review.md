# Kodgranskning av order_report.py

## Utgångsläge
Scriptet går att köra och skapar rapporter över bland annat försäljning och returer. Däremot ligger nästan all funktionalitet i samma fil och
kodblock, vilket gör lösningen svår att testa, återanvända och
vidareutveckla.

## Granskningsfynd

### Fynd 1 - Hela programmet körs vid import

**Observation:** Hela arbetsflödet körs på modulnivå.

**Konsekvens:** Import läser och skriver filer. Koden får oväntade sidoeffekter och blir svår att återanvända och testa.

**Förslag:** Lägg programstarten i en 'main()'-funktion och skydda anropet med en main-guard.


### Fynd 2 - Flera ansvar är sammanblandade

**Observation:** Scriptet blandar filhantering, validering, transformationslogik, rapportering och programflöde.

**Konsekvens:** Delarna kan inte testas och återanvändas oberoende av varandra, olika typer av förändringar behöver göras på samma plats.

**Förslag:** Separera filinläsning, validering, transformationslogik, rapportering och programflöde i olika moduler.


### Fynd 3 - Valideringen ger ett generellt fel

**Observation:** Valideringen kastar 'Exception' med meddelandet 'Fel data'.

**Konsekvens:** Felet är svårt att felsöka och svårt att kontrollera specifikt i ett automatiskt test. Det frågar inte vilka kolumner som saknas.

**Förslag:** Kasta 'ValueError' och namnen på den saknade kolumnerna.


### Fynd 4 - Statusmeddelanden använder print

**Observation:** 'print()' används för att beskriva att programmet läser data och att körningen är klar.

**Konsekvens:** Det går inte att styra nivå, format, destination, och det framgår inte vilken modul som skapade meddelandet.

**Förslag:** Använd modulloggers för körinformation och konfigurera loggning centralt vid programmets startpunkt.


### Fynd 5 - Duplicerad kod

**Observation:** Rapporterna för produktkategori och region innehåller mycket likadan kod. Båda grupperar data och beräknar order_count, total_sales, returns och return_rate, och sorterar sedan resultatet.

**Konsekvens:** Duplicerad kod gör programmet längre och ökar risken för fel. Om beräkningen behöver ändras måste samma förändring göras på flera ställen.

**Förslag:** Skapa en återanvändbar funktion för den gemensamma rapportlogiken. Funktionen kan exempelvis ta emot vilken kolumn som rapporten ska grupperas efter.


### Fynd 6 - Sökvägar och förutsättningar är hårdkodade

**Observation:** Sökvägarna till indata och utdata är hårdkodade i programmet och scriptet förutsätter att outputmappen finns.

**Konsekvens:** Det blir svårare att köra programmet med andra filer och att testa det med tillfälliga sökvägar. Att outputmappen måste finnas är en förutsättning som inte hanteras av programmet.

**Förslag:** Samla sökvägarna i en liten konfiguration och skapa outputmappen automatiskt vid programstart.


## Sammanfattning
Originalprogrammet fungerar och producerar de förväntade rapporterna, men strukturen kan förbättras. De viktigaste förbättringarna är att separera ansvar, minska duplicerad kod, göra logiken mer testbar, ersätta print() med logging och förbättra felhanteringen och valideringen.