#!/usr/bin/env python3
"""Brongetrouwe pilot: geen identificatie, geodatering of relationele gevolgtrekking."""
import gzip, sys
from pathlib import Path
from rdflib import Dataset, Graph, Namespace, RDF, URIRef
HG2=Namespace('https://linkeddata.cultureelerfgoed.nl/def/hg2/')
DC=Namespace('http://purl.org/dc/elements/1.1/')
GEO=Namespace('http://www.opengis.net/ont/geosparql#')
PROV=Namespace('http://www.w3.org/ns/prov#')
BASE='https://linkeddata.cultureelerfgoed.nl/erfgeo/verdwenendorpen/id/'

def convert(src, out):
    ds=Dataset()
    with gzip.open(src,'rt',encoding='utf-8') as f: ds.parse(data=f.read(),format='trig')
    source=Graph()
    for s,p,o,g in ds.quads((None,None,None,None)): source.add((s,p,o))
    outg=Graph()
    for p,n in [('hg2',HG2),('dc',DC),('geo',GEO),('prov',PROV)]: outg.bind(p,n)
    records=sorted(set(source.subjects(DC.title,None)),key=str)
    for original in records:
        if not str(original).startswith(BASE):continue
        sid=str(original).removeprefix(BASE)
        ref=URIRef(BASE+'hg2-reference/'+sid)
        assertion=URIRef(BASE+'hg2-assertion/'+sid)
        outg.add((ref,RDF.type,HG2.PlaceReference))
        outg.add((ref,PROV.wasDerivedFrom,original))
        for triple in [
            (assertion,RDF.type,HG2.PlaceAssertion),
            (assertion,HG2.aboutPlaceReference,ref),
            (assertion,HG2.sourceRecord,original),
            (assertion,PROV.wasDerivedFrom,original)]:outg.add(triple)
        for p,new in [(DC.title,HG2.observedName),(DC.date,HG2.uninterpretedDate),
                      (DC.source,HG2.sourceDescription),(DC.subject,HG2.observedSubject)]:
            for value in source.objects(original,p):outg.add((assertion,new,value))
        for i,wkt in enumerate(source.objects(original,GEO.asWKT),1):
            geom=URIRef(str(assertion)+'/geometry/'+str(i))
            outg.add((geom,RDF.type,GEO.Geometry))
            outg.add((geom,GEO.asWKT,wkt))
            outg.add((assertion,HG2.observedGeometry,geom))
    outg.serialize(destination=out,format='turtle')
    print(f'{len(records)} bronrecords, {len(outg)} RDF-triples')
if __name__=='__main__':
    if len(sys.argv)!=3: raise SystemExit('Gebruik: python convert_verdwenendorpen.py bron.trig.gz uitvoer.ttl')
    convert(sys.argv[1],sys.argv[2])
