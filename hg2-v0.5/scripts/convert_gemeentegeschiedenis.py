#!/usr/bin/env python3
"""Brongetrouwe HG2-v0.3 conversie. Geen samenvoeging, bestuursidentiteiten of herindelingen afleiden."""
import gzip,sys
from rdflib import Dataset,Graph,Namespace,URIRef,RDF
HG2=Namespace('https://linkeddata.cultureelerfgoed.nl/def/hg2/')
DC=Namespace('http://purl.org/dc/elements/1.1/')
SCHEMA=Namespace('http://schema.org/')
GEO=Namespace('http://www.opengis.net/ont/geosparql#')
PROV=Namespace('http://www.w3.org/ns/prov#')
OWMS=Namespace('http://standaarden.overheid.nl/owms/terms/')
BASE='https://linkeddata.cultureelerfgoed.nl/erfgeo/gemeentegeschiedenis/id/'
def convert(src,dest):
 ds=Dataset()
 with gzip.open(src,'rt',encoding='utf8') as f: ds.parse(data=f.read(),format='trig')
 g=Graph()
 for s,p,o,c in ds.quads((None,None,None,None)):g.add((s,p,o))
 result=Dataset()
 out=result.graph(URIRef('https://linkeddata.cultureelerfgoed.nl/graph/gemeentegeschiedenis'))
 for prefix,ns in [('hg2',HG2),('dc',DC),('schema',SCHEMA),('geo',GEO),('prov',PROV)]:out.bind(prefix,ns)
 recs=sorted(set(g.subjects(DC.title,None)),key=str)
 from rdflib.term import URIRef as IsURI
 for original in recs:
  sid=str(original).removeprefix(BASE)
  if not str(original).startswith(BASE):continue
  ref=URIRef(BASE+'hg2-reference/'+sid); a=URIRef(BASE+'hg2-assertion/'+sid)
  for t in [(ref,RDF.type,HG2.PlaceReference),(ref,PROV.wasDerivedFrom,original),(a,RDF.type,HG2.PlaceAssertion),(a,HG2.aboutPlaceReference,ref),(a,HG2.sourceRecord,original),(a,PROV.wasDerivedFrom,original)]:out.add(t)
  for prop,new in [(DC.title,HG2.observedName),(DC.identifier,HG2.observedIdentifier),(SCHEMA.startDate,HG2.observedStartDate),(SCHEMA.endDate,HG2.observedEndDate),(OWMS.CBSCode,HG2.observedCBSCode),(DC.URI,HG2.observedExternalReference)]:
   for v in g.objects(original,prop):out.add((a,new if prop!=DC.URI or isinstance(v,IsURI) else HG2.observedExternalReferenceLiteral,v))
  for i,wkt in enumerate(g.objects(original,GEO.asWKT),1):
   geom=URIRef(str(a)+'/geometry/'+str(i))
   for t in [(geom,RDF.type,GEO.Geometry),(geom,GEO.asWKT,wkt),(a,HG2.observedGeometry,geom)]:out.add(t)
 result.serialize(destination=dest,format='trig')
 print(f'{len(recs)} bronrecords, {len(out)} HG2-triples')
if __name__=='__main__':
 if len(sys.argv)!=3:raise SystemExit('Gebruik: python scripts/convert_gemeentegeschiedenis.py bron.trig.gz uitvoer.trig')
 convert(sys.argv[1],sys.argv[2])
