
import pygame

pygame.init()
rgb=(21, 28, 96 )
players_colors=(48, 96, 21 )
ball_color=(21, 96, 91 )
line_color=(0,0,0)
screen_width=500
screen_height=400

size =(screen_width,screen_height)

screen=pygame.display.set_mode(size)
player_width=15
player_height=90
player_1_x=50
player_1_y=150
player_2_x=430
player_2_y=150
ball_x=250
ball_y=200
ball_radius=20

pygame.display.set_caption("pong")
icon=pygame.image.load("ping-pong.png")
pygame.display.set_icon(icon)

running= True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False

    screen.fill(rgb)

    player_1=pygame.draw.rect(screen,players_colors,(player_1_x,player_1_y,player_width,player_height))

    player_2=pygame.draw.rect(screen,players_colors,(player_2_x,player_2_y,player_width,player_height))    
    pygame.draw.aaline(screen,line_color,(screen_width/2,0),(screen_width/2,screen_height))
    ball=pygame.draw.circle(screen,ball_color,(ball_x,ball_y),ball_radius)

    
    pygame.display.flip()

 