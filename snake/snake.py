import pygame
import numpy as np
import time
import random

pygame.init()

dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width,dis_height))
pygame.display.update()
pygame.display.set_caption('Snake Adaptation')

blue = (0,0,255)
red = (255,0,0)

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)




x1 = dis_width/2
y1 = dis_height/2

snake_block = 10

x1_change = 0
y1_change = 0

clock = pygame.time.Clock()
snake_speed = 30

font_style = pygame.font.SysFont(None,50)

def message(msg, color):
    msg = font_style.render(msg, True, color)
    dis.blit(msg, [dis_width/3, dis_height/3])


def gameloop():

    game_over = False
    game_close = False

    x1 = dis_width/2
    y1 = dis_height/2

    x1_change = 0
    y1_change = 0

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0)* 10.0
    foody = round(random.randrange(0, dis_width - snake_block )  /10.0) * 10.0
    

    while(not game_over):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over=True
            
            if event.type  == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if (x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0):
            game_over = True

            
        x1 += x1_change
        print( x1_change)
        y1 += y1_change
        print(y1_change)
        dis.fill(white)

        # print(dis, blue, [foodx, foody])
        # pygame.draw.rect(dis, blue, [foodx, foody])
        # pygame.draw.rect(dis, black, [x1, y1, 10, 10])

        pygame.display.update()

        clock.tick(snake_speed)


gameloop()

message("You Lost", red)
pygame.display.update()
time.sleep(2)
    
pygame.quit()
quit()