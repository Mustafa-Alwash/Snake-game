import pygame
from sys import exit
from random import randint

cell_size=30
cell_num=30

class fruit:
    def __init__(self):
        self.x = randint(0,(cell_num -1))
        self.y = randint(0,(cell_num -1))
        self.pos = pygame.Vector2(self.x,self.y)
    def make_fruit(self):
        fruit_rect=pygame.Rect(self.pos.x*cell_size,self.pos.y*cell_size,cell_size,cell_size)
        pygame.draw.rect(screen,(126,166,114),fruit_rect)
    def eaten(self):
        self.x = randint(0,(cell_num)-1)
        self.y = randint(0,(cell_num) -1)
        self.pos = pygame.Vector2(self.x,self.y)

class snake:
    def __init__(self):
        self.body = [pygame.Vector2(5,10),pygame.Vector2(4,10),pygame.Vector2(3,10)]
        self.direction = pygame.Vector2(0,1)
        self.vectors = self.body[:-1]
        self.cond = False
    def make_snake(self):
        for i in self.body:
            snake_rect = pygame.Rect(i.x*cell_size,i.y*cell_size,cell_size,cell_size)
            pygame.draw.rect(screen,(183,111,122),snake_rect)
    def moving_snake(self):
        if self.cond ==True :
            self.vectors = self.body[:]
            self.vectors.insert(0,self.vectors[0] + self.direction)
            self.body = self.vectors[:]
            self.cond = False
        else:
            self.vectors = self.body[:-1]
            self.vectors.insert(0,self.vectors[0] + self.direction)
            self.body = self.vectors[:]
    def inserting_bolck(self):
        self.cond = True
    def restart(self):
        self.body = [pygame.Vector2(5,10),pygame.Vector2(4,10),pygame.Vector2(3,10)]



class MAIN:
    def __init__(self) -> None:
        self.Fruit = fruit()
        self.Snake=snake()
        self.crunch=pygame.mixer.Sound('/Users/mustafaalwash/Documents/Snake-game/apple_bite.mp3')
        self.laugh = pygame.mixer.Sound('/Users/mustafaalwash/Documents/Snake-game/laughter.mp3')
    def update(self):
        self.Snake.moving_snake()
        self.eating()
        self.lose()
    def drawing(self):
        self.Fruit.make_fruit()
        self.Snake.make_snake()
    def eating(self):
        if self.Fruit.pos == self.Snake.body[0]:
            self.Fruit.eaten()
            self.Snake.inserting_bolck()
            self.crunch.play()
        for what in self.Snake.body[1:]:
            if what == self.Fruit.pos:
                self.Fruit.eaten()

    def lose(self):
        if not 0 <= self.Snake.body[0].x < cell_num or not 0 <= self.Snake.body[0].y < cell_num:
            self.laugh.play()
            self.Snake.restart()
        for z in self.Snake.body[1:]:
            if z == self.Snake.body[0]:
                self.laugh.play()
                self.Snake.restart()

    
    
pygame.mixer.pre_init(44100,-16,2,512)    
pygame.init() 

screen_update = pygame.USEREVENT
pygame.time.set_timer(screen_update,100)

screen = pygame.display.set_mode((cell_size *cell_num,cell_size*cell_num))
clock = pygame.time.Clock()

main =MAIN()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == screen_update:
            main.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main.Snake.direction.y != 1:
                    main.Snake.direction =pygame.Vector2(0,-1)
            if event.key == pygame.K_LEFT:
                if main.Snake.direction.x != 1:
                    main.Snake.direction =pygame.Vector2(-1,0)      
            if event.key == pygame.K_RIGHT:
                if main.Snake.direction.x != -1:
                    main.Snake.direction =pygame.Vector2(1,0)   
            if event.key == pygame.K_DOWN:
                if main.Snake.direction.y != -1:
                    main.Snake.direction =pygame.Vector2(0,1)      
   

    screen.fill((175,215,70))

    main.drawing()
 
    pygame.display.update()
    clock.tick(60)