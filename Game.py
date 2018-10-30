import pygame
import random
import time

blackColor = (0, 0, 0)
whiteColor = (255, 255, 255)
redColor = (255, 0, 0)
screenSize = (600, 600)

pygame.init()
screen = pygame.display.set_mode(screenSize)
pygame.display.set_caption('Snake Game')
screen.fill(blackColor)
clock = pygame.time.Clock()
pygame.font.init()

exitGame = False
snakeSize = screenSize[1]//40
orientations = []
orientationBackup = 0
moves = 0
foodX = random.randrange(0, 600 , snakeSize)
foodY = foodX
canAppend = False
snakeOrientation = 0
sameLine = 0

class tail():
    def __init__(self, x, y, orientation, moved):
        self.x = x
        self.y = y
        self.orientation = orientation
        self.moved = moved

snake = [tail(screenSize[0]//2 - 3*snakeSize, screenSize[0]//2, 2, 10), tail(screenSize[0]//2 - 2*snakeSize, screenSize[0]//2, 2, 10),tail(screenSize[0]//2 - snakeSize, screenSize[0]//2, 2, 10)
, tail(screenSize[0]//2, screenSize[0]//2, 2, 10)]

pygame.draw.rect(screen, redColor, [foodX, foodY, snakeSize, snakeSize])

while not exitGame:
    screen.fill(blackColor)

    for i in range(len(snake)):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exitGame = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    orientations.append(2)
                    orientationBackup = 2
                    if len(orientations) == 1:
                        for j in snake:
                            j.moved = 0
                elif event.key == pygame.K_UP:
                    orientations.append(1)
                    orientationBackup = 2
                    if len(orientations) == 1:
                        for j in snake:
                            j.moved = 0
                elif event.key == pygame.K_DOWN:
                    orientations.append(3)
                    orientationBackup = 2
                    if len(orientations) == 1:
                        for j in snake:
                            j.moved = 0
                elif event.key == pygame.K_LEFT:
                    orientations.append(4)
                    orientationBackup = 2
                    if len(orientations) == 1:
                        for j in snake:
                            j.moved = 0

        if snake[i].moved == len(snake) - 1 - i:
            try:
                snake[i].orientation = orientations[0]
            except:
                pass
            try:
                if snake[i].orientation == orientations[0]:
                    snake[i].orientation = orientations[1]
            except:
                pass
            if i == 0 :
                try:
                    orientations.remove(orientations[0])
                except:
                    pass
                if len(orientations) >= 1:
                    for j in snake:
                        j.moved = 0

        if snake[i].orientation == 1:
            snake[i].y -= snakeSize
        elif snake[i].orientation == 2:
            snake[i].x += snakeSize
        elif snake[i].orientation == 3:
            snake[i].y += snakeSize
        elif snake[i].orientation == 4:
            snake[i].x -= snakeSize

        if snake[len(snake) - 1].x <= foodX + snakeSize and snake[len(snake) - 1].y <= foodY + snakeSize and snake[len(snake) - 1].x >= foodX and snake[len(snake) - 1].y >= foodY:
            canAppend = True

        if i == len(snake) - 1:
            snakeOrientation = snake[i].orientation
        else:
            if snake[i].orientation != snakeOrientation:
                sameLine += 1

        snake[i].moved += 1

        if snake[i].x > 600:
            snake[i].x = 0
        if snake[i].x < 0:
            snake[i].x = 600
        if snake[i].y > 600:
            snake[i].y = 0
        if snake[i].y < 0:
            snake[i].y = 600

        pygame.draw.rect(screen, whiteColor, [snake[i].x, snake[i].y, snakeSize, snakeSize])

    if canAppend and sameLine == 0:
        insertX = snake[0].x
        insertY = snake[0].y
        if snake[0].orientation == 1:
            insertY = snake[0].y + snakeSize
        elif snake[0].orientation == 2:
            insertX = snake[0].x - snakeSize
        elif snake[0].orientation == 3:
            insertY = snake[0].y - snakeSize
        elif snake[0].orientation == 4:
            insertX += snakeSize

        snake.insert(0, tail(insertX, insertY, snake[0].orientation, snake[0].moved))

        foodX = random.randrange(0, 600 , snakeSize)
        foodY = random.randrange(0, 600 , snakeSize)
        canAppend = False

    sameLine = 0

    pygame.draw.rect(screen, redColor, [foodX, foodY, snakeSize, snakeSize])
    pygame.display.update()
    clock.tick(30)
pygame.quit()
exit
