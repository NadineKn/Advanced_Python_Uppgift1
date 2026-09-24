# Orderrapportering

Ett refaktorerat Pythonprogram för att läsa in orderdata och skapa rapporter över försäljning och returer.

## Projektstruktur

* `src/order_report/main.py` – startpunkt och programflöde
* `src/order_report/config.py` – konfiguration och sökvägar
* `src/order_report/loading.py` – inläsning av data
* `src/order_report/validation.py` – validering av indata
* `src/order_report/processing.py` – datatransformationer
* `src/order_report/reporting.py` – skapande av rapporter
* `tests/` – automatiska tester

## Installation

Skapa och aktivera en virtuell miljö och installera projektets beroenden:

```bash
python -m pip install -r requirements.txt
```

## Köra programmet

Kör från projektmappen:

```bash
python -m order_report.main
```

Programmet läser orderdata från `data/orders.csv` och skapar följande rapporter i `output/`:

* `overview.csv`
* `sales_by_category.csv`
* `sales_by_region.csv`
* `returns_by_category.csv`

## Köra tester

Kör alla tester med:

```bash
python -m pytest -v
```

Tester finns i mappen `tests/` och kontrollerar bland annat rapportberäkningar och validering av indata.


## Reflektion
1. Vilka var de viktigaste problemen i originalkoden?

Det viktigaste problemet var att nästan all funktionalitet låg i samma fil. Filinläsning, validering, datatransformation, rapportering och programflöde var blandat. Det fanns också duplicerad kod, print() för statusmeddelanden och en generell felhantering som gjorde fel svårare att förstå.

2. Vilka förändringar tycker du förbättrade programmet mest?

Jag tycker att uppdelningen i separata moduler och borttagningen av duplicerad kod förbättrade programmet mest. Även tydligare validering, logging och automatiska tester gör programmet lättare att förstå, testa och ändra.

3. Varför valde du den projektstruktur du använde?

Jag valde att dela upp programmet efter ansvar. Inläsning, validering, transformationer och rapportering har olika uppgifter och kan därför ligga i separata moduler. main.py fungerar som programmets startpunkt och håller ihop arbetsflödet.

4. Var använde du OOP/dataclass och varför passade det där?

Jag använde en dataclass i config.py för programmets konfiguration. Config innehåller sökvägarna till indata och utdata. Det passar bra eftersom konfigurationen är en tydlig och avgränsad del av programmet. frozen=True gör konfigurationen oföränderlig.

5. Vilka viktiga beteenden skyddar dina automatiska tester, och vilken nytta ger testerna om programmet förändras i framtiden?

Testerna skyddar bland annat beräkningen av sammanfattningen, rapporterna per kategori och region samt valideringen av obligatoriska kolumner. De kontrollerar både förväntade resultat och ett felscenario. Om programmet ändras i framtiden kan testerna snabbt visa om en förändring har påverkat befintlig funktionalitet.

6. Vad var svårast?

Det svåraste var att dela upp den ursprungliga koden i mindre delar utan att förändra resultatet. Jag behövde kontrollera att de nya funktionerna fortfarande skapade samma rapporter som originalprogrammet.

7. Vad hade du velat förbättra ytterligare om du haft mer tid?

Jag hade velat lägga till fler tester för exempelvis datatransformationer och felaktiga värden. Jag hade också kunnat utveckla loggingen så att det tydligare framgår vilka rapporter som skapats och var de sparats.