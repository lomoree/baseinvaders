import math
from vec import Vec
import config


MAX_X = 0 # NEED TO CHANGE TO CONFIG
MAX_Y = 0

def getAcceleration(source, dest, player):
    vector = direction(source, dest)
    velvec = player.vel
    res = Vec(vector.x - velvec.x, vector.y - velvec.y)

    d = distance(source, dest)
    acc = 0.8
    if d < 1500:
        acc = 0.5
    return (res, acc)

def setConfig(config):
    global MAX_X
    global MAX_Y
    MAX_X = config.mapWidth
    MAX_Y = config.mapHeight

def direction(source, dest):
    eucDist = _eucDist(source, dest)
    transDist = _transDist(source, dest)
    magnitude = None
    useEucDist = None

    if eucDist <= transDist:
        magnitude = eucDist
        useEucDist = True
    else:
        magnitude = transDist
        useEucDist = False


    if source.x <= dest.x:
        if source.y <= dest.y:
            if useEucDist:
                return Vec((dest.x - source.x), (dest.y - source.y))
            else:
                newSource = Vec(source.x + MAX_X, source.y + MAX_Y)
                return Vec((dest.x - newSource.x), (dest.y - newSource.y))
        else:
            if useEucDist:
                return Vec((dest.x - source.x), (dest.y - source.y))
            else:
                newSource = Vec(source.x + MAX_X, source.y - MAX_Y)
                return Vec((dest.x - newSource.x), (dest.y - newSource.y))
    else:
        if source.y <= dest.y:
            if useEucDist:
                return Vec((dest.x - source.x), (dest.y - source.y))
            else:
                newSource = Vec(source.x - MAX_X, source.y + MAX_Y)
                return Vec((dest.x - newSource.x), (dest.y - newSource.y))
        else:
            if useEucDist:
                return Vec((dest.x - source.x), (dest.y - source.y))
            else:
                newSource = Vec(source.x - MAX_X, source.y - MAX_Y)
                return Vec((dest.x - newSource.x), (dest.y - newSource.y))
    


def distance(source, dest):
    return _eucDist(source, dest)
    #return min(_eucDist(source, dest), _transDist(source, dest))

def _eucDist(source, dest):
    return math.sqrt((source.x - dest.x)**2 + (source.y - dest.y)**2)

def _transDist(source, dest):
    if source.x <= dest.x:
        if source.y <= dest.y:
            return _eucDist(dest, Vec(source.x + MAX_X, source.y + MAX_Y))
        else:
            return _eucDist(dest, Vec(source.x + MAX_X, source.y - MAX_Y))
    else:
        if source.y <= dest.y:
            return _eucDist(dest, Vec(source.x - MAX_X, source.y + MAX_Y))
        else:
            return _eucDist(dest, Vec(source.x - MAX_X, source.y - MAX_Y))
