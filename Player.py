class Player:
    def __init__(self, name, health, strength, defense, dexterity):
        self.name = name
        self.health = health
        self.strength = strength
        self.defense = defense
        self.dexterity = dexterity

    def __str__(self):
        return f"{self.name}, {self.strength}, {self.health}, {self.defense}, {self.dexterity}"
    
    def print_stats(self):
        print(f"Health: {self.health}\nStrength: {self.strength}\nDefense: {self.defense}\nDexterity: {self.dexterity}")

    def stat_upgrade(self, stat, value):
        if stat == "health": self.health += value
        if stat == "strength": self.strength += value 
        if stat == "defense": self.defense += value
        if stat == "dexterity": self.dexterity += value
        return ""

