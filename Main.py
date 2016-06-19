__author__ = 'sh'
import pygame
import os
import sys
import time
import GameInfo
import Ball
import Rectangle

def drawBall(ball):
    pygame.draw.ellipse(screen,(0,0,0),pygame.Rect([ball.x,ball.y],(ball.radius,ball.radius)))
def drawRect(rect):
    pygame.draw.rect(screen,(0,0,0), [rect.x, rect.y, rect.length, rect.length])


pygame.init()

screen = pygame.display.set_mode((GameInfo.displayWidth,GameInfo.displayHeight))

clock = pygame.time.Clock()

key = 0
text =" "
count=GameInfo.displayHeight
max=0

ball = Ball.Ball(170,0)
rects = list()

rects.append(Rectangle.Rectangle(100,100,100,1))

while GameInfo.Run:

    #KEY INPUT
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GameInfo.Run=False
        elif event.type == pygame.KEYDOWN:
            keyStatus ="KEY DOWN"
            key = event.key

        elif event.type == pygame.KEYUP:
            keyStatus ="KEY UP"
            key = event.key

    #UPDATE
    if key == pygame.K_RIGHT and keyStatus == "KEY DOWN":
            ball.setStatus(newxspeed=ball.xspeed+2)
    if key == pygame.K_LEFT and keyStatus == "KEY DOWN":
            ball.setStatus(newxspeed=ball.xspeed-2)

    if key == pygame.K_SPACE and keyStatus =="KEY DOWN":
            ball.setStatus(newyspeed=ball.yspeed-10)

    if ball.y+50>=GameInfo.displayHeight:
        ball.setStatus(newyspeed=-15)

    if ball.x <= 0 :
        ball.setStatus(newxspeed=ball.xspeed*-0.9)
        ball.setStatus(newx=0)

    elif ball.x + 50 >= GameInfo.displayWidth :
        ball.setStatus(newxspeed=ball.xspeed*-0.9)
        ball.setStatus(newx=GameInfo.displayWidth-ball.radius)



    for rect in rects:
        ball.betweenCheck(rect)
        rect.update()
        if GameInfo.displayHeight <= rect.y:
            rects.remove(rect)
    ball.update()
    count+=1
    if max<=count-ball.y:
        max = count-ball.y


    #DRAW
    screen.fill((255,255,255))

    drawBall(ball)

    for rect in rects:
        drawRect(rect)




    if key :
        sf = pygame.font.SysFont("Monospace",20,bold=True)
        textStr = pygame.key.name(key)+" "+keyStatus+" "+str(max)
        text = sf.render(textStr,True,(0,172,255))
        screen.blit(text,(50,40))

    pygame.display.flip()
    clock.tick(GameInfo.framePerSecond)

pygame.QUIT()