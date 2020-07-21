
import pygame, sys
from pygame import *
import ctypes
init()
WIN_WIDTH =  1366
WIN_HEIGHT = 728


HALF_WIDTH = int(WIN_WIDTH / 2)
HALF_HEIGHT = int(WIN_HEIGHT / 2)
DISPLAY = (HALF_WIDTH, HALF_HEIGHT)
DEPTH = 32

user32 = ctypes.windll.user32
screenSize = WIN_WIDTH, WIN_HEIGHT
size = (screenSize)
screen = display.set_mode(size)

FLAGS = 0
CAMERA_SLACK = 30
black = (0,0,0)
skyblue = (176,228,245)
blue = (0,0,255)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)

bigfont = pygame.font.Font(None, 80)
smallfont = pygame.font.Font(None, 45)
betterfont = pygame.font.Font(None, 22)

#Sprite Loading#

spritesheet = pygame.image.load("resources\Textures\Player\America\maindummy.png")

character = Surface((16,32),pygame.SRCALPHA)
character.blit(spritesheet,(0,0))
character = pygame.transform.scale(character, (16*3,32*3))
dummystand1 = character

character = Surface((16,32),pygame.SRCALPHA)
character.blit(spritesheet,(-30,0))
character = pygame.transform.scale(character, (16*3,32*3))
dummywalk1 = character

character = Surface((12,31),pygame.SRCALPHA)
character.blit(spritesheet,(-62,0))
character = pygame.transform.scale(character, (12*3,31*3))
dummywalk2 = character

character = Surface((16,31),pygame.SRCALPHA)
character.blit(spritesheet,(-90,0))
character = pygame.transform.scale(character, (16*3,31*3))
dummywalk3 = character

character = Surface((16,32),pygame.SRCALPHA)
character.blit(spritesheet,(-120,0))
character = pygame.transform.scale(character, (16*3,32*3))
dummyjump1 = character


spritesheet2 = pygame.image.load("resources\Textures\Entities\Snowman\schneemann.png")

character = Surface((15,32),pygame.SRCALPHA)
character.blit(spritesheet2,(0,0))
character = pygame.transform.scale(character, (15*3,32*3))
schneemannstand1 = character

character = Surface((15,30),pygame.SRCALPHA)
character.blit(spritesheet2,(-30,0))
character = pygame.transform.scale(character, (15*3,30*3))
schneemannwalk1 = character

character = Surface((16,29),pygame.SRCALPHA)
character.blit(spritesheet2,(-58,0))
character = pygame.transform.scale(character, (16*3,29*3))
schneemannwalk2 = character

character = Surface((17,29),pygame.SRCALPHA)
character.blit(spritesheet2,(-84,0))
character = pygame.transform.scale(character, (17*3,29*3))
schneemannwalk3 = character

character = Surface((17,27),pygame.SRCALPHA)
character.blit(spritesheet2,(-113,0))
character = pygame.transform.scale(character, (17*3,27*3))
schneemannjump1 = character


spritesheet3 = pygame.image.load("resources\Textures\Entities\Flury\JEDIFLURY.png")

character = Surface((14,31),pygame.SRCALPHA)
character.blit(spritesheet3,(0,-1))
character = pygame.transform.scale(character, (14*3,31*3))
flurystand1 = character

character = Surface((16,31),pygame.SRCALPHA)
character.blit(spritesheet3,(-30,-1))
character = pygame.transform.scale(character, (16*3,31*3))
flurywalk1 = character

character = Surface((16,31),pygame.SRCALPHA)
character.blit(spritesheet3,(-60,-1))
character = pygame.transform.scale(character, (16*3,31*3))
flurywalk2 = character

character = Surface((16,31),pygame.SRCALPHA)
character.blit(spritesheet3,(-90,-1))
character = pygame.transform.scale(character, (16*3,31*3))
flurywalk3 = character

character = Surface((13,31),pygame.SRCALPHA)
character.blit(spritesheet3,(-121,-1))
character = pygame.transform.scale(character, (13*3,31*3))
fluryjump1 = character


spritesheet4 = pygame.image.load("resources\Textures\Entities\Mario\mariosheet.png")

character = Surface((16,32),pygame.SRCALPHA)
character.blit(spritesheet4,(-209,-52))
character = pygame.transform.scale(character, (16*3,32*3))
mariostand1 = character

character = Surface((16,32),pygame.SRCALPHA)
character.blit(spritesheet4,(-239,-52))
character = pygame.transform.scale(character, (16*3,32*3))
mariowalk1 = character

