
import pygame
import os
import sys
import time
import GameInfo
import Ball
import Rectangle
import random

BLACK = (0, 0, 0)
WHITE = (0xff, 0xff, 0xff)

objcolor = WHITE
bgcolor = BLACK

def drawBall(ball):
	pygame.draw.ellipse(screen, objcolor, pygame.Rect([ball.x, ball.y], (ball.radius, ball.radius)))

def drawRect(rect):
	pygame.draw.rect(screen, objcolor, [rect.x, rect.y, rect.length, rect.length])

pygame.init()

screen = pygame.display.set_mode((GameInfo.displayWidth, GameInfo.displayHeight))

clock = pygame.time.Clock()


text = " "
count = 3000
max = 0
score = 0

diff = 7 #난이도 (1이 제일 높음)

ball = Ball.Ball(GameInfo.displayWidth / 2, GameInfo.displayHeight / 2)
rects = list()

ldown = False
rdown = False

while GameInfo.Run:
	#KEY INPUT
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			GameInfo.Run = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				rdown = True
			elif event.key == pygame.K_LEFT:
				ldown = True
		elif event.type == pygame.KEYUP:			
			if event.key == pygame.K_RIGHT:
				rdown = False
			elif event.key == pygame.K_LEFT:
				ldown = False

	#UPDATE
	
	if rdown:
		ball.setStatus(newxspeed = ball.xspeed+2)
	if ldown:
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
	screen.fill(bgcolor)

	drawBall(ball)

	for rect in rects:
		drawRect(rect)

	sf = pygame.font.SysFont("Monospace",20,bold=True)
	textStr = "score: " + str(score)
	text = sf.render(textStr,True,(0,172,255))
	screen.blit(text,(50,40))

	pygame.display.flip()
	clock.tick(GameInfo.framePerSecond)

	if(ball.y >= GameInfo.displayHeight):
		break

screen.fill(bgcolor)
sf = pygame.font.SysFont("Monospace",40,bold=True)
textStr = "Game Over"
text = sf.render(textStr,True,(0,172,255))
screen.blit(text,(GameInfo.displayWidth/2-GameInfo.displayWidth/5,GameInfo.displayHeight/2))
textStr = str(score)
text = sf.render(textStr,True,(0,172,255))
screen.blit(text,(GameInfo.displayWidth/2-GameInfo.displayWidth/5,GameInfo.displayHeight/2+100))

pygame.display.flip()
time.sleep(2)
