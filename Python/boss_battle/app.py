from obj.fight import Fight



def main():
    fight = Fight()
    while fight.combatants["hero"].health > 0 and fight.combatants["hero"].health > 0:
        hero = fight.combatants["hero"]
        print("\nTurn ", fight.turn, "\nTake an action!")
        #YOUR CODE GOES HERE, UNLESS YOU WANT TO MESS WITH THE TURN ORDER!



        #VILLAIN TURN AND SYSTEM
        fight.villain_turn()
        fight.end_turn()





if __name__ == "__main__":
    main()