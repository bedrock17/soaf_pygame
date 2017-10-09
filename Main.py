__author__ = 'sh'
import pygame
import os
import sys
import time
import GameInfo
import Ball
import Rectangle
import random

BLACK = (0, 0, 0)

def drawBall(ball):
    pygame.draw.ellipse(screen, BLACK, pygame.Rect([ball.x, ball.y], (ball.radius, ball.radius)))

def drawRect(rect):
    pygame.draw.rect(screen, BLACK, [rect.x, rect.y, rect.length, rect.length])


pygame.init()

screen = pygame.display.set_mode((GameInfo.displayWidth, GameInfo.displayHeight))

clock = pygame.time.Clock()

key = 0
text = " "
count = 3000
max = 0
score = 0

diff = 7 #난이도 (1이 제일 높음)

ball = Ball.Ball(GameInfo.displayWidth / 2, GameInfo.displayHeight / 2)
rects = list()

while GameInfo.Run:
    #KEY INPUT
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GameInfo.Run = False
        elif event.type == pygame.KEYDOWN:
            keyStatus = 1
            key = event.key

        elif event.type == pygame.KEYUP:
            keyStatus = 0
            key = event.key

    #UPDATE
    if key == pygame.K_RIGHT and keyStatus:
            ball.setStatus(newxspeed = ball.xspeed+2)
    if key == pygame.K_LEFT and keyStatus:
            ball.setStatus(newxspeed = ball.xspeed-2)

    if ball.y + 50 >= GameInfo.displayHeight:
        ball.bounce()

    if ball.x <= 0 :
        ball.setStatus(newxspeed = ball.xspeed * -0.9)
        ball.setStatus(newx = ball.x + 1)
        ball.setStatus(newx = 0)

    elif ball.x + ball.radius >= GameInfo.displayWidth :
        ball.setStatus(newxspeed = ball.xspeed * -0.9)
        ball.setStatus(newx = ball.x -1)
        ball.setStatus(newx = GameInfo.displayWidth - ball.radius)

    if rects.__len__() <= 15 and count%(diff*10) == 0:
        rects.append(Rectangle.Rectangle(random.random() * GameInfo.displayWidth-GameInfo.rectangleSize / 2,
         -GameInfo.rectangleSize, GameInfo.rectangleSize, 1 + (count / 400)))

    if count%1000 == 0 and diff > 1:
        diff -= 1

    for rect in rects:
        ball.betweenCheck(rect)
        rect.update()
        if GameInfo.displayHeight <= rect.y:
            rects.remove(rect)
            score += 1
    ball.update()
    count += 1
    if max <= count-ball.y:
        max = count-ball.y


    #DRAW
    screen.fill((255,255,255))

    drawBall(ball)

    for rect in rects:
        drawRect(rect)

    if key :
        sf = pygame.font.SysFont("Monospace",20,bold=True)
        textStr = "score: " + str(score)
        text = sf.render(textStr,True,(0,172,255))
        screen.blit(text,(50,40))

    pygame.display.flip()
    clock.tick(GameInfo.framePerSecond)

    if(ball.y >= GameInfo.displayHeight):
        break

screen.fill((255,255,255))
sf = pygame.font.SysFont("Monospace",40,bold=True)
textStr = "Game Over"
text = sf.render(textStr,True,(0,172,255))
screen.blit(text,(GameInfo.displayWidth/2-GameInfo.displayWidth/5,GameInfo.displayHeight/2))
textStr = str(score)
text = sf.render(textStr,True,(0,172,255))
screen.blit(text,(GameInfo.displayWidth/2-GameInfo.displayWidth/5,GameInfo.displayHeight/2+100))

pygame.display.flip()
time.sleep(2)
