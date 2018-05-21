

import pygame
import os
import sys
import time
from enum import Enum, auto

class STONE(Enum):
  NONE = 0
  BLACK = auto()
  WHITE = auto()

print(list(STONE))

screen = pygame.display.set_mode((1000, 1000))

clock = pygame.time.Clock()

run = True

class OMOK:
  def __init__(self, width, height, mode):
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
  
  def proc(self, pos):
    print(pos)
    idx = self.posToStoneIdx(pos)
    if idx != False:
      print("DEBUG : ", idx)
      self.map[idx[0]][idx[1]] = self.turn
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
          # pygame.draw.circle(screen, (0, 0, 0), [width * i - self.stoneRadius, height * j - self.stoneRadius], self.stoneRadius)
          pygame.draw.ellipse(screen, (0,0,0), pygame.Rect([width * i - self.stoneRadius, height * j - self.stoneRadius], (self.stoneRadius * 2, self.stoneRadius * 2)))
        elif self.map[i][j] == STONE.WHITE:
          pygame.draw.ellipse(screen, (0xff,0xff,0xff), pygame.Rect([width * i - self.stoneRadius, height * j - self.stoneRadius], (self.stoneRadius * 2, self.stoneRadius * 2)))
          pygame.draw.ellipse(screen, (0,0,0), pygame.Rect([width * i - self.stoneRadius, height * j - self.stoneRadius], (self.stoneRadius * 2, self.stoneRadius * 2)), 2)



omok = OMOK(19, 19, 0)

while run:
  key = 1
  pos = 0
  #KEY INPUT
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      print("GAME END")
      run = False
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
  screen.fill((255,255,255))
  omok.draw()



  pygame.display.flip()
  clock.tick(10)

