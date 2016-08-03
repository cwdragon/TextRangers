class Tile:
	
	id = None
	players = list()
	surroundingTiles {"north" : None, "south" : None, "east" : None, "west" : None,
	"northEast" : None, "northWest" : None,	"southEast" : None, "southWest" : None}
	event = None
	weather = None
	desc = None
	x = None
	y = None
	
	def __init__(self, id, north, south, east, west, northEast, northWest, southEast, southWest, desc, x, y)
		self.id = id
		self.surroundingTiles["northTile"] = north
		self.surroundingTiles["southTile"] = south
		self.surroundingTiles["eastTile"] = east
		self.surroundingTiles["westTile"] = west
		self.surroundingTiles["northEastTile"] = northEast
		self.surroundingTiles["northWestTile"] = northWest
		self.surroundingTiles["southEastTile"] = southEast
		self.surroundingTiles["northEastTile"] = northEast
		self.desc = desc
		self.x = x
		self.y = y
		
	def addPlayer(self, player)
		self.players.append(player)
		player.setTile(self)
		
	def removePlayer(self, player)
		self.players.remove(player)
		
	def movePlayer(self, player, direction)
		removePlayer(player)