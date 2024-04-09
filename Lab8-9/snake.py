import math
import time
import datetime
import pygame
import random

pygame.init()  # initialization
CLOCK = pygame.time.Clock()
FPS = 8  # speed of the game
WINDOW_WIDTH, WINDOW_HEIGHT = 480, 440  # program window size
SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT + 80))  # create window
WHITE = (255, 255, 255)  # colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

BLOCK_SIZE = 20  # the size of block (square)

font = pygame.font.SysFont('Verdana', 63, bold=True)  # big font
font_small = pygame.font.SysFont('Verdana', 18)  # small font

SCORE = 0  # score
LEVEL = 0  # level

pygame.display.set_caption('Snake')  # name of window

POSITIONS_OF_THE_WALL = ('top', 'left', 'bottom', 'right')  # tuple of wall positions


def check_food_collision() -> bool:  # food should lay on wall or snake
    global super_food, food, walls, snake
    foods = [food]
    if super_food:
        foods.append(super_food)

    for f in foods:
        for wa in walls:
            for p in wa.construction:
                if f.collide(p):
                    return True

        for tail_of_snake in snake.body:
            if f.collide(tail_of_snake):
                return True

    return False


def generate_random_color() -> tuple:  # all item will be coloured randomly
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


def own_round(value, base=BLOCK_SIZE):  # rounding the coordinates for following the grid
    return base * round(value / BLOCK_SIZE)


def draw_grid():  # draw grid
    for i in range(0, WINDOW_WIDTH, BLOCK_SIZE):
        for j in range(0, WINDOW_HEIGHT + 20, BLOCK_SIZE):
            pygame.draw.rect(SCREEN, pygame.Color('grey'), (i, j, BLOCK_SIZE, BLOCK_SIZE), 1)


class Particle:  # part of every object
    def __init__(self, _x=0, _y=0, color=(0, 0, 0), _block_size=BLOCK_SIZE):
        #simple food is smaller than simple block
        super().__init__()
        self.block_size = _block_size
        self.x = _x
        self.y = _y
        self.image = pygame.Surface((_block_size, _block_size))  # square form
        self.image.fill(color)

    def draw(self):
        SCREEN.blit(self.image, self.get_coordinates())

    def get_coordinates(self) -> tuple:  # tuple of x and y
        return self.x, self.y


class Wall:
    def __init__(self, _position='top', _length=25, _color=(0, 0, 0)):
        self.construction = []  # wall consists of array of particles (squares)
        self.position = _position  # left, right, top, bottom
        self.length = _length  # length of wall
        self.color = _color
        self.construct()  # the tail of wall (squares)

    def construct(self):
        if self.position == 'top' or self.position == 'bottom':  # bottom or top
            x = own_round(0)
            y = 440 if self.position == 'top' else WINDOW_HEIGHT  # y is the border
            for i in range(self.length):
                self.construction.append(Particle(_x=x + i * BLOCK_SIZE, _y=y, color=self.color))
        if self.position == 'right' or self.position == 'left':  # left or right
            y = own_round(0)
            x = 480 if self.position == 'left' else WINDOW_WIDTH - BLOCK_SIZE  # y is the border
            for i in range(self.length):
                self.construction.append(Particle(_x=x, _y=y + i * BLOCK_SIZE, color=self.color))

    def draw(self):  # draw wall
        for particle in self.construction:
            particle.draw()


class Food:
    def __init__(self):
        # simple food is smaller than a block
        self.particle = Particle(color=generate_random_color(), _block_size=int(BLOCK_SIZE/math.sqrt(2)))
        self.set_random_position()
        self.color = GREEN

    def set_random_position(self):  # food can appear anywhere
        self.particle.x = own_round(random.randint(BLOCK_SIZE, WINDOW_WIDTH - BLOCK_SIZE))
        self.particle.y = own_round(random.randint(BLOCK_SIZE, WINDOW_HEIGHT - BLOCK_SIZE))

    def draw(self):
        self.particle.draw()  # draw the food

    def collide(self, particle) -> bool:  # check if food does not lie on wall or snake
        return self.particle.x == particle.x and self.particle.y == particle.y


COLOR_FOR_SUPER_FOOD = generate_random_color()  # I need special constant color for the super food


class SuperFood(Food):
    def __init__(self):
        super().__init__()
        self.particle = Particle(color=COLOR_FOR_SUPER_FOOD, _block_size=BLOCK_SIZE)
        self.set_random_position()


