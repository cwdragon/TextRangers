from Race import Race
from Class import Class
class Player:

    name = None
    race = None
    gender = None
	playerClass = None
    stats = {"health" : None, "mana" : None, "armor" : None, "strength" : None, "dexterity" : None,
             "constitution" : None, "intelligence" : None, "wisdom" : None, "luck" : None}
    equipped = {"head": None,
                            "body": None,
                            "ringFingerLeft":None, 
                            "pinkyFingerLeft":None, 
                            "middleFingerLeft":None, 
                            "indexFingerLeft":None, 
                            "ringFingerRight":None, 
                            "pinkyFingerRight":None, 
                            "middleFingerRight":None, 
                            "indexFingerRight":None,
                            "legs":None,
                            "feet":None,
                            "gloves":None,
                            "arms":None,
                            "head":None,
                            "necklace": None}
    inventory = list()
    x = None
    y = None

    def _init_():
        return

    def JSONtoPlayer(self, data):
        
        return