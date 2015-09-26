import math, physics
import random
from mine import Mine
from vec import Vec

seeking = False
target = None
statuscount = 0

def discoverMines(player):
    global seeking
    global target

    if seeking and target and physics.distance(player.pos, target.location) < 1:
        self.mines.remove(target)
        seeking = False
        target = None

    #player.scan(random.random()* player.config.mapWidth, random.random() * player.config.mapHeight)
    player.scan(random.random() * player.config.mapWidth, random.random() * player.config.mapHeight)
    if not seeking and player.mines:
        target = closestMine(player)
        seeking = True
    player.status()
    if not seeking and not target and player.mines:
        target = closestMine(player)
        seeking = True
    if not target:
        return

    direc = physics.direction(player.pos, target.location)
    player.accel(math.atan2(direc.y, direc.x), 1) 

def closestMine(player):
    if not player.mines:
        return None

    minDist = float("inf")
    target = None
    for mine in player.mines:
        dist = physics.distance(player.pos, mine.location)
        if dist < minDist and not mine.controlled:
            minDist = dist
            target = mine
    return target

    print "Target to return is: "
    print target
    return target

def makeDecision(player):
    global statuscount 
    if (statuscount > 250 and not seeking):
        player.accel(random.random() * 6.28, 1)
        statuscount = 0
    discoverMines(player)
    statuscount = statuscount + 1

