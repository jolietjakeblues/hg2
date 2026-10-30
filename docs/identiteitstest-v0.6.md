# Identiteitstest v0.6

## Twee afzonderlijke testen

1. **Echte gegevens: Rotterdam**. Uit de aangeleverde dataset zijn 17 historische gemeenterecords met naam Rotterdam geselecteerd. Hun bronreferenties en uitspraken zijn ongewijzigd overgenomen in `examples/rotterdam-identiteitstest.trig`. Een `IdentityHypothesis` verbindt uitsluitend de kandidaat-referenties; er is **geen** `hg2:Place` of `hg2:PlaceState` afgeleid, en er is geen `owl:sameAs` geclaimd.
2. **Hypothetisch scenario**. `tests/hypothetische-herindeling.trig` bevat verzonnen plaatsen A, B en C en twee expliciete historische relaties. Dit is uitsluitend testdata, **geen bewijs** dat een concrete Nederlandse herindeling zo verliep.

## Semantische beslissingen
- Een naam (Rotterdam) is geen identiteitsbewijs.
- Een tijdreeks in gemeentegeschiedenis kan gemeentegrenzen beschrijven zonder dat we daarmee de juridische identiteit hebben vastgesteld.
- Een `HistoricalRelation` is een afzonderlijk object met brononderbouwing, geen impliciete regel dat voorganger en opvolger identiek zijn.
- De `IdentityHypothesis` is geen conclusie. Pas na externe juridische/historische onderbouwing koppelen we de referenties aan een `Place`.

## Open vragen
- Identificeert `Place` een geografisch gebied, een bestuurlijke organisatie of een bestuurlijk territorium? De huidige HG2-definitie kiest geografische entiteit; voor een juridische gemeente is mogelijk een aparte klasse nodig.
- Hoe onderscheiden we grenscorrectie, annexatie, fusie en naamswijziging zonder juridisch identiteitverlies?
- Welke bronnen (herindelingswetten, CBS-register, bronverantwoording) zijn gezaghebbend voor juridische continuïteit?

## Validatieprofielen
`shapes/hg2-interpretatie.shacl.ttl` is **strenger** dan de kernshapes: bij geïnterpreteerde toestanden en relaties is onderbouwing verplicht. Pas dit profiel niet blind toe op de brongetrouwe datasetconversies, die nog geen toestanden en relaties claimen.
