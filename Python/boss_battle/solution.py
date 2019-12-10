from obj.fight import Fight



def main():
    fight = Fight()
    while fight.combatants["hero"].health > 0 and fight.combatants["hero"].health > 0:
        hero = fight.combatants["hero"]
        print("\nTurn ", fight.turn, "\nTake an action!")
        #YOUR CODE GOES HERE, UNLESS YOU WANT TO MESS WITH THE TURN ORDER!
        print("Active statuses are")
        for status in fight.statuses:
            print(f"{status[0]} takes {status[1]} damage for {status[2]+1} more turn(s)") 
        print("\nYour skills are!")
        for skill in hero.skills:
            if hero.cooldowns[skill] == 0:
                print("{:<15} dmg:{:<3} dot:{:<3} dur:{:<3} cld:{:<3}".format(skill,hero.skills[skill][0],hero.skills[skill][1],hero.skills[skill][2],hero.skills[skill][3]))
            else:
                print(f"{skill} on cooldown for {hero.cooldowns[skill]} turns!")
        done_action = False
        while not done_action :
            try:
                action = input("Enter name of action to take! ")
                target = input("To whom? ")
                print("")
                fight.take_turn("hero", action, target)
                done_action = True
            except KeyError:
                print("You cant do that!")
            
            except ValueError:
                print("Isn't that on cooldown?")


        #VILLAIN TURN AND SYSTEM
        fight.villain_turn()
        fight.end_turn()





if __name__ == "__main__":
    main()