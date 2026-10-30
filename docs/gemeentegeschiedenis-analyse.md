# Gemeentegeschiedenis: bevindingen en vragen

Bron: RCE-export (`trig.gz`), lokaal geanalyseerd.

- Bronrecords met dc:title: **4551**
- Unieke triples in bronexport: **29640**
- RDF-triples in nieuwe HG2-pilot: **53588**
- Aanwezige startDate-waarden: **3407**
- Aanwezige endDate-waarden: **3709**
- Geometrieën: **2873**
- CBS-codes: **1445**
- URI-verwijzingen: **1670**

## Wat het bronmateriaal nog niet rechtvaardigt
1. Gelijke gemeentenamen betekenen niet automatisch dezelfde gemeentelijke identiteit.
2. Jaartallen uit het bronrecord zijn niet zonder meer de bestaansduur van één blijvende bestuursorganisatie.
3. Een polygon kan een historische begrenzing zijn, maar ook een reconstructie met eigen broncontext.
4. De export bevat geen expliciete `hg:absorbedBy`/`hg:originatedFrom`-relaties.
5. `http://rdf.histograph.io/PlaceInTime` en `https://rdf.histograph.io/PlaceInTime` zijn verschillende URI's.

## Ontwerpbesluiten (voorlopig)
- We modelleren één bronrecord als één `PlaceReference` en één `PlaceAssertion`.
- We bewaren alle oorspronkelijke RDF in de bijgeleverde bronexport.
- Start-/einddatums blijven bronwaarnemingen, zonder nieuwe `time:Interval`-interpretatie.
- Geen `hg2:PlaceState` aanmaken voordat duidelijk is wat het record temporeel afbakent.
- Ontologie is vooralsnog een extra laag, geen semantische gelijkstelling met oude hg-URI's.

## Volgende test
Selecteer de opvolging van **Brielle, Hellevoetsluis en Westvoorne naar Voorne aan Zee** en vergelijk met een geval van grenswijziging waarbij de gemeente-identiteit mogelijk blijft bestaan. Hiervoor kunnen officiële herindelingsgegevens en bronrelaties nodig zijn.
