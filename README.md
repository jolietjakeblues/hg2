# HG2 – stap 2: brongetrouwe waarnemingen (0.2.0-draft)

Deze repository is een **experimentele** doorontwikkeling van de hg2-starter en de pilot Verdwenen dorpen.

- Ontologie-IRI: `https://linkeddata.cultureelerfgoed.nl/def/hg2`
- Begrippen-namespace: `https://linkeddata.cultureelerfgoed.nl/def/hg2/` (slash, geen hash)
- `ontology/hg2.ttl`: bestaande starter met nieuwe waarnemings- en referentietermen
- `shapes/hg2.shacl.ttl`: aanvullende controles
- `scripts/convert_verdwenendorpen.py`: reproduceerbare conversie
- `examples/verdwenendorpen-hg2-v0.2.ttl`: de geconverteerde 562 records
- `docs/modelleerbeslissingen.md`: besluiten, onzekerheden en vervolgvragen

## Reproduceren

```powershell
python -m pip install rdflib
python scripts/convert_verdwenendorpen.py bron-verdwenendorpen.trig.gz examples/verdwenendorpen-hg2-v0.2.ttl
```

## Belangrijk

De 562 `PlaceReference`-objecten zijn **geen vastgestelde afzonderlijke plaatsen**. Gelijknamige plaatsen worden niet samengevoegd. Er zijn geen historische toestanden of gebeurtenissen afgeleid uit niet-geduide datums.

Dit is een verkenning, geen advies om een bestaande productieontologie te vervangen.
