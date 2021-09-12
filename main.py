import pygame
import time
import random

pygame.init()  # initiate pygame

display_width = 800
display_height = 600 

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

car_width = 60

gameDisplay = pygame.display.set_mode((display_width, display_height))  # passed a tuple to avoid fnc from treating w&h as separate params
pygame.display.set_caption('Dodge')
clock = pygame.time.Clock()

carImg = pygame.image.load('assets/racecar-000.png')
obstacleCarImg = pygame.image.load('assets/racecar-001.png')

# def lanes(lanex, laney, lanew, laneh, color):
#     pygame.draw.rect(gameDisplay, color, [lanex, laney, lanew, laneh])

def obstaclecars(obstaclex, obstacley, obstaclew, obstacleh):
    gameDisplay.blit(obstacleCarImg, (obstaclex, obstacley))

def maincar(x, y):
    gameDisplay.blit(carImg, (x, y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurface, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurface, TextRect)

    pygame.display.update()
    
    time.sleep(2)

    game_loop()

def crash():
    message_display('You crashed')

def game_loop():

    x = (display_width*0.45)
    y = (display_height*0.8)

    x_change = 0

    # lane_start_x = random.randrange(0,display_width) 
    # lane_start_y = -600
    # lane_speed = 7
    # lane_width = 10
    # lane_height = 60
    
    obstacle_startx = random.randrange(0,display_width)
    obstacle_starty = -600 
    obstacle_speed = 7
    obstacle_width = 60
    obstacle_height = 75


    gameExit = False

    # EVENT LOOP 

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            # print(event)  # event log

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0


        x += x_change 

        gameDisplay.fill(white)

        # lanes(lane_start_x, lane_start_y, lane_width, lane_height, black)
        # lane_start_y += lane_speed

        obstaclecars(obstacle_startx, obstacle_starty, obstacle_width, obstacle_height)

        obstacle_starty += obstacle_speed

        maincar(x,y)

        if x > display_width - car_width or x < 0:
            crash()

        if obstacle_starty > display_height:
            obstacle_starty = 0 - obstacle_height 
            obstacle_startx = random.randrange(0,display_width)
        
        if y < obstacle_starty + obstacle_height:
            print('y crossover')

            if x > obstacle_startx and x < obstacle_startx + obstacle_width or x + car_width > obstacle_startx and x + car_width < obstacle_startx + obstacle_width:
                print('x crossover')
                crash()

        # if lane_start_y > display_height:
        #     lane_start_y = 0 - lane_height
        #     lane_start_y = random.randrange(0,display_width)


        pygame.display.update() # or flip()
        clock.tick(60)  # Update .. FPS

game_loop()
pygame.quit()  # uninitiate pygame when the user wants to quit
quit()
