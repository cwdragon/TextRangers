from Player import Player
class Tile:

    id = None
    players = list()
    surroundingTiles = {"north" : None, "south" : None, "east" : None, "west" : None,
    "northEast" : None, "northWest" : None, "southEast" : None, "southWest" : None, "up" : None, "down" : None}
    event = None
    weather = None
    desc = None
    x = None
    y = None

    def __init__(self, id, north, south, east, west, northEast, northWest, southEast, southWest, up, down, desc, x, y):
        self.id = id
        self.surroundingTiles["north"] = north
        self.surroundingTiles["south"] = south
        self.surroundingTiles["east"] = east
        self.surroundingTiles["west"] = west
        self.surroundingTiles["northEast"] = northEast
        self.surroundingTiles["northWest"] = northWest
        self.surroundingTiles["southEast"] = southEast
        self.surroundingTiles["southWest"] = southWest
        self.surroundingTiles["up"] = up
        self.surroundingTiles["down"] = down
        self.desc = desc
        self.x = x
        self.y = y

    def addPlayer(self, player):
        self.players.append(player)
        player.setTile(self)

    def removePlayer(self, player):
        self.players.remove(player)

    def movePlayer(self, player, direction):
        removePlayer(player)
        tile = surroundingTiles[direction]
        tile.addPlayer(player)