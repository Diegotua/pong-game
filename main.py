
import pygame
import random as rd
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
player_1_y_speed=0
player_2_x=430
player_2_y=150
player_2_y_speed=0
ball_x=250
ball_y=200
ball_radius=20
ball_speed_x=0.1
ball_speed_y=0.1
pygame.display.set_caption("pong")
icon=pygame.image.load("ping-pong.png")
pygame.display.set_icon(icon)

running= True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:


            if event.key==pygame.K_w:
                player_1_y_speed=-0.2
                
            if event.key==pygame.K_s:
                player_1_y_speed=0.2
            
            if event.key==pygame.K_UP:
                player_2_y_speed=-0.2
                
            if event.key==pygame.K_DOWN:
                player_2_y_speed=0.2

        if event.type == pygame.KEYUP:


            if event.key==pygame.K_s:
                player_1_y_speed=0
                
            if event.key==pygame.K_s:
                player_1_y_speed=0
                
            if event.key==pygame.K_UP:
                player_2_y_speed=0
                
            if event.key==pygame.K_DOWN:
                player_2_y_speed=0

    player_1_y += player_1_y_speed
                    
    player_2_y += player_2_y_speed 

    ball_x +=ball_speed_x
    ball_y +=ball_speed_y

    if ball_y >(screen_height-ball_radius) or ball_y < ball_radius:
        ball_speed_y *= -1

    if ball_x>screen_width:
        ball_x = screen_width/2
        ball_y= screen_height/2
        ball_speed_x*= rd.choice([-1,1])

    elif ball_x <0:
        ball_x = screen_width/2
        ball_y= screen_height/2
        ball_speed_x*= rd.choice([-1,1])
       
    if player_1_y <=0:
        player_1_y=0

    if player_1_y >=screen_height - player_height:
        player_1_y = screen_height - player_height 

    
    if player_2_y <=0:
        player_2_y=0

    if player_2_y >=screen_height - player_height:
        player_2_y = screen_height - player_height          
    screen.fill(rgb)

    player_1=pygame.draw.rect(screen,players_colors,(player_1_x,player_1_y,player_width,player_height))

    player_2=pygame.draw.rect(screen,players_colors,(player_2_x,player_2_y,player_width,player_height))    
    pygame.draw.aaline(screen,line_color,(screen_width/2,0),(screen_width/2,screen_height))
    ball=pygame.draw.circle(screen,ball_color,(ball_x,ball_y),ball_radius)
    

    
    pygame.display.flip()                                                                                     