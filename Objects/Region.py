class Region:
	
	id = None
	tiles = list()
	surroundingRegions = {"north" : None, "south" : None, "east" : None, "west" : None
	"northEast" : None,	"northWest" : None,	"southEast" : None,	"southWest" : None}
	
	def __init__(self, tiles, north, south, east, west, northEast, northWest, southEast, southWest)
		self.tiles = tiles
		self.regions["northRegion"] = north;
		self.regions["southRegion"] = south;
		self.regions["eastRegion"] = east;
		self.regions["westRegion"] = west;
		self.regions["northEastRegion"] = northEast;
		self.regions["northWestRegion"] = northWest;
		self.regions["southEastRegion"] = southEast;
		self.regions["southWestRegion"] = southWest;