class PassiveAbility:

    name = None
    desc = None
    affectedAttributes = list()
    percentageModifier = None
    raceRestrictions = None
    classRestrictions = list()

    def __init__(self, name, desc, affectedAttributes, percentageModifier, raceRestrictions, classRestrictions):
        self.name = name
        self.desc = desc
        self.affectedAttributes = affectedAttributes
        self.percentageModifier = percentageModifier
        self.raceRestrictions = raceRestrictions
        self.classRestrictions = classRestrictions