character = Surface((16,32),pygame.SRCALPHA)
character.blit(spritesheet4,(-269,-51))
character = pygame.transform.scale(character, (16*3,32*3))
mariowalk2 = character

character = Surface((16,32),pygame.SRCALPHA)
character.blit(spritesheet4,(-299,-51))
character = pygame.transform.scale(character, (16*3,32*3))
mariowalk3 = character

character = Surface((16,32),pygame.SRCALPHA)
character.blit(spritesheet4,(-359,-52))
character = pygame.transform.scale(character, (16*3,32*3))
mariojump1 = character


spritesheet5 = pygame.image.load("resources\Textures\Entities\Soldier\soldiersheet.png")
                               
character = Surface((28,31),pygame.SRCALPHA)
character.blit(spritesheet5,(-3,0))
character = pygame.transform.scale(character, (28*3,32*3))
soldierstand1 = character

character = Surface((25,32),pygame.SRCALPHA)
character.blit(spritesheet5,(-37,0))
character = pygame.transform.scale(character, (25*3,32*3))
soldierwalk1 = character

character = Surface((12,32),pygame.SRCALPHA)
character.blit(spritesheet5,(-74,0))
character = pygame.transform.scale(character, (12*3,32*3))
soldierwalk2 = character

character = Surface((25,32),pygame.SRCALPHA)
character.blit(spritesheet5,(-101,0))
character = pygame.transform.scale(character, (25*3,32*3))
soldierwalk3 = character

character = Surface((27,32),pygame.SRCALPHA)
character.blit(spritesheet5,(-129,-1))
character = pygame.transform.scale(character, (27*3,32*3))
soldierjump1 = character


spritesheet6 = pygame.image.load("resources\Textures\Entities\Joel\joelsheet.png")

character = Surface((16,32),pygame.SRCALPHA)
character.blit(spritesheet6,(-8,0))
character = pygame.transform.scale(character, (16*3,32*3))
joelstand1 = character

character = Surface((16,32),pygame.SRCALPHA)
character.blit(spritesheet6,(-41,0))
character = pygame.transform.scale(character, (16*3,32*3))
joelwalk1 = character

character = Surface((16,32),pygame.SRCALPHA)
character.blit(spritesheet6,(-72,0))
character = pygame.transform.scale(character, (16*3,32*3))
joelwalk2 = character

character = Surface((13,32),pygame.SRCALPHA)
character.blit(spritesheet6,(-105,0))
character = pygame.transform.scale(character, (13*3,32*3))
joelwalk3 = character

character = Surface((16,32),pygame.SRCALPHA)
character.blit(spritesheet6,(-138,0))
character = pygame.transform.scale(character, (16*3,32*3))
joeljump1 = character



