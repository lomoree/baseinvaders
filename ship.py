from vec import Vec

'''
Class for general ships
'''
class Ship:

    def __init__(self, xPos, yPos, xVel=0.0, yVel=0.0, score=0):
        self.pos = Vec(xPos, yPos)
        self.vel = Vec(xVel, yVel)
        self.score = score
