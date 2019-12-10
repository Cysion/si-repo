from obj.character import Character
import random
class Fight:
    def __init__(self):
        self.turn = 1
        self.combatants = {
            "hero":Character("data/hero.json"),
            "villain":Character("data/villain.json")
        }
        #indexing for statuses are [target, damage, turns remaining]
        self.statuses = []
        self.excaimations = ["shouts", "taunts", "screams", "boldly states", "sings in D minor"]

    def take_turn(self, char, action, target):
        skill = self.combatants[char].skills[action]
        if self.combatants[char].cooldowns[action] != 0:
            raise ValueError
        self.combatants[target].health -= skill[0]
        self.combatants[char].cooldowns[action] = skill[3]
        print(target, " takes ", skill[0], " damage from ", action)
        if skill[2] != 0:
            self.statuses.append([target, skill[1], skill[2]])
        print(f"{random.choice(self.combatants[char].taunts)} the {char} {random.choice(self.excaimations)}")
        
        
    
    def apply_statuses(self):
        for status in self.statuses:
            self.combatants[status[0]].health -= status[1]
            if status[2] == 0:
                self.statuses.remove(status)
            else:
                status[2] -= 1
    
    def end_turn(self):
        self.apply_statuses()
        self.turn += 1
        for combatant in self.combatants:
            for cd in self.combatants[combatant].cooldowns:
                if self.combatants[combatant].cooldowns[cd]:
                    self.combatants[combatant].cooldowns[cd] -= 1
            print(combatant, " has ", self.combatants[combatant].health, " hp")
        
        

    def villain_turn(self):
        try:
            if self.turn % 2 == 0:
                self.take_turn("villain", "flaming water breath", "hero")
            elif self.turn % 3 == 0:
                self.take_turn("villain", "head barrage", "hero")
            elif self.turn % 5 == 0:
                self.take_turn("villain", "angry glare", "hero")
            else:
                self.take_turn("villain", "balanced bite", "hero")
        except ValueError:
            print("due to the game being confused the villain attacks itself!")
            self.take_turn("villain", "balanced bite", "villain")

