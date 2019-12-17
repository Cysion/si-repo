"""
I den här uppgiften ska du skriva tre olika funktioner.
En hjälpfunktion som heter add() ska skrivas. Den ska addera de
två argument som skickas in i funktionen och returnera summan 
av dem. Argumenten är antingen tal eller strängen ’infinity’. 
Om något av argumenten är ’infinity’ så ska även den returnerade 
summan vara ’infinity’. I annat fall ska den matematiska summan 
returneras.
exempelvis:
add(2, 3) -> 5
add(2, 'infinity') -> 'infinity'
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Med hjälp av hjälpfunktionen add() ska funktioner som adderar alla element 
i en inskickad lista implementeras. Listan kan enbart bestå av tal och
’infinity’ som element. Listsummeringsfunktioner ska implementeras i två 
versioner:
    en iterativ variant, add_list_iter()
    en rekursiv variant, add_list_rec()
Summeringen i funktionerna ska ske med hjälp av din hjälpfunktion add()
exempelvis:
add_list_iter([1, 2, 3, 4]) -> 10
add_list_iter([1, 2, 'infinity', 4]) -> 'infinity'
och samma resultat förväntas för samma input till add_list_rec()
"""