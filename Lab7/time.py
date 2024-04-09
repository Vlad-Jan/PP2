import pygame 
from datetime import datetime
pygame.init()

width , height = 800 , 800
x = width//2
y = height//2
white = (255 ,255 , 255)
screen = pygame.display.set_mode((width, height))

mickey = pygame.image.load("mikkey.jpg") 
leftHand = pygame.image.load("left.png") 
rightHand = pygame.image.load("right.png")
mickeyRect = mickey.get_rect() 

def rotcent (surf , image , center , angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect =  rotated_image.get_rect(center = image.get_rect(center = center).center)
    surf.blit(rotated_image , new_rect)

current_datetime = datetime.now()
current_datetime = datetime.now()
second = 78 - current_datetime.second*6
minute = 78 - current_datetime.minute*6

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    second -= 0.099
    minute -= 0.00165

    screen.fill(white)
    screen.blit(mickey,(x , y))
    screen.blit(mickey , mickeyRect)


    rotcent(screen , leftHand , (x , y) , second)
    rotcent(screen , rightHand , (x , y) , minute)
    pygame.display.update()