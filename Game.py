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
orientationIndex = 0

class tail():
    def __init__(self, x, y, orientation, moved, orientationIndex):
        self.x = x
        self.y = y
        self.orientation = orientation
        self.moved = moved
        self.orientations = []
        self.orientationIndex = orientationIndex

snake = [tail(screenSize[0]//2 - 3*snakeSize, screenSize[0]//2, 2, 10, orientationIndex), tail(screenSize[0]//2 - 2*snakeSize, screenSize[0]//2, 2, 10, orientationIndex),tail(screenSize[0]//2 - snakeSize, screenSize[0]//2, 2, 10, orientationIndex)
, tail(screenSize[0]//2, screenSize[0]//2, 2, 10, orientationIndex)]

pygame.draw.rect(screen, redColor, [foodX, foodY, snakeSize, snakeSize])

while not exitGame:
    screen.fill(blackColor)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exitGame = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                for j in snake:
                    j.orientations.append(2)
                    if j.orientationIndex == len(j.orientations) - 1:
                        j.moved = 0
                break
            elif event.key == pygame.K_UP:
                for j in snake:
                    j.orientations.append(1)
                    if j.orientationIndex == len(j.orientations) - 1:
                        j.moved = 0
                break

            elif event.key == pygame.K_DOWN:
                for j in snake:
                    j.orientations.append(3)
                    if j.orientationIndex == len(j.orientations) - 1:
                        j.moved = 0
                break
            elif event.key == pygame.K_LEFT:
                for j in snake:
                    j.orientations.append(4)
                    if j.orientationIndex == len(j.orientations) - 1:
                        j.moved = 0
                break

    for i in range(len(snake)):
        print(len(snake) - 1 - i, i, snake[i].moved , "ASD")
        if snake[i].moved == len(snake) - 1 - i:
            print(snake[i].orientationIndex, i, snake[i].moved)
            snake[i].orientation = snake[i].orientations[snake[i].orientationIndex]
            snake[i].orientationIndex += 1
            if snake[i].orientationIndex != len(snake[i].orientations):
                snake[i].moved = 0

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

        snake.insert(0, tail(insertX, insertY, snake[0].orientation, snake[0].moved, snake[0].orientationIndex))

        foodX = random.randrange(0, 600 , snakeSize)
        foodY = random.randrange(0, 600 , snakeSize)
        canAppend = False

    sameLine = 0

    pygame.draw.rect(screen, redColor, [foodX, foodY, snakeSize, snakeSize])
    pygame.display.update()
    clock.tick(10)
pygame.quit()
exit