def main():
    global cameraX, cameraY
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode(DISPLAY, FLAGS, DEPTH)
    pygame.display.set_caption("JCLT Game")
    Timer = pygame.time.Clock()
    pygame.display.set_mode(size, FULLSCREEN)
    bg = Surface((32, 32))
    up = down = left = right = running = False
    bg = Surface((WIN_WIDTH,WIN_HEIGHT)).convert_alpha()
    bg.fill(Color("skyblue"))
    screen.blit(bg, [0,0])
    entities = pygame.sprite.Group()
    player = Player(16*3,16*3)
    platforms = []
    

    x = y = 0
    level = [

        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "P                                                                  P",
        "P                                                                  P",
        "P                                                                  P",
        "P                                                                  P",
        "P                                                                  P",
        "P                                                                  P",
        "P                                                                  P",
        "P                                                                  P",
        "P                                                                  P",
        "P                                                                  P",
        "P                                                                  P",
        "P                                                                  P",
        "P                                                                  P",
        "P                                                         PP       P",
        "P                                                       PP  P      P",
        "P                                                      PP   P      P",
        "P                                                    PP     P      P",
        "P                                                  PP       P      P",
        "P                                               PP          P      P",
        "P                                            PP             P      P",
        "P                                        PP                 P      P",
        "P                    PP   PP   PP   PP                      P      PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "P               PP                                          P                                                       P",                  
        "P          PP                                               P                                                       P",
        "P      PP                                                   P                                                       P",
        "P   PP                                                      P                                                       P",
        "PPPP  GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGPPPPPPPPPPPPPPPPPGGGGPPPPPPPPPPPPPPGGGGPPPPPPPPPPPPPPPPPPPPPPPPEP",]
    
    #build the level#
    for row in level:
        for col in row:
            if col == "P":
                p = Platform(x, y)
                platforms.append(p)
                entities.add(p)
            if col == "E":
                e = ExitBlock(x, y)
                platforms.append(e)
                entities.add(e)
            if col == "R":
                p = Rgspikes(x, y)
                platforms.append(p)
                entities.add(p)
            if col == "L":
                p = Lgspikes(x, y)
                platforms.append(p)
                entities.add(p)
            if col == "U":
                p = Upleftspikes(x, y)
                platforms.append(p)
                entities.add(p)
            if col == "I":
                p = Uprightspikes(x, y)
                platforms.append(p)
                entities.add(p)
            if col == "D":
                p = Downallaroundspikes(x, y)
                platforms.append(p)
                entities.add(p)
            if col == "T":
                p = Leftspikes(x, y)
                platforms.append(p)
                entities.add(p)
            if col == "Z":
                p = Rightspikes(x, y)
                platforms.append(p)
                entities.add(p)
            if col == "G":
                p = Groundspikes(x, y)
                platforms.append(p)
                entities.add(p)
            if col == "S":
                b = SpecialBlock(x, y)
                platforms.append(b)
                entities.add(b)
            if col == "J":
                b = Downaroundspikesl(x, y)
                platforms.append(b)
                entities.add(b)
            if col == "K":
                b = Downaroundspikesr(x, y)
                platforms.append(b)
                entities.add(b)
            if col == "M":
                m = Allaroundspikes(x, y)
                platforms.append(m)
                entities.add(m)
            if col == "N":
                N = Downspikes(x, y)
                platforms.append(N)
                entities.add(N)
            if col == "C":
                c = Trollblock(x, y)
                platforms.append(c)
                entities.add(c)

            x += 16*3
        y += 16*3
        x = 0



    total_level_width  = len(level[0])*32*3
    total_level_height = len(level)*32*3
    camera = Camera(complex_camera, total_level_width, total_level_height)
    entities.add(player)

    

        
    while 1:
        Timer.tick(60)


        for e in pygame.event.get():
            if e.type == KEYDOWN and e.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if e.type == KEYDOWN and e.key == K_UP:
                up = True
            if e.type == KEYDOWN and e.key == K_LEFT:
                left = True
            if e.type == KEYDOWN and e.key == K_RIGHT:
                right = True
            if e.type == KEYUP and e.key == K_UP:
                up = False
            if e.type == KEYUP and e.key == K_DOWN:
                down = False
            if e.type == KEYUP and e.key == K_RIGHT:
                right = False
            if e.type == KEYUP and e.key == K_LEFT:
                left = False
            if e.type == KEYDOWN and e.key == K_w:
                up = True
            if e.type == KEYDOWN and e.key == K_s:
                down = True
            if e.type == KEYDOWN and e.key == K_a:
                left = True
            if e.type == KEYDOWN and e.key == K_d:
                right = True
            if e.type == KEYUP and e.key == K_w:
                up = False
            if e.type == KEYUP and e.key == K_s:
                down = False
            if e.type == KEYUP and e.key == K_d:
                right = False
            if e.type == KEYUP and e.key == K_a:
                left = False
            if e.type == KEYDOWN and e.key == K_r:
                main()
            

        

        
        screen.blit(bg,(0,0))

        camera.update(player)

        # update player, draw everything else#
        player.update(up, down, left, right, running, platforms)
        for e in entities:
            screen.blit(e.image, camera.apply(e))

        
            

        pygame.display.update()

class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)

