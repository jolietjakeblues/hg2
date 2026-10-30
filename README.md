# hg2: Histograph 2 (werkversie)

**Ontologie-IRI:** `https://linkeddata.cultureelerfgoed.nl/def/hg2`  
**Termnamespace:** `https://linkeddata.cultureelerfgoed.nl/def/hg2/`  
**Status:** 0.1.0-draft, geen productiepublicatie of formele vervanging van Histograph.

Een experimenteel, gegevensgericht model voor historische geografie: identiteit, toestanden, brongebonden uitspraken en historische relaties.

## Bestanden
- `ontology/hg2.ttl`: eerste OWL/RDFS-ontologie.
- `shapes/hg2.shacl.ttl`: eerste SHACL-regels, waarschuwingen waar informatie mogelijk ontbreekt.
- `examples/schematic-example.ttl`: synthetisch voorbeeld, nadrukkelijk geen echte ErfGeo-data.
- `docs/modelleerbeslissingen.md`: uitgangspunten, open vragen en valkuilen.

## Status en beperkingen
Dit is **geen** volledige conversie van ErfGeo/Histograph. Specifiek `hg:PlaceInTime` is semantisch nog niet bewezen gelijk aan `hg2:Place`, `hg2:PlaceState` of `hg2:PlaceAssertion`. Daarom zijn geen riskante equivalentierelaties toegevoegd.

Eerstvolgende stap: op echte ErfGeo-records (gemeentegeschiedenis, Kloekecodes en verdwenen dorpen) toetsen welke identiteit, toestand en broninformatie vaststaan en waar alleen onzekerheid bestaat. Daarna historische relatievocabulaire, migratiemapping en shape-regels aanscherpen.

## Terminologie
`PlaceAssertion` is voorlopig een generieke brongebonden bewering. De ontologie legt nog niet formeel vast *welke* propositie beweerd wordt. Dit is een expliciet ontwerpvraagstuk, geen afgeronde oplossing.
