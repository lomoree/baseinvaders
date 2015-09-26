from ship import Ship
from vec import Vec
from config import Config
from mine import Mine
import socket

import re

'''
Special case of ship
'''
class Player(Ship):

    def __init__(self, name, sock, xPos, yPos, xVel=0.0, yVel=0.0, score=0):
        Ship.__init__(self, xPos, yPos, xVel, yVel, score)
        self.name = name
        self.sock = sock
        self.config = self._get_config()
        self.placedBomb = False
        self.mines = set()
        self.ships = []
        self.bombs = []

    def _run(self, command):
        # print command
        sock = self.sock
        try:
            sock.sendall(command+"\n")
            sfile = sock.makefile()
            ret = sfile.readline()
            print ret
            return ret
        except socket.error as msg:
            print "Could not run command '"+command+"': "+str(msg)

    def _get_config(self):
        return Config(self._run("CONFIGURATIONS"))

    def _parse_status_str(self,status, scan=False):
        player = re.search("STATUS_OUT (.+) MINES", status).group(1).strip().split(" ")
        xPos,yPos,dx,dy = map(float, player)
        self.pos = Vec(xPos, yPos)
        self.vel = Vec(dx, dy)
        
        mines = re.search("MINES (.+) PLAYERS", status).group(1).strip().split(" ")
        mines = zip(*[mines[1:][i::3] for i in range(3)])
        self.mines.update([Mine(Vec(float(mine[1]), float(mine[2])), mine[0] == self.name) for mine in mines])
        

        ships = re.search("PLAYERS (.+) BOMBS", status).group(1).strip().split(" ")
        ships = zip(*[map(float, ships[1:][i::4]) for i in range(4)]) # fyi this is in place. shrekt.
        self.ships = []
        for ship in ships:
            self.ships.append(Ship(ship[0], ship[1], ship[2], ship[3]))

        bombs = re.search("BOMBS (.+)", status).group(1).strip().split(" ")
        self.bombs = zip(*[bombs[1:][i::2] for i in range(2)])

        print "Player: pos(%f,%f) vel(%f,%f)" % (self.pos.x, self.pos.y, self.vel.x, self.vel.y)
        print "Mines: "
        print self.mines
        print "Ships: "
        print self.ships
        print "Bombs: "
        print self.bombs

    def _parse_scan_str(self, status):
        if "ERROR" in status:
            return
        mines = re.search("MINES (.+) PLAYERS", status).group(1).strip().split(" ")
        mines = zip(*[mines[1:][i::3] for i in range(3)])
        self.mines.update([Mine(Vec(float(mine[1]), float(mine[2])), mine[0] == self.name) for mine in mines])
        
        ships = re.search("PLAYERS (.+) BOMBS", status).group(1).strip().split(" ")
        ships = zip(*[map(float, ships[1:][i::4]) for i in range(4)]) # fyi this is in place. shrekt.
        self.ships = []
        for ship in ships:
            self.ships.append(Ship(ship[0], ship[1], ship[2], ship[3]))

        bombs = re.search("BOMBS (.+)", status).group(1).strip().split(" ")
        self.bombs = zip(*[map(float, bombs[1:][i::2]) for i in range(2)])

    def brake(self):
       self._run("BRAKE")

    def accel(self, direction, power):
        self._run("ACCELERATE %f %f" % (direction, power))

    def status(self):
        status = self._run("STATUS")
        self._parse_status_str(status)

    def bomb(self, x, y):
        self._run("BOMB %f %f" % (x, y))

    def bomb(self, x, y, time):
        self._run("BOMB %f %f %d" % (x, y, time))

    def scan(self, x, y):
        scanStatus = self._run("SCAN %f %f" % (x, y))
        self._parse_scan_str(scanStatus)

    # TODO or who cares lol
    def scoreboard(self):
        return
