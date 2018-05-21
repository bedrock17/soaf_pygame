__author__ = 'sh'

import GameInfo




class Rectangle:
    x=0
    y=0
    length=0
    speed=0
    def __init__(self,xpos,ypos,length,speed):
        self.x=xpos
        self.y=ypos
        self.length=length
        self.speed=speed


    def setStatus(self,newxpos=False,newypos=False,newspeed=False):
        if(not isinstance(newxpos,bool)):
            self.x=newxpos
        if(not isinstance(newypos,bool)):
            self.y=newypos
        if(not isinstance(newspeed,bool)):
            self.speed=newspeed

    def update(self):
        self.y+=self.speed


