from RacialAbility import RacialAbility
class Race:

    name = None
    desc = None
    strength = None
    dexterity = None
    constitution = None
    intelligence = None
    wisdom = None
    luck = None
    passiveAbilities = list()

    def __init__(self, name, desc, strength, dexterity, constitution, intelligence, wisdom, luck):
        self.name = name
        self.desc = desc
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.luck = luck
    #racial abilities will be added after Race initialization

    def readRaces(self):
        with open('../Races/PlayerRaces.json') as data_file:
                data = json.load(data_file)
        print data