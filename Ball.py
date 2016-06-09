__author__ = 'sh'

def abs(N):
    return N if N>=0 else -N

class Ball:
    x=0
    y=0
    xspeed=0.0
    yspeed=0.0
    allowphysics=True
    radius = 50

    def __init__(self,x,y,allowphysics=True):
        self.x=x
        self.y=y
        self.allowphysics=allowphysics

    def physics(self,yspeed=0.5,resistance=0.95):
        self.yspeed+=yspeed
        if abs(self.xspeed) <= 1:
            self.xspeed=0
        self.xspeed*=resistance


    def move(self,xspeed):
        self.xspeed+=xspeed

    def bounce(self,yspeed):
        self.yspeed=yspeed

    #움직임 수정
    def update(self):
        if self.allowphysics:
            self.physics()
        self.y+=self.yspeed
        self.x+=self.xspeed

    def setStatus(self,newx=False,newy=False,newxspeed=False,newyspeed=False):
        if(not isinstance(newx,bool)):
            self.x=newx
        if(not isinstance(newy,bool)):
            self.y=newy
        if(not isinstance(newxspeed,bool)):
            self.xspeed=newxspeed
        if(not isinstance(newyspeed,bool)):
            self.yspeed=newyspeed





