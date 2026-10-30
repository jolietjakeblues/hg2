# HG2 v0.6.0-draft: identiteit, historische toestanden en bronuitspraken

**Ontologie-IRI:** `https://linkeddata.cultureelerfgoed.nl/def/hg2`  
**Termnamespace:** `https://linkeddata.cultureelerfgoed.nl/def/hg2/`

Experimentele vervolgstap op v0.4. Er is **geen automatische omzetting** van bronrecord naar duurzame geografische identiteit. Bestaande data blijven TriG, ontologie en shapes blijven Turtle.

## Mappen

- `ontology/hg2.ttl`: HG2-ontologie (v0.5.0-draft), met bestaande eigenschappen en drie nieuwe verantwoordingsrelaties.
- `shapes/hg2-core.shacl.ttl`: kernvalidatie voor bronreferenties, uitspraken, historische toestanden en relaties.
- `shapes/verdwenendorpen.shacl.ttl`: datasetprofiel voor Verdwenen dorpen.
- `shapes/gemeentegeschiedenis.shacl.ttl`: datasetprofiel voor Gemeentegeschiedenis.
- `examples/*.trig`: bestaande v0.4-data onveranderd meegeleverd als testmateriaal.
- `scripts/convert_*.py`: bestaande conversiescripts, ongewijzigd.
- `scripts/check_datasets.py`: eenvoudige aanvullende kwaliteitscontroles.
- `docs/modelleerbeslissingen.md`: semantische beslissingen en vragen.

## Named graphs

- `https://linkeddata.cultureelerfgoed.nl/graph/verdwenendorpen`
- `https://linkeddata.cultureelerfgoed.nl/graph/gemeentegeschiedenis`

## Zelf testen

```powershell
cd C:\AI\hg2
python -m pip install rdflib pyshacl
python scripts/check_datasets.py
python -m pyshacl -s shapes/hg2-core.shacl.ttl -sf turtle -df trig -f human examples/verdwenendorpen-hg2-v0.4.trig
python -m pyshacl -s shapes/verdwenendorpen.shacl.ttl -sf turtle -df trig -f human examples/verdwenendorpen-hg2-v0.4.trig
python -m pyshacl -s shapes/hg2-core.shacl.ttl -sf turtle -df trig -f human examples/gemeentegeschiedenis-hg2-v0.4.trig
python -m pyshacl -s shapes/gemeentegeschiedenis.shacl.ttl -sf turtle -df trig -f human examples/gemeentegeschiedenis-hg2-v0.4.trig
```

Let op: sommige SHACL-tools behandelen TriG named graphs anders (union versus default graph). Bij problemen laad de gewenste named graph als aparte datagraph in de validator. De formele SHACL-validatie is nog niet daadwerkelijk uitgevoerd in deze omgeving, alleen parse- en programmatische controles.

## Beslissingen v0.5

1. Plaatsreferenties zijn geen vastgestelde plaatsen.
2. Brondata vormen geen automatisch bewijs van een historische toestand.
3. `identityEvidence`, `interpretationOf` en `relationEvidence` leggen menselijke interpretaties traceerbaar vast.
4. Dateringen worden pas geïnterpreteerd als hun betekenis is vastgesteld.
5. Historische relaties vergen onderbouwing en een gekozen relatietype.

## Geen migratie

De twee bestaande TriG-graphs worden in v0.5 niet vervangen. Het gaat eerst om het verbeteren van het model en de validator.

## Nieuw in v0.6
- `examples/rotterdam-identiteitstest.trig`: 17 echte bronreferenties en een toetsbare hypothese, geen identiteitsclaim.
- `tests/hypothetische-herindeling.trig`: expliciet verzonnen fusiescenario voor relaties.
- `shapes/hg2-interpretatie.shacl.ttl`: strenge aanvullende SHACL voor geïnterpreteerde toestanden en relaties.
- `docs/identiteitstest-v0.6.md`: aannames, open vragen en ontwerpkeuzes.

Belangrijk: bestaande productiedatasets zijn **niet** gewijzigd. Testgraphs niet zonder review publiceren.
