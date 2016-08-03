import json
import os
from Tile import Tile
class Region:
	
	id = None
	tiles = list()
	surroundingRegions = {"north" : None, "south" : None, "east" : None, "westRegiont" : None,
	"northEast" : None,	"northWest" : None,	"southEast" : None,	"southWest" : None}

	def __init__(self, tiles, north, south, east, west, northEast, northWest, southEast, southWest):
		print "test"
		self.tiles = tiles
		self.surroundingRegions["northRegion"] = north
		self.surroundingRegions["southRegion"] = south
		self.surroundingRegions["eastRegion"] = east
		self.surroundingRegions["westRegion"] = west
		self.surroundingRegions["northEastRegion"] = northEast
		self.surroundingRegions["northWestRegion"] = northWest
		self.surroundingRegions["southEastRegion"] = southEast
		self.surroundingRegions["southWestRegion"] = southWest

	def readTiles(self):
		with open('../Regions/Region1.json') as data_file:
    			data = json.load(data_file)
   		print data
test = Region(None, None, None,None,None,None,None,None,None)
test.readTiles()

