

import pygame
import os
import sys
import time
from enum import Enum, auto

class STONE(Enum):
  NONE = 0
  BLACK = auto()
  WHITE = auto()

WIN_STONE_COUNT = 5

print(list(STONE))

screen = pygame.display.set_mode((1000, 1000))

clock = pygame.time.Clock()



class OMOK:
  def __init__(self, width, height, mode):
    self.run = True
    self.width = width
    self.height = height
    self.mode = mode
    self.map = [[STONE.NONE] * (width + 1) for i in range(height + 1)]
    self.stoneRadius = (screen.get_height() / height+ screen.get_width() / width) / 4 # / 2 / 2
    self.turn = STONE.BLACK
    #game init
    pygame.init()

  def posToStoneIdx(self, pos):
    for i in range(self.width + 1):
      for j in range(self.height + 1):
        width = screen.get_width() / self.width
        height =  screen.get_height() / self.height

        halfw = width / 2
        halfh = height / 2

        if width * i - halfw < pos[0] < width * (i + 1) - halfw:
          if height * j - halfh < pos[1] < height * (j + 1) - halfh:
            return (i, j)
    return False

  def stoneCount(self, i, j, stone):
    
    print(i, j, stone)
    #오른쪽
    if j + WIN_STONE_COUNT < self.width + 1:
      count = 0
      for k in range(WIN_STONE_COUNT):
        if self.map[i][j + k] == stone:
          count += 1
          if count == WIN_STONE_COUNT:
            return stone
        else:
          break

    #좌하단
    if i + WIN_STONE_COUNT < self.height + 1 and j - WIN_STONE_COUNT >= 0:
      count = 0
      for k in range(WIN_STONE_COUNT):
        if self.map[i + k][j - k] == stone:
          count += 1 
          if count == WIN_STONE_COUNT:
            return stone
        else:
          break
    #아래
    if i + WIN_STONE_COUNT < self.height + 1:
      count = 0
      for k in range(WIN_STONE_COUNT):
        if self.map[i + k][j] == stone:
          count += 1
          if count == WIN_STONE_COUNT:
            return stone
        else:
          break
    #우하단
    if i + WIN_STONE_COUNT < self.height + 1 and j + WIN_STONE_COUNT < self.width + 1:
      count = 0
      for k in range(WIN_STONE_COUNT):
        if self.map[i + k][j + k] == stone:
          count += 1
          if count == WIN_STONE_COUNT:
            return stone
        else:
          break

    return STONE.NONE

  def gameEndCheck(self):
    stone = STONE.NONE
  
    for i in range(self.width + 1):
      for j in range(self.height + 1):
        if self.map[i][j] != STONE.NONE:
          stone = self.stoneCount(i, j, self.map[i][j])
          if stone != STONE.NONE:
            return stone
    
    return stone
          
          
        
  def proc(self, pos):
    print(pos)
    idx = self.posToStoneIdx(pos)

    if self.map[idx[0]][idx[1]] != STONE.NONE:
      return

      

    if idx != False:
      print("DEBUG : ", idx)
      self.map[idx[0]][idx[1]] = self.turn

      stone = self.gameEndCheck()
      if stone != STONE.NONE:
        print("WIN : ", stone)
        self.run = False
        return

      if self.turn == STONE.BLACK:
        self.turn = STONE.WHITE
      else:
        self.turn = STONE.BLACK

    

  def draw(self):

    # pygame.draw.line(screen, pygame.color.Color(0,0,0), (0,0), (screen.get_width(), screen.get_height()), 3)
    width = screen.get_width() / self.width
    height =  screen.get_height() / self.height    

    for i in range(self.height):
      pygame.draw.line(screen, pygame.color.Color(0, 0, 0),
       (0, height * i),
      (screen.get_width(), height * i), 3)

    for j in range(self.width):
      pygame.draw.line(screen, pygame.color.Color(0, 0, 0), 
      (width * j, 0), 
      (width * j, screen.get_height()), 3)

    for i in range(self.width + 1):
      for j in range(self.height + 1):
        if self.map[i][j] == STONE.BLACK:
          # pygame.draw.circle(screen, (0,0,0), [width * i - self.stoneRadius, height * j - self.stoneRadius], self.stoneRadius)
          pygame.draw.ellipse(screen, (255,0,0), pygame.Rect([width * i - self.stoneRadius, height * j - self.stoneRadius], (self.stoneRadius * 2, self.stoneRadius * 2)))
        elif self.map[i][j] == STONE.WHITE:
          pygame.draw.ellipse(screen, (0,255,0), pygame.Rect([width * i - self.stoneRadius, height * j - self.stoneRadius], (self.stoneRadius * 2, self.stoneRadius * 2)))
          pygame.draw.ellipse(screen, (0,0,0), pygame.Rect([width * i - self.stoneRadius, height * j - self.stoneRadius], (self.stoneRadius * 2, self.stoneRadius * 2)), 2)

  def gameEnd(self):

    if self.turn == STONE.BLACK:
      screen.fill((255,0,0))
    else:
      screen.fill((0, 255, 0))
    sf = pygame.font.SysFont("Monospace",40,bold=True)
    textStr = " "
    text = sf.render(textStr,True,(0,172,255))
    screen.blit(text,((screen.get_width()/2, screen.get_height()/2)))
    if self.turn == STONE.BLACK:
      textStr = "RED WIN!"
    else:
      textStr = "GREEN WIN!"
    text = sf.render(textStr,True,(0,172,255))
    screen.blit(text,(screen.get_width()/2, screen.get_height()/2  + 100))


    pygame.display.flip()
    time.sleep(2)




omok = OMOK(19, 19, 0)

while omok.run:
  key = 1
  pos = 0
  #KEY INPUT
  for event in pygame.event.get():
    if event.type == pygame.QUIT:

      omok.run = False
      break
    elif event.type == pygame.KEYDOWN:
      keyStatus = 1
      key = event.key

    elif event.type == pygame.KEYUP:
      keyStatus = 0
      key = event.key
    elif event.type == pygame.MOUSEBUTTONDOWN:
      pos = event.pos

  #UPDATE
  
  # print(key)
  if (pos != 0):
    
    omok.proc(pos)

  #DRAW
  screen.fill((198,139,18))
  omok.draw()



  pygame.display.flip()
  clock.tick(10)

omok.gameEnd()
