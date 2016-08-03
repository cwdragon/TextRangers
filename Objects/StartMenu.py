import sys
import os
from Player import Player
class StartMenu:

    def _init_(self):
        name = raw_input("Hello, what is your name")

    def checkExistingSave(self, name):
        saves = os.listdir("../Saves")
        if name + ".txt" in saves:
            with open(name + ".txt") as data_file:
                save = json.load(data_file)
            return save
        else:
            return playerCreation(name)

    def playerCreation(self, name):
        race = raw_input("Hello " + name + "it appears this is your first time playing, of what race are you")
        with open(name + ".txt") as data_file:
            raceData = json.load(data_file)[race]
