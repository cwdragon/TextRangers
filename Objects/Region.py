from Tile import Tile
class Region:
    
    id = None
    tiles = list()
    surroundingRegions = {"north" : None, "south" : None, "east" : None, "west" : None,
    "northEast" : None, "northWest" : None, "southEast" : None, "southWest" : None}

    def __init__(self, tiles, north, south, east, west, northEast, northWest, southEast, southWest)
        self.tiles = tiles
        self.surroundingRegions["northRegion"] = north;
        self.surroundingRegions["southRegion"] = south;
        self.surroundingRegions["eastRegion"] = east;
        self.surroundingRegions["westRegion"] = west;
        self.surroundingRegions["northEastRegion"] = northEast;
        self.surroundingRegions["northWestRegion"] = northWest;
        self.surroundingRegions["southWestRegion"] = southWest;
        self.surroundingRegions["southEastRegion"] = southEast;