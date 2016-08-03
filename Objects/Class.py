from Ability import Ability
class Class:

    name = None
    desc = None
    raceRestrictions = None
    abilities = list()
    passiveAbilities = list()

    def __init__(self, name, desc, raceRestrictions, abilities):
        self.name = name
        self.desc = desc
        self.raceRestrictions = raceRestrictions

    #abilities will be loaded after class initialization
