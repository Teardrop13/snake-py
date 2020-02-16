import random
import pygame

green = 102, 255, 51

class Block:
    def __init__(self, x, y, surface, blockSize):
        self.x = x
        self.y = y
        self.surface = surface
        self.blockSize = blockSize

    def moveBlock(self, x, y):
        self.x = x
        self.y = y

    def drawBlock(self):
        block = pygame.Rect(self.x * blockSize, self.y * blockSize, blockSize, blockSize)
        pygame.draw.rect(self.surface, green, block)


class Point:
    def __init__(self, width, height):
        self.x = random.randint(0, width)
        self.y = random.randint(0, height)

class Snake:
    def __init__(self, surface, width, height, blockSize):
        self.blocks = [Block(14,12, surface), Block(15,12, surface), Block(16,12, surface), Block(17,12, surface)]
        self.movesList = ["right"]
        self.surface = surface 
        self.width = width
        self.height = height
        self.blockSize = blockSize
    
    def nextMove(self, move):
        if self.movesList[-1] != move:
            self.movesList.append(move)

    def move(self):
        if self.movesList[0] == "down":
            self.blocks.append(Block(self.blocks[-1].x, self.blocks[-1].y + 1, self.surface, self.blockSize))
        if self.movesList[0] == "up":
            self.blocks.append(Block(self.blocks[-1].x, self.blocks[-1].y - 1, self.surface, self.blockSize))
        if self.movesList[0] == "left":
            self.blocks.append(Block(self.blocks[-1].x - 1, self.blocks[-1].y, self.surface, self.blockSize))
        if self.movesList[0] == "right":
            self.blocks.append(Block(self.blocks[-1].x + 1, self.blocks[-1].y, self.surface, self.blockSize))
        if len(self.movesList) > 1:
            self.movesList.pop(0)
        self.blocks.pop(0)

    # x,y - coordinates where the snake is heading in next move
    # returns True when colision occures
    def colisionCheck(self):
        x = self.blocks[-1].x
        y = self.blocks[-1].y
        if x > self.width or x < 0 or y > self.height or y < 0:
            return True
        return False

    def draw(self):
        for block in self.blocks:
            block.drawBlock()
