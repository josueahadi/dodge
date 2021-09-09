import pygame
import time
import random

pygame.init()

crash_sound = pygame.mixer.Sound("collision.ogg")
pygame.mixer.music.load("Jazz_In_Paris.ogg")

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 0, 0)
green = (0, 200, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
obstacle_colour = (53, 115, 255)

kart_width = 60
kart_height = 75

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Super Sprint Kart')
clock = pygame.time.Clock()

kartImg = pygame.image.load('AlphaKart.png')

pygame.display.set_icon(kartImg)

pause = False
# crashed = True


def obstacles_dodged(count):
    font = pygame.font.SysFont("comicsansms", 20)
    score = font.render("Score: "+str(count), True, black)
    gameDisplay.blit(score, (5, 0))

    # level = font.render("Level: " + str(count), True, black)
    # gameDisplay.blit(level, (10, 0))


def obstacles(obstaclex, obstacley, obstaclew, obstacleh, colour):
    pygame.draw.rect(gameDisplay, obstacle_colour, [obstaclex, obstacley, obstaclew, obstacleh])


def kart(x, y):
    gameDisplay.blit(kartImg, (x, y))


def text_objects(text, font):
    text_surface = font.render(text, True, black)
    return text_surface, text_surface.get_rect()


# def message_display(text):
#     # large_text = pygame.font.Font('freesansbold.ttf', 80)
#     large_text = pygame.font.SysFont("comicsansms", 115)
#     text_surf, text_rect = text_objects(text, large_text)
#     text_rect.center = ((display_width/2), (display_height/2))
#     gameDisplay.blit(text_surf, text_rect)
#
#     pygame.display.update()
#
#     time.sleep(2)
#
#     game_loop()


def crash():

    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)

    # large_text = pygame.font.Font('freesansbold.ttf', 80)
    large_text = pygame.font.SysFont("comicsansms", 80)
    text_surf, text_rect = text_objects("You Crashed!", large_text)
    text_rect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(text_surf, text_rect)

    while True:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame / quit()
                quit()

        # gameDisplay.fill(white)

        button("Play Again", 150, 450, 100, 50, green, bright_green, game_loop)
        button("Quit", 550, 450, 100, 50, red, bright_red, quit_game)

        pygame.display.update()
        clock.tick(15)


def button(msg, x, y, w, h, inactive_colour, active_colour, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    # print(click)

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, active_colour, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
            # if action == "play":
            #     game_loop()
            # elif action == "quit":
            #     pygame.quit()
            #     quit()
    else:
        pygame.draw.rect(gameDisplay, inactive_colour, (x, y, w, h))

    # small_text = pygame.font.Font('freesansbold.ttf', 20)
    small_text = pygame.font.SysFont("comicsansms", 20)
    text_surf, text_rect = text_objects(msg, small_text)
    text_rect.center = ((x + (w / 2)), y + (h / 2))
    gameDisplay.blit(text_surf, text_rect)


def quit_game():
    pygame.quit()
    quit()


def resume():
    global pause

    pygame.mixer.music.unpause()

    pause = False


def paused():

    pygame.mixer.music.pause()

    # large_text = pygame.font.Font('freesansbold.ttf', 80)
    large_text = pygame.font.SysFont("comicsansms", 80)
    text_surf, text_rect = text_objects("Paused", large_text)
    text_rect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(text_surf, text_rect)

    while pause:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame/quit()
                quit()

        # gameDisplay.fill(white)

        button("Resume", 150, 450, 100, 50, green, bright_green, resume)
        button("Quit", 550, 450, 100, 50, red, bright_red, quit_game)

        pygame.display.update()
        clock.tick(15)


def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame/quit()
                quit()

        gameDisplay.fill(white)
        # large_text = pygame.font.Font('freesansbold.ttf', 80)
        large_text = pygame.font.SysFont("comicsansms", 80)
        text_surf, text_rect = text_objects("Super Sprint Kart", large_text)
        text_rect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(text_surf, text_rect)

        button("Go!", 150, 450, 100, 50, green, bright_green, game_loop)
        button("Quit", 550, 450, 100, 50, red, bright_red, quit_game)

        pygame.display.update()
        clock.tick(15)


def game_loop():
    global pause

    pygame.mixer.music.play(-1)  # indefinite

    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0
    y_change = 0

    obstacle_startx = random.randrange(0, display_width)
    obstacle_starty = -600
    obstacle_speed = 5
    obstacle_width = 100
    obstacle_height = 100

    score = 0
    # level = 1

    game_exit = False

    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -8
                if event.key == pygame.K_RIGHT:
                    x_change = 8
                if event.key == pygame.K_a:
                    x_change = -8
                if event.key == pygame.K_d:
                    x_change = 8
                if event.key == pygame.K_w:
                    y_change = -8
                if event.key == pygame.K_s:
                    y_change = 8
                if event.key == pygame.K_p:
                    pause = True
                    paused()
                elif event.key == pygame.K_SPACE:
                    pause = True
                    paused()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    x_change = 0
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    y_change = 0

        x += x_change
        y += y_change

        gameDisplay.fill(white)

        # obstacles(obstaclex, obstacley, obstaclew, obstacleh, colour)
        obstacles(obstacle_startx, obstacle_starty, obstacle_width, obstacle_height, obstacle_colour)
        obstacle_starty += obstacle_speed
        kart(x, y)

        obstacles_dodged(score)
        # obstacles_dodged(level)

        if x > display_width - kart_width or x < 0:
            # game_exit = True
            crash()
        if y > display_height - kart_height or y < 0:
            y_change = 0

        if obstacle_starty > display_height:
            obstacle_starty = 0 - obstacle_height
            obstacle_startx = random.randrange(0, display_width)

            score += 1
            obstacle_speed += 0.1
            obstacle_width += (score * 0.01)

        if y < obstacle_starty+obstacle_height:
            # print('y crossover')

            if obstacle_startx < x < obstacle_startx+obstacle_width or obstacle_startx < x+kart_width < obstacle_startx+obstacle_width:
                # print('x crossover')
                crash() 

        pygame.display.update()
        clock.tick(60)


game_intro()
game_intro()
game_loop()
pygame.quit()
quit()
