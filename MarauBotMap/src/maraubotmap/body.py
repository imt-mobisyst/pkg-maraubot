import math

class Body:
    def __init__(self, posx, posy, theta, radius):
        self.x= posx
        self.y= posy
        self.theta= theta
        self.radius= radius
        self.speed= 0.0
        self.drift= 0.0
        self.rotate= 0.0
    
    def process(self, epsilon=0.01):
        c= math.cos( self.theta )
        s= math.sin( self.theta )
        self.theta+= self.rotate*epsilon
        self.x+= c*self.speed*epsilon
        self.y+= s*self.speed*epsilon
        self.x+= s*self.drift*epsilon
        self.y+= -c*self.drift*epsilon
