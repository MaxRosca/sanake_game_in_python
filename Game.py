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

class Snake():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.xspeed = 1
        self.yspeed = 0
        self.history = []
        self.total = 10

    def draw(self):
        for i in self.history:
            pygame.draw.rect(screen, whiteColor, [i[0], i[1], size, size])

    def update(self):
        self.x += self.xspeed
        self.y += self.yspeed
        if self.x > 600:
            self.x = 0
        if self.x < 0:
            self.x = 600
        if self.y > 600:
            self.y = 0
        if self.y < 0:
            self.y = 600
        if len(self.history) >= self.total:
            self.history.remove(self.history[0])
        self.history.append([self.x, self.y])


    def setSpeed(self, directions):
        self.xspeed = size * directions[0]
        self.yspeed = size * directions[1]

    def increaseTail(self):
        self.total += 1

    def isHited(self):
        containing = 0
        for headPos in self.history:
            containing = 0
            for i in range(len(self.history)):
                if self.history[i] == headPos:
                    containing += 1
            # print(containing)
            if containing >= 2:
                return True
        return False

class Food():
    def __init__(self):
        self.x = random.randrange(0, screenSize[0], size)
        self.y = random.randrange(0, screenSize[1], size)

    def nextPos(self):
        self.x = random.randrange(0, screenSize[0], size)
        self.y = random.randrange(0, screenSize[1], size)

    def draw(self):
        pygame.draw.rect(screen, redColor, [self.x, self.y, size, size])

    def isEaten(self, snake):
        if self.x == snake.x and self.y + size/2 == snake.y + size/2:
            return True
        return False

size = screenSize[0]//40
snake = Snake()
food = Food()
directions = (0, 1)

gameOver = False

while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if directions != (0, 1):
                    directions = (0, -1)
            if event.key == pygame.K_RIGHT:
                if directions != (-1, 0):
                    directions = (1, 0)
            if event.key == pygame.K_DOWN:
                if directions != (0, -1):
                    directions = (0, 1)
            if event.key == pygame.K_LEFT:
                if directions != (1, 0):
                    directions = (-1, 0)
            if event.key == pygame.K_r:
                snake = Snake()

    screen.fill(blackColor)

    food.draw()

    snake.setSpeed(directions)
    snake.update()
    snake.draw()

    if food.isEaten(snake):
        snake.increaseTail()
        food.nextPos()

    if snake.isHited():
        snake = Snake()

    pygame.display.update()
    clock.tick(10)

pygame.quit()
exit
