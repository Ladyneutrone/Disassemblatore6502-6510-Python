
python Assemblator6502_6510ByOpcode.py [nome del file con gli opcode] [H o D] [Start]

## [nome del file con gli opcode]
devono essere separati dalla virgola
ad esempio :

120,30,16,10,45,189,56,123 decimali
A9,93,48,A9,41,A2,00,20,D2 esadecimali

## [H o D]
D Se i dati in ingresso sono decimali
H Se i dati in ingresso sono esadecimali

## [Start]
Indirizzo esadecimale di partenza del listato disassemblato

[Con opcode esadecimali]
python Assemblator6502_6510ByOpcode.py asm6510_IN.txt H 600A

[Con opcode decimali]
python Assemblator6502_6510ByOpcode.py asm6510_IN.txt D 6000

I listato sarà messo nel file listato.txt

