# FA1: Betaalautomaat
Dit programma berekent bij een gegeven ingeworpen bedrag automatisch het wisselgeld, met zo min mogelijk munten. 
De output is vervolgens een lijst met alle munten zijn aantal dat teruggegeven moet worden. 

## Pseudocode
##### Vraag eerst de prijs van het gekozen product en de hoeveelheid van de inworp.
`input de prijs van het product`  
`input de hoeveelheid van de inworp`

##### Controleer of er wisselgeld uitgeworpen moet worden of dat er meer geld ingeworpen moet worden.
`if prijs groter dan inworp`  
`  zeg resterend bedrag is prijs - inworp`  
`elif prijs kleiner dan inworp`  
`  zeg u krijgt het volgende wisselgeld`  
`   x // 50 om aantal van een munt te berekenen`  
`   x = x % 50 om x het resterende aantal te maken`
`   x // 20`  
`   x = x % 20`  
`   etc...`  
`   of een for loop, for m in munten ([50, 20, 10, 5, 2, 1])`  
` else`  
`   zeg genoeg betaald`