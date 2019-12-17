"""
Ett så kallat Caesar-chiffer är en enkel typ av kryptering som skiftar karaktärer
i en sträng ett fixt antal steg i alfabetet. Utforma en funktion caesar_cipher() 
som tar ett tal och ett ord som indata och som använder en global sträng med 
alfabetet. Funktionen ska returnera en krypterad sträng enligt exemplet. Alla 
koder består av endast stora bokstäver oavsett om klartextordet har stora eller 
små bokstäver. För att omvandla små bokstäver till stora kan strängmetoden upper() 
användas.

referenssträngen kan se ut så här:
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVXYZ"

testfall# | input | output |
    1     |   2   | JGNNQ  |
          | hello |        |
----------------------------
    2     |   3   |   ABC  |
          |   xyz |        |
"""