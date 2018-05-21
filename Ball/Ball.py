__author__ = 'sh'

class Ball:
    x=0
    y=0
    xspeed=0.0
    yspeed=0.0
    allowphysics=True
    radius = 50
    bouncSpeed = - 25

    def __init__(self,x,y,allowphysics=True):
        self.x=x
        self.y=y
        self.allowphysics=allowphysics

    def physics(self,yspeed=0.7,resistance=0.95):
        self.yspeed+=yspeed
        if abs(self.xspeed) <= 1:
            self.xspeed=0
        self.xspeed*=resistance


    def move(self,xspeed):
        self.xspeed+=xspeed

    def bounce(self):
        self.yspeed=self.bouncSpeed

    def setStatus(self,newx=False,newy=False,newxspeed=False,newyspeed=False):
        if(not isinstance(newx,bool)):
            self.x=newx
        if(not isinstance(newy,bool)):
            self.y=newy
        if(not isinstance(newxspeed,bool)):
            self.xspeed=newxspeed
        if(not isinstance(newyspeed,bool)):
            self.yspeed=newyspeed

    def betweenCheck(self,target):
        R = False
        L = False
        U = False
        D = False

        if(target.x<=self.x and self.x <= target.x+target.length):
            L=True
        elif(target.x<=self.x+self.radius and self.x+self.radius <= target.x+target.length):
            R=True
        if(target.y<=self.y and self.y <= target.y+target.length):
            U=True
        elif(target.y<=self.y+self.radius and self.y+self.radius <= target.y+target.length):
            D=True

        if R and (U or D):
            if self.xspeed>=0:
                self.xspeed*=-1
        if L and (U or D):
            if self.xspeed<=0:
                self.xspeed*=-1
        if U and (R or L) and not D:
            if self.yspeed<=0:
                self.yspeed=target.speed
        if D and (R or L) and not U:
            if self.yspeed>=0:
                self.bounce()

    #움직임 수정
    def update(self):
        if self.allowphysics:
            self.physics()
        self.y+=self.yspeed
        self.x+=self.xspeed






