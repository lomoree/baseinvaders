class Config:

    def __init__(self, configStr):
        conflist = configStr.split(" ")[::2][1:]
        self.mapWidth = int(conflist[0])
        self.mapHeight = int(conflist[1])
        self.captureRadius = conflist[2]
        self.visionRadius = conflist[3]
        self.friction = conflist[4]
        self.brakeFriction = conflist[5]
        self.bombplRadius = conflist[6]
        self.bombeffectRadius = conflist[7]
        self.bombDelay = conflist[8]
        self.bombPower = conflist[9]
        self.scanRadius = conflist[10]
        self.scanDelay = conflist[11]
