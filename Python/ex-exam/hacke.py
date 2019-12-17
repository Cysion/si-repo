"""
Hacke är student på BTH och har gått kursen DV1574. Han skrev väldigt mycket 
kommentarer i sin kod i början av kursen, men nu när han är mer varm i kläderna tycker han 
att kommentarerna är mest i vägen och vill ta bort dem. Han har producerat ganska många 
kodfiler under kursens gång, så det är ett tidsödande arbete. Därför bestämmer han sig för att 
skriva ett Python
-
script som tar hand om det hela "automatiskt". Han får dock inte 
programmet att fungera.
Hjälp Hacke att hitta felen! Vad ska han ändra för att
koden ska bli körbar
och göra det som 
var tänkt
? 
Förklara eller skriv om/komplettera hans kod, där du löser minst 2 brister
"""

def clean_line(line):
    for i in len(line):
        if line[i] == "#":
            return line[i:]
    return line

def remove_comments(in_filename, out_filename):
    in_handle = open(in_filename, 'r')
    out_handle = open(out_filename, 'w')
    for line in in_handle:
        out_handle.write(clean_line(line))