class Snake:
    def __init__(self, *args, **kwargs):
        self.body = [Particle(BLOCK_SIZE, BLOCK_SIZE, generate_random_color())]
        self.tail_color = generate_random_color()  # all blocks of tail should have the same color
        self.add_tail()  # add two extra blocks to the head
        self.add_tail()
        self.block = BLOCK_SIZE
        self.dx = self.block  # by default snake is moving in the right direction
        self.dy = 0

    def head(self):  # head of the snake
        return self.body[0]

    def move(self):  # motion
        for i in range(len(self.body) - 1, 0, -1):  # all particles move
            # self.body[i].set_coordinates(self.body[i].get_coordinates())
            self.body[i].x = self.body[i - 1].x  # except head, all blocks get coordinates of previous block
            self.body[i].y = self.body[i - 1].y

        self.head().x += self.dx  # head moves by dx
        self.head().y += self.dy

        if self.head().x > WINDOW_WIDTH:  # if snake reaches the border, it starts motion form the opposite edge
            self.head().x = 0
        if self.head().x < 0:
            self.head().x = WINDOW_WIDTH
        if self.head().y > WINDOW_HEIGHT:
            self.head().y = 0
        if self.head().y < 0:
            self.head().y = WINDOW_HEIGHT

    def draw(self):
        for i, particle in enumerate(self.body):
            particle.draw()

    def add_tail(self):  # increase the length of snake
        self.body.append(Particle(color=self.tail_color))

    def head_collide(self, particle) -> bool:  # if snake collides with its tail, or wall, or food
        return self.head().x == particle.x and self.head().y == particle.y


super_food_appeared = False  # conditions
level_increased = False
game_over = False

snake = Snake()  # objects init
food = Food()
super_food = None # by default super food is not exist
walls = list()
color_of_wall = generate_random_color()  # wall should have same color

DISAPPEAR_SUPER_FOOD_EVENT = pygame.USEREVENT+1


def super_food_disappears_after_some_seconds(seconds=6):  # the time of existing superfood is limited
    pygame.time.set_timer(DISAPPEAR_SUPER_FOOD_EVENT, seconds*1000)  # the time should be in milliseconds


def over_the_game():  # game over screen
    global game_over
    SCREEN.fill((69, 172, 116))
    SCREEN.blit(font.render('GAME OVER', True, WHITE), (30, 170))
    SCREEN.blit(font_small.render(f'Score: {SCORE}', True, WHITE), (32, 250))
    SCREEN.blit(font_small.render(f'Level: {LEVEL}', True, WHITE), (32, 275))
    pygame.display.update()
    time.sleep(6)
    game_over = True


for pos in POSITIONS_OF_THE_WALL:  # adding walls
    w = Wall(_position=pos, _length=random.randint(30, 30), _color=color_of_wall)
    w.construct()
    walls.append(w)

while not game_over:
    # print("iii")
    for event in pygame.event.get():
        if event.type == DISAPPEAR_SUPER_FOOD_EVENT:  # if disappear super coin event called
            super_food = None
        if event.type == pygame.QUIT:  # quit
            game_over = True
        if event.type == pygame.KEYDOWN:
            pressed = pygame.key.get_pressed()  # change the direction of snake motion
            if pressed[pygame.K_UP] and snake.dx != 0:  # snake can not rapidly start reverse motion
                snake.dy = -1 * snake.block
                snake.dx = 0
            if pressed[pygame.K_DOWN] and snake.dx != 0:
                snake.dy = snake.block
                snake.dx = 0
            if pressed[pygame.K_LEFT] and snake.dy != 0:
                snake.dy = 0
                snake.dx = -1 * snake.block
            if pressed[pygame.K_RIGHT] and snake.dy != 0:
                snake.dy = 0
                snake.dx = snake.block

    SCREEN.fill(WHITE)  # display all game actions
    snake.move()
    snake.draw()
    draw_grid()
    food.draw()
    if super_food:  # it may be absent
        super_food.draw()
    for w in walls:
        w.draw()

    # display the score and level
    SCREEN.blit(font_small.render(f'Score: {SCORE}', True, BLUE), (11, WINDOW_HEIGHT + 30))
    SCREEN.blit(font_small.render(f'Level: {LEVEL}', True, BLUE), (11, WINDOW_HEIGHT + 53))

    if snake.head_collide(food.particle):  # get food
        SCORE += 1
        snake.add_tail()
        food.set_random_position()

    if super_food:
        if snake.head_collide(super_food.particle):
            SCORE += 2
            snake.add_tail()  # twice increasing
            snake.add_tail()
            super_food = None

    if check_food_collision():  # food should not lay on wall or snake
        food.set_random_position()

    for tail in snake.body[1:]:  # game over if snake collide its body
        if snake.head_collide(tail):
            over_the_game()

    for w in walls:  # game over if snake collide the wall
        for part in w.construction:
            if snake.head_collide(part):
                over_the_game()

    if SCORE != 0:
        if SCORE % 5 == 0:  # if score is divisible by 5
            if not super_food_appeared:
                super_food_appeared = True
                super_food = SuperFood()
                super_food_disappears_after_some_seconds() # the time of existing superfood is limited
        if SCORE % 5 == 1:
            super_food_appeared = False

        if SCORE % 7 == 0:  # increasing level and speed if score is divisible by 7
            if not level_increased:
                level_increased = True
                LEVEL += 1
                FPS += 2
        elif SCORE % 7 == 1:
            level_increased = False

    pygame.display.update()  # updating the screen
    CLOCK.tick(FPS)

pygame.quit()