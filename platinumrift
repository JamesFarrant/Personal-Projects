# =======================================================================================
# Framework (only) by Alastair
# AI code by swooce
# =======================================================================================

import sys, math
import random


AMERICA = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
MAINLAND = [50, 51, 52, 53, 54, 55, 56, 58, 59, 60, 61, 62, 63, 64, 65, 66, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 90, 91, 92, 93, 94, 95, 96, 98, 99, 100, 101, 102, 103, 105, 106, 107, 108, 109, 110, 111, 112, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 144, 145, 146, 147, 148, 151, 152, 153]
SOUTH_POLE = [57, 67, 78, 89, 97, 104, 113]
JAPAN = [143, 149, 150]


# =======================================================================================
# FUNCTIONS
# =======================================================================================

class Tile:
    id = -1
    owner = -1
    p0 = 0
    p1 = 0
    p2 = 0
    p3 = 0

    platinum = 0

    def __init__(self):
        self.adjacents = []

    def units(self, player):
        if player == 0:
            return self.p0
        if player == 1:
            return self.p1
        if player == 2:
            return self.p2
        if player == 3:
            return self.p3
        return 0

    def enemies(self, player):
        return self.p0+self.p1+self.p2+self.p3 - self.units(player)

    def owns(self, player):
        return self.owner == player

    def is_neutral(self):
        return self.owner == -1

    def get_adjacents(self):
        return self.adjacents


class Instruction:
    moves = ""
    buys = ""

    def buy(self, number, tile):
        self.buys += str(number) + " " + str(tile) + " "

    def move(self, number, start, end):
        self.moves += str(number) + " " + str(start) + " " + str(end) + " "


def get_tile(id):
    return tiles[id]

tiles = []

# =======================================================================================
# READ IN DATA (leave this)
# =======================================================================================

playerCount, myID, zoneCount, linkCount = [int(i) for i in input().split()]

for i in range(zoneCount):
    tiles.append(0)

for i in range(zoneCount):
    # zoneId: this zone's ID (between 0 and zoneCount-1)
    # platinumSource: the amount of Platinum this zone can provide per game turn
    zoneId, platinumSource = [int(i) for i in input().split()]

    tile = Tile()
    tile.id = zoneId
    tile.platinum = platinumSource

    tiles[zoneId] = tile

for i in range(linkCount):
    zone1, zone2 = [int(i) for i in input().split()]
    get_tile(zone1).adjacents.append(zone2)
    get_tile(zone2).adjacents.append(zone1)

# =======================================================================================
# PLAN STUFF OUT
# =======================================================================================


# =======================================================================================
# GAME LOOP
# =======================================================================================
while 1:
    # ===================================================================================
    # Update game state (leave this)
    # ===================================================================================
    platinum = int(input())
    for i in range(zoneCount):
        zId, ownerId, podsP0, podsP1, podsP2, podsP3 = [int(i) for i in input().split()]

        tile = get_tile(zId)
        tile.owner = ownerId
        tile.p0 = podsP0
        tile.p1 = podsP1
        tile.p2 = podsP2
        tile.p3 = podsP3

    # ===================================================================================
    # Work stuff out
    # ===================================================================================

    # first we work out some useful things

    friendly_unit_tiles = [t for t in tiles if t.units(myID) > 0]
    enemy_unit_tiles = [t for t in tiles if t.enemies(myID) > 0]

    friendly_tiles = [t for t in tiles if t.owner == myID]
    neutral_tiles = [t for t in tiles if t.owner == -1]
    enemy_tiles = [t for t in tiles if (t.owner != -1 and t.owner != myID)]

    platinum_tiles = [t for t in tiles if t.platinum > 0 in MAINLAND]

    max_purchases = math.floor(platinum / 20)

    # ===================================================================================
    # leave this
    instructions = Instruction()
    # ===================================================================================
    # Do movements
    # ===================================================================================
    for my_tile in friendly_unit_tiles:
        non_friendly = [get_tile(tile) for tile in my_tile.get_adjacents() if get_tile(tile).owner != myID]
        friendly = [get_tile(tile) for tile in my_tile.get_adjacents() if get_tile(tile).owner == myID]

        if len(platinum_tiles) > 0:
            instructions.move(1, my_tile.id, random.choice(platinum_tiles))
        elif len(non_friendly) > 0:
            instructions.move(1, my_tile.id, random.choice(non_friendly).id)
        elif len(friendly_tiles) > 0:
            instructions.move(1, my_tile.id, random.choice(friendly).id)

        for purchase in range(max_purchases):
            # buy a random neutral tile
            south_pole_neutral_or_enemy = [t for t in SOUTH_POLE if get_tile(t).owner != myID]

            spawnable_targets_south_pole = [t for t in SOUTH_POLE if get_tile(t).owner == -1 or get_tile(t).owner == myID]

            mainland_attack = [t for t in MAINLAND if get_tile(t).owner != myID]

            mainland_spawns = [t for t in MAINLAND if get_tile(t).owner == -1 or get_tile(t).owner == myID]

            if len(south_pole_neutral_or_enemy) > 0 and len(spawnable_targets_south_pole) > 0:
                instructions.buy(1, random.choice(spawnable_targets_south_pole))
            if len(mainland_attack) > 0 and len(mainland_spawns) > 0:
                instructions.buy(1, random.choice(mainland_spawns))

    if instructions.moves == "":
        print("WAIT")
    else:
        print(instructions.moves)
        print(instructions.buys)



def blur(tiles, initial, step):
    values = {}
    next_lowest = {}
    for k in initial:
        values[k] = initial[k]

    steps = 0
    while(steps < 20):
        steps += 1
        unresolved = 0

        for tile in tiles:
            neighbour_values = [values[adj] for adj in tile.get_adjacents() if (adj in values)]
            if(len(neighbour_values) > 0):
                min_val = min(neighbour_values)
                if(not tile.id in values or step(min_val) < values[tile.id]):
                    unresolved += 1
                    values[tile.id] = step(min_val)
        if(unresolved == 0):
            steps = 9999

    for tile in tiles:
        if(not tile.id in values) :
            values[tile.id] = 9999

    for tile in tiles:
        next_lowest[tile.id] = min(tile.get_adjacents() + [tile.id], key = lambda t: values[t] if t in values else 9999)

    return (values, next_lowest)









    # ===================================================================================
    # Do buying
    # ===================================================================================


    # ===================================================================================
    # leave this

    # ===================================================================================
