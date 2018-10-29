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


class tail():
    def __init__(self, x, y, orientation, moved, moves):
        self.x = x
        self.y = y
        self.orientation = orientation
        self.moved = moved
        self.moves = moves

orientation = 2
moved = 0
moves = 0

snake = [tail(screenSize[0]//2 - 2*snakeSize, screenSize[0]//2, orientation, 0, 0),tail(screenSize[0]//2 - snakeSize, screenSize[0]//2, orientation, 0, 0)
, tail(screenSize[0]//2, screenSize[0]//2, orientation, 0, 0)]

foodX = random.randrange(0, 600 , snakeSize)
foodY = foodX

pygame.draw.rect(screen, redColor, [foodX, foodY, snakeSize, snakeSize])

while not exitGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exitGame = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                orientation = 2
                moved = 0
                for j in snake:
                    j.moved = moved
                    j.moves += 1
            elif event.key == pygame.K_UP:
                orientation = 1
                moved = 0
                for j in snake:
                    j.moved = moved
                    j.moves += 1
            elif event.key == pygame.K_DOWN:
                orientation = 3
                moved = 0
                for j in snake:
                    j.moved = moved
                    j.moves += 1
            elif event.key == pygame.K_LEFT:
                orientation = 4
                moved = 0
                for j in snake:
                    j.moved = moved
                    j.moves += 1

    screen.fill(blackColor)

    for i in range(len(snake)):
        if snake[i].moved == len(snake) - 1 - i:
            snake[i].orientation = orientation
            if snake[i].moves > 1:
                snake[i].moves -= 1

        if snake[i].orientation == 1:
            snake[i].y -= snakeSize
        elif snake[i].orientation == 2:
            snake[i].x += snakeSize
        elif snake[i].orientation == 3:
            snake[i].y += snakeSize
        elif snake[i].orientation == 4:
            snake[i].x -= snakeSize

        snake[i].moved += 1

        if snake[len(snake) - 1].x <= foodX + snakeSize and snake[len(snake) - 1].y <= foodY + snakeSize and snake[len(snake) - 1].x >= foodX and snake[len(snake) - 1].y >= foodY:
            insertX = snake[1].x + snake[0].x - snake[1].x
            insertY = snake[1].y + snake[0].y - snake[1].y
            snake.append(None)
            for k in range(len(snake) - 2, -1, -1):
                snake[k + 1] = snake[k]
            snake[0] = tail(insertX, insertY, orientation, snake[1].moved - 1, snake[1].moves - 1)

        pygame.draw.rect(screen, whiteColor, [snake[i].x, snake[i].y, snakeSize, snakeSize])

    pygame.draw.rect(screen, redColor, [foodX, foodY, snakeSize, snakeSize])

    pygame.display.update()
    clock.tick(10)
pygame.quit()
exit