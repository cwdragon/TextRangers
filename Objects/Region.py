import json
import os
from Tile import Tile
class Region:
    
    id = None
    tiles = list()
    surroundingRegions = {"north" : None, "south" : None, "east" : None, "west" : None,
    "northEast" : None, "northWest" : None, "southEast" : None, "southWest" : None}

    def __init__(self, tiles, north, south, east, west, northEast, northWest, southEast, southWest):
        print "test"
        self.surroundingRegions["north"] = north
        self.surroundingRegions["south"] = south
        self.surroundingRegions["east"] = east
        self.surroundingRegions["west"] = west
        self.surroundingRegions["northEast"] = northEast
        self.surroundingRegions["northWest"] = northWest
        self.surroundingRegions["southEast"] = southEast
        self.surroundingRegions["southWest"] = southWest

    def readTiles(self, file):
        with open(file) as data_file:
                data = json.load(data_file)
        for value in data:
            self.tiles.append(Tile(value, data[value]["north"], data[value]["south"],
                                data[value]["east"], data[value]["west"], 
                                data[value]["northEast"], data[value]["northWest"], 
                                data[value]["southEast"], data[value]["southWest"], 
                                None, None, data[value]["description"], None, None))


