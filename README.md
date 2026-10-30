# HG2 v0.4: TriG-conventie

**Data worden uitsluitend als TriG (`.trig`) gepubliceerd.** De ontologie blijft Turtle (`ontology/hg2.ttl`). SHACL-shapes blijven Turtle (`shapes/hg2.shacl.ttl`), omdat ze een schema zijn, geen dataset.

Elk HG2-databestand heeft exact één named graph, met de bronset als naam:

- `https://linkeddata.cultureelerfgoed.nl/graph/verdwenendorpen`
- `https://linkeddata.cultureelerfgoed.nl/graph/gemeentegeschiedenis`

De HG2-conversies vormen een **alternatieve representatie** van de bronset. Laad bronexport en HG2-conversie **niet tegelijk in dezelfde graph** zonder expliciet vervangingsbeleid. Er worden nog geen duurzame plaatsidentiteiten of historische opvolgingen afgeleid.

Uitvoer:

- `examples/verdwenendorpen-hg2-v0.4.trig`
- `examples/gemeentegeschiedenis-hg2-v0.4.trig`

Herhalen (vanuit de projectmap):

```powershell
python scripts/convert_verdwenendorpen.py bron-verdwenendorpen.trig.gz examples/verdwenendorpen-hg2-v0.4.trig
python scripts/convert_gemeentegeschiedenis.py bron-gemeentegeschiedenis.trig.gz examples/gemeentegeschiedenis-hg2-v0.4.trig
```

De scripts lezen een `.trig.gz` en schrijven `.trig`; het oorspronkelijke named graph-label wordt gebruikt.

---

# HG2 v0.3-draft – gemeentegeschiedenis-pilot

**Ontologie:** `https://linkeddata.cultureelerfgoed.nl/def/hg2`  
**Prefix:** `https://linkeddata.cultureelerfgoed.nl/def/hg2/`  
**Status:** experimentele aanvulling op v0.2, geen productiemigratie.

Deze pilot bewaart de informatie uit **4.551 gemeenterecords** als 4.551 `PlaceReference`-objecten en 4.551 `PlaceAssertion`-objecten. De originele export is ook meegeleverd zodat de conversie controleerbaar blijft.

De datums `schema:startDate` en `schema:endDate` komen terecht in `hg2:observedStartDate` en `hg2:observedEndDate`. We nemen **niet** aan dat dit het ontstaan en einde van een duurzame gemeente-identiteit is. Een ontbrekende datum krijgt geen fictieve waarde.

Er worden geen `hg2:Place`, `hg2:PlaceState` of `hg2:HistoricalRelation` verzonnen. Ook identieke namen of CBS-codes leiden niet automatisch tot fusie van records. Een `dc:URI` wordt niet automatisch `owl:sameAs`.

## Inhoud
- `ontology/hg2.ttl`: ontologie v0.3 (toevoegingen voor bronwaarnemingen)
- `shapes/hg2.shacl.ttl`: SHACL inclusief test gemeenterecords
- `scripts/convert_gemeentegeschiedenis.py`: reproduceerbare conversie
- `examples/gemeentegeschiedenis-hg2-v0.3.ttl`: volledige proefconversie
- `examples/source-gemeentegeschiedenis.trig.gz`: onaangetaste oorspronkelijke export
- `docs/gemeentegeschiedenis-analyse.md`: overzicht en volgende modelleervragen

## Zelf draaien
```powershell
pip install rdflib pyshacl
python scripts/convert_gemeentegeschiedenis.py examples/source-gemeentegeschiedenis.trig.gz examples/gemeentegeschiedenis-hg2-v0.3.ttl
pyshacl -s shapes/hg2.shacl.ttl -e ontology/hg2.ttl examples/gemeentegeschiedenis-hg2-v0.3.ttl
```

Bewust niet de eindconclusie: pas wanneer we herindelingen of een juridisch doorlopende gemeente-identiteit kunnen onderbouwen, modelleren we `PlaceState` en `HistoricalRelation`.
