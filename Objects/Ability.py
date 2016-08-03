class Ability:

    name = None
    desc = None
    levelRequirement = None
    affectedAttributes = None
    percentageModifier = None
    healing = None

    def __init__(self, name, desc, levelRequirement, affectedAttributes, percentageModifier, healing):
        self.name = name
        self.desc = desc
        self.levelRequirement = levelRequirement
        self.affectedAttributes = affectedAttributes
        self.percentageModifier = percentageModifier
        self.healing = healing
        
    def readTiles(self):
        with open('../Races/PlayerRaces.json') as data_file:
                data = json.load(data_file)
        print data
