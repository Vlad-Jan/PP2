import pygame

pygame.init()
screen = pygame.display.set_mode((800 , 800))

ballpos = [400 , 400] 

speed =20

running = True
while running :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
             ballpos[1] -= speed
            elif event.key == pygame.K_DOWN:
                ballpos[1] += speed
            elif event.key == pygame.K_LEFT:
                ballpos[0] -= speed
            elif event.key == pygame.K_RIGHT:
                ballpos[0] += speed

        if ballpos[0] - 25 < 0:
            ballpos[0] = 25
        elif ballpos[0] + 25 > 800:
            ballpos[0] = 800 - 25
        if ballpos[1] - 25 < 0:
         ballpos[1] = 25
        elif ballpos[1] + 25 > 800:
            ballpos[1] = 800 - 25

    ballpos[0] = max(25, min(800 - 25, ballpos[0]))
    ballpos[1] = max(25, min(800 - 25, ballpos[1]))

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, 'Red', ballpos, 25)
    pygame.display.update()