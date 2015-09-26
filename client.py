#!/opt/bb/bin/python

import socket
import sys
from time import sleep    
from player import Player
import decisionmaker2 as engine
import physics

sock = None

def login(host, port, username, password):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, int(port)))
        sock.sendall(username+" "+password+"\n")
        return sock
    except socket.error as msg:
        print "Could not create socket: "+str(msg)

def run(command):
# print command
    try:
        sock.sendall(command+"\n")
        sfile = sock.makefile()
        ret = sfile.readline()
        print ret
        return ret
    except socket.error as msg:
        print "Could not run command '"+command+"': "+str(msg)

def brake():
    run("BRAKE")

def status():
    statusInfo = run("STATUS")

    print statusInfo

# angle is radians 
# magnitude is 0-1
def accel(angle, magnitude):
    cmd = "ACCELERATE %f %f" % (angle,magnitude)
    run(cmd)

def bomb(x, y, t=1):
    run("BOMB " + x + " " + y + " " + t)



def spiral():
    val = 0.0
    speed = 0.1
    inc = .05
    count =0
    while True:
        accel(val/10.0,speed)
        sleep(.5)
        val += 3.0
        count =count+1

        if count == 4:
            speed+= inc
            count=0

        if speed > 1:
            inc = -.05

        if speed < .1:
            inc =.05

if __name__ == "__main__":
    if (len(sys.argv) !=  5):
      print "Usage: "+sys.argv[0]+" <host> <port> <username> <pass>"
      sys.exit(1)

    host = sys.argv[1]
    port = sys.argv[2]
    username = sys.argv[3]
    password = sys.argv[4]
    sock = login(host, port, username, password)
    player = Player(username, sock, 0, 0)
    physics.setConfig(player.config)
    player.accel(0,1)
    cmd = raw_input("")
    #spiral()
    while(True):
        engine.makeDecision(player)
