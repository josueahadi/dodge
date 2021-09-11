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
otherCarImg = pygame.image.load('assets/racecar-001.png')

def lanes(lanex, laney, lanew, laneh, color):
    pygame.draw.rect(gameDisplay, color, [lanex, laney])

def othercars(carx, cary, carw, carh):
    gameDisplay.blit(otherCarImg, (carx, cary))

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

    lane_start_x = random.randrange(0,display_width) 
    lane_start_y = -600
    lane_speed = 7
    lane_width = 2  
    lane_height = 100
    
    car_start_x = random.randrange(0,display_width)
    car_start_y = -600 
    car_speed = 7
    car_width = 60
    car_height = 75


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

        lanes(lane_start_x, lane_start_y, lane_width, lane_height, black)
        lane_start_y += lane_speed

        othercars(car_start_x, car_start_y, car_width, car_height)

        car_start_y += car_speed

        maincar(x,y)

        if x > display_width - car_width or x < 0:
            crash()
        if car_start_y > display_height:
            car_start_y = 0 - car_height 
            car_start_x = random.randrange(0,display_width)


        pygame.display.update() # or flip()
        clock.tick(60)  # Update .. FPS

game_loop()
pygame.quit()  # uninitiate pygame when the user wants to quit
quit()
