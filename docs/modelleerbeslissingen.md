# Modelleerbeslissingen en open vragen (hg2 0.1.0-draft)

## Besloten als werkhypothese
1. `hg2:Place` = duurzame geografische identiteit, *niet* hetzelfde als een historische toestand of bronrecord.
2. `hg2:PlaceState` = afgebakende toestand. Een splitsing of herindeling vereist expliciete identiteitsregels; een gewijzigde geometrie is niet per definitie een nieuwe plaats.
3. `hg2:PlaceAssertion` = brongebonden bewering, met verwijzing naar bron of bronrecord; de waarheid ervan wordt niet aangenomen.
4. Onderscheid geldigheid van een verschijnsel (`validDuring`) en datering van de bron (`sourceDate`).
5. In deze versie *geen* `owl:sameAs` naar `hg:PlaceInTime`; de semantiek verschilt mogelijk.
6. Typen als `hg:Municipality` worden niet automatisch `owl:Class` in hg2. Gebruik voor classificatie bij voorkeur beheerde concepten.

## Nog niet besloten
- Is een juridisch bestuursorgaan een `Place`, een afzonderlijke organisatie, of een combinatie van beide?
- Wanneer zijn twee historische beschrijvingen dezelfde geografische entiteit?
- Hoe modelleren we concurrerende grensinterpretaties voor dezelfde periode: alternatieve toestanden of tegenstrijdige uitspraken over geometrie?
- Hoe duiden we een precies onbekende gebeurtenisdatum, bijvoorbeeld "verdwenen circa 1500"?
- Welke ontologie of vocabulaire definieert opvolging, splitsing, absorptie en bestuurlijke herindeling?
- Moet `PlaceAssertion` een uitspraakinhoud expliciet als afzonderlijke resource modelleren, of volstaat een gedocumenteerde verwijzing naar een toestand/relatie?
- Wie beheert URI's en koppelt bronrecords aan identiteiten?

## Niet doen
- `http://rdf.histograph.io/` en `https://rdf.histograph.io/` stilzwijgend gelijkstellen.
- Een PiT-record zonder bewijs omzetten naar een blijvende identiteit.
- Het bronjaar van een verdwenen dorp als bestaans-einddatum interpreteren zonder herkomstbewijs.
- Bestaande historische relaties gelijkstellen aan GeoSPARQL-topologie zonder semantisch bewijs.
