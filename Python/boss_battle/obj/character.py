import json

class Character:
    def __init__(self, template):
        with open(template) as infile:
            loaded_template = json.load(infile)
        self.name = loaded_template["name"]
        self.health = loaded_template["health"]
        self.taunts = loaded_template["taunts"]
        self.skills = loaded_template["skills"]
        self.cooldowns = {}
        for skill in self.skills:
            self.cooldowns[skill] = 0
    
