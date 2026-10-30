# Besluiten en open vragen (0.2.0-draft)

## Voorlopige besluiten
1. `hg2:Place` vertegenwoordigt een vastgestelde geografische identiteit, niet automatisch een bronrecord.
2. `hg2:PlaceReference` is een brongebonden, **voorlopige** referentie en mag zonder identiteitsonderzoek niet gelijkgesteld worden aan `hg2:Place`.
3. `hg2:PlaceAssertion` bewaart bronwaarnemingen met expliciete eigenschappen. Dit is **nog geen algemeen propositiemodel**.
4. `dc:date` uit Verdwenen dorpen wordt `hg2:uninterpretedDate` en **niet** `hg2:validDuring` of `hg2:sourceDate`.
5. WKT uit de bron wordt een afzonderlijke `geo:Geometry`, gekoppeld via `hg2:observedGeometry` aan de bronuitspraak; niet rechtstreeks aan een duurzame plaats.
6. Identieke namen zoals Westkerke geven geen bewijs voor identiteit.

## Nog te onderzoeken
- Wat dateert `dc:date` inhoudelijk? Verdwijning, bronvermelding, andere gebeurtenis?
- Beschrijven de punten een historische locatie, een schatting, of een moderne referentiepositie?
- Hoe representeren we een inhoudelijke propositie (predicaat, object) en broninterpretatie zonder nodeloze reificatie?
- Wat is een plaats bij verplaatsing, naamswijziging, bestuurlijke fusie of fysieke vernietiging?
- Wanneer en door wie wordt een `PlaceReference` gekoppeld aan een vastgestelde `Place`?
- Is een afzonderlijke `PlaceState` in alle toepassingen nodig, of alleen waar expliciete toestandverschillen zijn?

## Migratie
Bestaande 0.1 pilots creëerden recordgebaseerde `hg2:Place`-URI’s. Deze zijn **niet zomaar** in echte identiteiten te migreren. In 0.2 worden daarom nieuwe, duidelijke `hg2-reference/`-URI's gebruikt; oude proef-URI's blijven experimenteel.

## Technische controle
OWL-ontologie en RDF-output zijn syntactisch geparseerd met RDFLib. SHACL-shapes zijn syntactisch geparseerd; er is **geen volledige SHACL-validatie** uitgevoerd.
