#Imports
import pygame
from pygame import *

#Screen Dimensions

WIN_WIDTH = 768
WIN_HEIGHT = 672

#Screen Defaults

black = (0,0,0)
white = (255,255,255)
skyblue = (176,228,245)
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
DEPTH = 32
FLAGS = 0

#Spritesheet

spritesheet = pygame.image.load("resources\Textures\Player\America\maindummy.png")

#Main Function

def main():
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY, FLAGS, DEPTH)
    pygame.display.set_caption("Sprite Mapper")
    x = y = 0
    w = h = 100
    pygame.key.set_repeat(1,30)
    f = open("test.txt","w")
    f.close()

    while 1:
        for e in pygame.event.get():
            if e.type == QUIT: raise SystemExit, "QUIT"
            if e.type == KEYDOWN and e.key == K_ESCAPE:
                raise SystemExit, "ESCAPE"
            if e.type == KEYDOWN and e.key == K_DOWN:
                y = y - 1
            if e.type == KEYDOWN and e.key == K_UP:
                y = y + 1
            if e.type == KEYDOWN and e.key == K_RIGHT:
                x = x - 1
            if e.type == KEYDOWN and e.key == K_LEFT:
                x = x + 1
            if e.type == KEYDOWN and e.key == K_w:
                h = h - 1
            if e.type == KEYDOWN and e.key == K_s:
                h = h + 1
            if e.type == KEYDOWN and e.key == K_a:
                w = w - 1
            if e.type == KEYDOWN and e.key == K_d:
                w = w + 1
            if e.type == KEYDOWN and e.key == K_SPACE:
                name = raw_input("Name of Sprite?")
                
                f = open("test.txt","a")
                
                savedcode = "character = Surface((" + str(w) + "," + str(h) + "),pygame.SRCALPHA)" + "\n"
                f.write(savedcode)

                savedcode = "character.blit(spritesheet,(" + str(x) + "," + str(y) + "))" + "\n"
                f.write(savedcode)

                savedcode = "character = pygame.transform.scale(character, (" + str(w) + "*3," + str(h) + "*3))" + "\n"
                f.write(savedcode)

                savedcode = name + " = character" + "\n" + "\n"
                f.write(savedcode)

                f.close()
                
        screen.fill(Color("black"))
        
        character = Surface((w,h))
        character.fill(Color("#FFFFFF"))
        
        character.blit(spritesheet,(x,y))
        character = pygame.transform.scale(character,(w*4,h*4))
        screen.blit(character,(0,0))
        
        pygame.display.update()

if __name__ == "__main__":
    main()
