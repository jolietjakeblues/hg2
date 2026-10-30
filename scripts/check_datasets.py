#!/usr/bin/env python3
"""Lightweight deterministic checks, not a SHACL engine. Use pySHACL for formal validation."""
from pathlib import Path
from rdflib import Dataset, Namespace, RDF, URIRef
HG2=Namespace('https://linkeddata.cultureelerfgoed.nl/def/hg2/')
PROV=Namespace('http://www.w3.org/ns/prov#')
GEO=Namespace('http://www.opengis.net/ont/geosparql#')
ROOT=Path(__file__).resolve().parent.parent
for setname in ('verdwenendorpen','gemeentegeschiedenis'):
    file=next((ROOT/'examples').glob(f'{setname}-hg2-*.trig'))
    ds=Dataset();ds.parse(file,format='trig')
    graph=list(ds.contexts())
    expected=URIRef(f'https://linkeddata.cultureelerfgoed.nl/graph/{setname}')
    active=[g for g in graph if len(g)>0]
    assert len(active)==1 and active[0].identifier==expected, (setname,[g.identifier for g in active])
    g=active[0]
    refs=list(g.subjects(RDF.type,HG2.PlaceReference)); statements=list(g.subjects(RDF.type,HG2.PlaceAssertion))
    problems=[]
    for ref in refs:
        if not list(g.objects(ref,PROV.wasDerivedFrom)): problems.append(f'no provenance {ref}')
    for statement in statements:
        if not list(g.objects(statement,HG2.sourceRecord)):problems.append(f'no sourceRecord {statement}')
        if len(list(g.objects(statement,HG2.aboutPlaceReference)))!=1:problems.append(f'bad aboutPlaceReference {statement}')
        for geometry in g.objects(statement,HG2.observedGeometry):
            if (geometry,RDF.type,GEO.Geometry) not in g or not list(g.objects(geometry,GEO.asWKT)):
                problems.append(f'bad geometry {geometry}')
    print(f'{setname}: {len(g):,} triples, {len(refs)} references, {len(statements)} assertions, {len(problems)} errors')
    if problems:print('\n'.join(problems[:15])); raise SystemExit(1)
print('Basiscontroles geslaagd. Dit is geen formele SHACL-validatie.')
