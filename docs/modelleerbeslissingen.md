# HG2 v0.5: modelleerbeslissingen

## 1. Drie niveaus, geen automatische gelijkstelling
- `PlaceReference` = verwijzing in broncontext, nog geen vastgestelde plaatsidentiteit.
- `PlaceAssertion` = brongebonden inhoud/waarneming; bewijst de historische werkelijkheid niet zelfstandig.
- `Place` = na identificatie aangenomen geografische identiteit.
- `PlaceState` = geïnterpreteerde, tijdgebonden toestand van een `Place`, niet automatisch elk bronrecord.
- `HistoricalRelation` = geïnterpreteerde relatie tussen twee geïdentificeerde `Place`-instanties.

## 2. Evidence en interpretatie
`Place` kan met `identityEvidence` naar bronreferenties verwijzen. `PlaceState` kan met `interpretationOf` naar bronuitspraken verwijzen. `HistoricalRelation` kan met `relationEvidence` verantwoord worden. Deze relaties houden het verschil tussen bron en interpretatie expliciet.

## 3. Tijd
`observedStartDate`, `observedEndDate` en `uninterpretedDate` zijn bronwaarden. Ze impliceren geen bestaansduur, juridische oprichtingsdatum of dateringsperiode. Pas na broninterpretatie een `validDuring` toe. `sourceDate` is alleen de productiedatering van de bron, niet het historische jaar waarop die bron betrekking heeft.

## 4. Geometrie
`observedGeometry` is de brongeometrie. Een `PlaceState` kan een `hasGeometry` hebben wanneer een historische ruimtelijke toestand is gereconstrueerd. Deze geometrieën hoeven niet hetzelfde te zijn.

## 5. Historische herindeling
`absorbedBy` en `originatedFrom` uit de oude hg-ontologie worden niet blind naar HG2 omgezet. Eerst onderscheiden: bestuurlijk-juridische opvolging, ruimtelijk opgaan in, en wijziging van grenzen zonder nieuwe identiteit.

## 6. Niet doen
- Geen automatische `owl:sameAs` op grond van naam, code of punt.
- Geen automatische `PlaceState` per gemeenterecord.
- Geen automatische interpretatie van een jaartal bij verdwenen dorpen.
- Geen verplichting voor `Place` in de ruwe datasetpilots.

## 7. Nog te besluiten
- Wanneer is gemeente-identiteit juridisch versus geografisch?
- Hoe worden onzekerheid, meerdere verklaringen en betwiste equivalentie gemodelleerd?
- Wat is de formele semantiek van de tien legacy-hg-relaties?
- Welk beheerd vocabulaire gebruiken we voor relatietypen en temporalRole?
