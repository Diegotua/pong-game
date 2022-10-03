from pickle import TRUE
from turtle import Screen
import pygame

pygame.init()

screen_width=500
screen_height=400

size =(screen_width,screen_height)

screen=pygame.display.set_mode(size)

running= True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False
            