def simple_camera(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    return Rect(-l+HALF_WIDTH, -t+HALF_HEIGHT, w, h)

def complex_camera(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t, _, _ = -l+HALF_WIDTH, -t+HALF_HEIGHT, w, h

    l = min(0, l)                           #stop scrolling at the left edge#
    l = max(-(camera.width-WIN_WIDTH), l)   #stop scrolling at the right edge#
    t = max(-(camera.height-WIN_HEIGHT), t) #stop scrolling at the bottom#
    t = min(0, t)                           #stop scrolling at the top#
    return Rect(l, t, w, h)

class Entity(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

class Player(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.xvel = 0
        self.yvel = 0
        self.faceright = True
        self.onGround = False
        self.airborne = True
        self.counter = 0
        self.image = dummystand1
        self.rect = Rect(x, y, 16*3,32*3)
        
    def update(self, up, down, left, right, running, platforms):
        if up:
            #only jump if on the ground#
            if self.onGround: self.yvel -= 6.5
        if down:
            pass
        if running:
            self.xvel = 12
        if left:
            self.xvel = -9
            self.faceright = False
        if right:
            self.xvel = 9
            self.faceright = True
        if not self.onGround:
            #only accelerate with gravity if in the air#
            self.yvel += 0.4
            #max falling speed#
            if self.yvel > 100: self.yvel = 100
        if not(left or right):
            self.xvel = 0
        if self.yvel < 0 or self.yvel > 1.2: self.airborne = True
        #increment in x direction#
        self.rect.left += self.xvel
        # do x-axis collisions
        self.collide(self.xvel, 0, platforms)
        #increment in y direction#
        self.rect.top += self.yvel
        #assuming we're in the air#
        self.onGround = False;
        #do y-axis collisions#
        self.collide(0, self.yvel, platforms)

        self.animate()

        
    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if isinstance(p, ExitBlock):
                    normal_end()
                    pygame.display.quit()
                    sys.exit()
                if isinstance(p, Groundspikes):
                    pygame.time.delay(100)
                    play_again()
                    main()
                if isinstance(p, Rgspikes):
                    play_again()
                    main()
                if isinstance(p, Lgspikes):
                    play_again()
                    main()
                if isinstance(p, Uprightspikes):
                    play_again()
                    main()
                if isinstance(p, Upleftspikes):
                    play_again()
                    main()
                if isinstance(p, Downallaroundspikes):
                    play_again()
                    main()
                if isinstance(p, Leftspikes):
                    play_again()
                    main()
                if isinstance(p, Rightspikes):
                    play_again()
                    main()
                if isinstance(p, SpecialBlock):
                    special_end()
                    pygame.quit()
                    sys.exit()
                if isinstance(p, Downaroundspikesl):
                    play_again()
                    main()
                if isinstance(p, Downaroundspikesr):
                    play_again()
                    main()
                if isinstance(p, Allaroundspikes):
                    play_again()
                    main()
                if isinstance(p, Downspikes):
                    play_again()
                    main()
                if xvel > 0:
                    self.rect.right = p.rect.left
                if xvel < 0:
                    self.rect.left = p.rect.right
                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.airborne = False
                    self.yvel = 0
                if yvel < 0:
                    self.rect.top = p.rect.bottom
    def animate(self):

        if self.xvel > 0 or self.xvel < 0:
            self.walkloop()
            if self.airborne: self.updatecharacter(dummyjump1)
        else:
            self.updatecharacter(dummystand1)
            if self.airborne: self.updatecharacter(dummyjump1)

    def walkloop(self):
        if self.counter == 5:
            self.updatecharacter(dummywalk3)
        elif self.counter == 10:
            self.updatecharacter(dummywalk2)
        elif self.counter == 15:
            self.updatecharacter(dummywalk1)
            self.counter = 0
        self.counter = self.counter + 1

    def updatecharacter(self, ansurf):
        if not self.faceright: ansurf = pygame.transform.flip(ansurf,True,False)
        self.image = ansurf



class Platform(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = pygame.image.load("resources\Textures\Platforms\Block.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(16*3,16*3))
        self.rect = Rect(x, y, 16*3, 16*3)
        
    def update(self):
        pass    

class CBlock(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = pygame.image.load("resources\Textures\Platforms\CBlock.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(16*3,16*3))
        self.rect = Rect(x, y, 16*3, 16*3)
                         
class Groundspikes(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = pygame.image.load("resources\Textures\Platforms\Groundspikes.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(16*3,16*3))
        self.rect = Rect(x, y, 16*3, 16*3)
        
class Lgspikes(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = pygame.image.load("resources\Textures\Platforms\Lgspikes.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(16*3, 16*3))
        self.rect = Rect(x, y, 16*3, 16*3)

class Rgspikes(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = pygame.image.load("resources\Textures\Platforms\Rgspikes.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(16*3, 16*3))
        self.rect = Rect(x, y, 16*3, 16*3)
        
class ExitBlock(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = pygame.image.load("resources\Textures\Platforms\Greenblock.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(16*3,16*3))
        self.rect = Rect(x, y, 16*3, 16*3)

class Uprightspikes(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = pygame.image.load("resources\Textures\Platforms\Uparoundspikesr.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(16*3, 16*3))
        self.rect = Rect(x, y, 16*3, 16*3)

class Upleftspikes(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = pygame.image.load("resources\Textures\Platforms\Uparoundspikesl.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(16*3, 16*3))
        self.rect = Rect(x, y, 16*3, 16*3)
        
class Downallaroundspikes(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = pygame.image.load("resources\Textures\Platforms\Downallaroundspikes.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(16*3, 16*3))
        self.rect = Rect(x, y, 16*3, 16*3)

class Rightspikes(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = pygame.image.load("resources\Textures\Platforms\Spikesl.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(16*3, 16*3))
        self.rect = Rect(x, y, 16*3, 16*3)

class Leftspikes(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = pygame.image.load("resources\Textures\Platforms\Spikesr.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(16*3, 16*3))
        self.rect = Rect(x, y, 16*3, 16*3)

class SpecialBlock(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = pygame.image.load("resources\Textures\Platforms\CBlock.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(16*3, 16*3))
        self.rect = Rect(x, y, 16*3, 16*3)

class Downaroundspikesl(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = pygame.image.load("resources\Textures\Platforms\Downaroundspikesl.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(16*3, 16*3))
        self.rect = Rect(x, y, 16*3, 16*3)

class Downaroundspikesr(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = pygame.image.load("resources\Textures\Platforms\Downaroundspikesr.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(16*3, 16*3))
        self.rect = Rect(x, y, 16*3, 16*3)

class Allaroundspikes(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = pygame.image.load("resources\Textures\Platforms\Allaroundspikes.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(16*3, 16*3))
        self.rect = Rect(x, y, 16*3, 16*3)        

class Downspikes(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = pygame.image.load("resources\Textures\Platforms\Downspikes.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(16*3, 16*3))
        self.rect = Rect(x, y, 16*3, 16*3)

class Trollblock(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = pygame.image.load("resources\Textures\Platforms\Block.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(16*3, 16*3))
        self.rect = Rect(x, y, 0*3, 0*3)





def play_again():
    text = bigfont.render("You died.Try again?", 13, (red))
    textx = 1366 - text.get_width()
    texty = 728 - text.get_height()
    textx_size = text.get_width()
    texty_size = text.get_height()
    pygame.draw.rect(screen, (black), ((textx + 60, texty + 60),
                                               (textx_size + 60, texty_size + 60)))
    screen.blit(text, (WIN_WIDTH / 2 - text.get_width() / 2,
                       WIN_HEIGHT / 2 - text.get_height() / 2))
    clock = pygame.time.Clock()
    pygame.display.flip()
    in_main_menu = True
    while in_main_menu:
        clock.tick(50)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                in_main_menu = False
                main()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                if x >= textx - 1000 and x <= textx + textx_size + 1000:
                    if y >= texty - 1000 and y <= texty + texty_size + 1000:
                         in_main_menu = False
                         break

def normal_end():
    text = bigfont.render("level complete", 13, (0, 0, 0))
    textx = WIN_WIDTH - text.get_width()
    texty = WIN_HEIGHT - text.get_height()
    textx_size = text.get_width()
    texty_size = text.get_height()
    pygame.draw.rect(screen, (skyblue), ((textx + 60, texty + 60),
                                               (textx_size + 60, texty_size + 60)))
    screen.blit(text, (WIN_WIDTH / 2 - text.get_width() / 2,
                       WIN_HEIGHT / 2 - text.get_height() / 2))
    clock = pygame.time.Clock()
    pygame.display.flip()
    in_main_menu = True
    while in_main_menu:
        clock.tick(50)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                in_main_menu = False
                pygame.display.quit()
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                if x >= textx - 1000 and x <= textx + textx_size + 1000:
                    if y >= texty - 1000 and y <= texty + texty_size + 1000:
                         in_main_menu = False
                         break

def special_end():
    text = bigfont.render("you found a secret exit!", 13, (0, 0, 0))
    textx = WIN_WIDTH - text.get_width()
    texty = WIN_HEIGHT - text.get_height()
    textx_size = text.get_width()
    texty_size = text.get_height()
    pygame.draw.rect(screen, (skyblue), ((textx + 60, texty + 60),
                                               (textx_size + 60, texty_size + 60)))
    screen.blit(text, (WIN_WIDTH / 2 - text.get_width() / 2,
                       WIN_HEIGHT / 2 - text.get_height() / 2))
    clock = pygame.time.Clock()
    pygame.display.flip()
    in_main_menu = True
    while in_main_menu:
        clock.tick(50)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                in_main_menu = False
                pygame.display.quit()
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                if x >= textx - 1000 and x <= textx + textx_size + 1000:
                    if y >= texty - 1000 and y <= texty + texty_size + 1000:
                         in_main_menu = False
                         break
                        
if __name__ == "__main__":
    main()

