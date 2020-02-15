import sys
import pygame
import time


def drawButton(surface, x, y, pictureFile):
    image = pygame.image.load(pictureFile)
    imageRect = image.get_rect()
    imageRect.x = x
    imageRect.y = y
    surface.blit(image, imageRect)

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+imageRect.width > mouse[0] > x and y+imageRect.height > mouse[1] > y and click[0] == 1:
        return True
    else:
        return False

def drawNumber(surface, font, x, y, number):
    text = font.render(str(number), False, (0,0,0))
    textSize = font.size(str(number))
    surface.blit(text, (x-(textSize[0]/2), y-(textSize[1]/2)))


yellow = 255, 255, 102
green = 102, 255, 51

# 0 - menu, 1 - game started
gameState = 0

# Snake speed 1-5, multiplication of 80ms, time before rendering next frame
delay = 3

buttonEvents = []
minusPreviousState = plusPreviousState = False


pygame.init()
pygame.font.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
myfont = pygame.font.SysFont('Arial', 60)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(yellow)
    buttonEvents = pygame.key.get_pressed()

    if gameState == 0:
        if drawButton(screen, 250, 200, "startButton.png") == True:
            gameState = 1

        if drawButton(screen, 250, 320, "minusButton.png") == True:
            if minusPreviousState == False:
                if delay < 5:
                    delay += 1
            minusPreviousState = True
        else:
            minusPreviousState = False

        if drawButton(screen, 470, 320, "plusButton.png") == True:
            if plusPreviousState == False:
                if delay > 1:
                    delay -= 1
            plusPreviousState = True
        else:
            plusPreviousState = False

        drawNumber(screen, myfont, 400, 360, 6-delay)
        time.sleep(0.05)

    if gameState == 1:
        
        time.sleep(0.08 * delay)

    pygame.display.flip()