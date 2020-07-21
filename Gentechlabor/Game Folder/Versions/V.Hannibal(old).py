

import pygame, sys
from pygame import *
WIN_WIDTH =  480*3
WIN_HEIGHT = 260*3
HALF_WIDTH = int(WIN_WIDTH / 2)
HALF_HEIGHT = int(WIN_HEIGHT / 2)
#pygame.font.init()
#font = pygame.font.SysFont("Courier New", 10)
#text = font.render("Cyka Blyat", 1, (0,0,0))
#game_over = False
#PROJECT ENDSCREEN#
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
DEPTH = 32
FLAGS = 0
CAMERA_SLACK = 30
black = (0,0,0)
skyblue = (176,228,245)
blue = (0,0,255)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)


#Sprite Loading
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


character = Surface((15,28),pygame.SRCALPHA)
character.blit(spritesheet2,(-30,-2))
character = pygame.transform.scale(character, (15*3,28*3))
smanwalk1 = character

character = Surface((16,27),pygame.SRCALPHA)
character.blit(spritesheet2,(-58,-2))
character = pygame.transform.scale(character, (16*3,27*3))
smanwalk2 = character

character = Surface((17,26),pygame.SRCALPHA)
character.blit(spritesheet2,(-84,-3))
character = pygame.transform.scale(character, (17*3,26*3))
smanwalk3 = character

character = Surface((17,24),pygame.SRCALPHA)
character.blit(spritesheet2,(-113,-3))
character = pygame.transform.scale(character, (17*3,24*3))
smanjump1 = character

character = Surface((15,29),pygame.SRCALPHA)
character.blit(spritesheet2,(0,-3))
character = pygame.transform.scale(character, (15*3,29*3))
smanstand1 = character



spritesheet3 = pygame.image.load("resources\Textures\Entities\Soldier\soldiersheet.png")

                               
character = Surface((28,31),pygame.SRCALPHA)
character.blit(spritesheet3,(-3,0))
character = pygame.transform.scale(character, (28*3,32*3))
soldierstand1 = character

character = Surface((25,32),pygame.SRCALPHA)
character.blit(spritesheet3,(-37,0))
character = pygame.transform.scale(character, (25*3,32*3))
soldierwalk1 = character

character = Surface((12,32),pygame.SRCALPHA)
character.blit(spritesheet3,(-74,0))
character = pygame.transform.scale(character, (12*3,32*3))
soldierwalk2 = character

character = Surface((25,32),pygame.SRCALPHA)
character.blit(spritesheet3,(-101,0))
character = pygame.transform.scale(character, (25*3,32*3))
soldierwalk3 = character

character = Surface((27,32),pygame.SRCALPHA)
character.blit(spritesheet3,(-129,-1))
character = pygame.transform.scale(character, (27*3,32*3))
soldierjump1 = character



def main():
    global cameraX, cameraY
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode(DISPLAY, FLAGS, DEPTH)
    pygame.display.set_caption("Version Hannibal")
    Timer = pygame.time.Clock()
    #Lives = 3
    #PROJECT LIVESYSTEM#
    bg = Surface((32, 32))
    bg.convert_alpha()
    up = down = left = right = running = False
    #bg = pygame.image.load("bgtest2.jpg")
    #PROJECT BACKGROUND#
    bg = Surface((WIN_WIDTH,WIN_HEIGHT)).convert_alpha()
    bg.fill(Color("skyblue"))
    screen.blit(bg, [0,0])
    entities = pygame.sprite.Group()
    player = Player(16*3,16*3)
    platforms = []

    x = y = 0
    level = [

        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "P                 SS     SP                                        P",
        "P                  S     SP                                        P",
        "P                        SP                                        P",
        "P                        SP                                        P",
        "PPPPPPPP                 SP                                        P",
        "P               P  P     SP                                        P",
        "P                        SP                                        P",
        "P                        SP             S    SSSSS                 P",
        "P                        SS                    SSS                 P",
        "P                         S                                        P",
        "P                         P                                        P",
        "P                                                                  P",
        "P                                  P      P     P                  P",
        "P                            P                                     P",
        "P                         P                                PP      P",
        "P                                                           P      P",
        "P                                                           P      P",
        "P                                                           P      P",
        "P                                                           PSSSS  P",
        "P                                                           PPPPP  P",
        "P                                                           P      P",
        "P                                                           P      P",
        "P                                                           P      P",
        "P                                                           P      P",
        "P                                                           P      P",
        "P                                                           P      P",
        "P                                                           P      P",
        "PSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSP      P",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP   SSSP",
        "                                                            P   PPPP",
        "                                                            P      P",
        "                                                            PEEEEEEP",
        "                                                            PPPPPPPP",]



    # build the level
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
            if col == "S":
                p = Spikes(x, y)
                platforms.append(p)
                entities.add(p)
            if col == "C":
                c = Stopblock(x, y)
                platforms.append(c)
                entities.add(c)
            if col == "B":
                b = CBlock(x, y)
                platforms.append(b)
                entities.add(b)
            
            
            x += 16*3
        y += 16*3
        x = 0



    total_level_width  = len(level[0])*64*3
    total_level_height = len(level)*64*3
    camera = Camera(complex_camera, total_level_width, total_level_height)
    entities.add(player)

    

        
    while 1:
        Timer.tick(60)


        for e in pygame.event.get():
            if e.type == QUIT: raise SystemExit, "QUIT"
            if e.type == KEYDOWN and e.key == K_ESCAPE:
                raise SystemExit, "ESCAPE"
            if e.type == KEYDOWN and e.key == K_UP:
                up = True
            if e.type == KEYDOWN and e.key == K_DOWN:
                down = True
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

        

        
        screen.blit(bg,(0,0))

        camera.update(player)

        # update player, draw everything else
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

    l = min(0, l)                           # stop scrolling at the left edge
    l = max(-(camera.width-WIN_WIDTH), l)   # stop scrolling at the right edge
    t = max(-(camera.height-WIN_HEIGHT), t) # stop scrolling at the bottom
    t = min(0, t)                           # stop scrolling at the top
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
        self.rect = Rect(x, y, 16*3, 32*3)
        
    def update(self, up, down, left, right, running, platforms):
        if up:
            # only jump if on the ground
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
            # only accelerate with gravity if in the air
            self.yvel += 0.4
            # max falling speed
            if self.yvel > 100: self.yvel = 100
        if not(left or right):
            self.xvel = 0
        if self.yvel < 0 or self.yvel > 2.2: self.airborne = True
        # increment in x direction
        self.rect.left += self.xvel
        # do x-axis collisions
        self.collide(self.xvel, 0, platforms)
        # increment in y direction
        self.rect.top += self.yvel
        # assuming we're in the air
        self.onGround = False;
        # do y-axis collisions
        self.collide(0, self.yvel, platforms)

        self.animate()

    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if isinstance(p, ExitBlock):
                    #game_over = True
                    print "Game Over"
                    print "press F to pay respects"
                    print "R.I.P. COD"
                    pygame.quit()
                    sys.exit()
                if isinstance(p, Spikes):
                    #game_over = True
                    print "Game Over"
                    print "press F to pay respects"
                    print "R.I.P. COD"
                    #self.image = pygame.image.load("resources\Textures\Entities\Wade_Ron\Waderon_dead.png")
                    pygame.quit()
                    sys.exit()
                if isinstance(p, Stopblock):
                    #game_over = True
                    print "Game Over"
                    print "press F to pay respects"
                    print "R.I.P. COD"
                    pygame.quit()
                    sys.exit()
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

   #if game_over:
        #self.image = pygame.image.load("resources\Textures\Entities\Wade_Ron\waderon_dead.png")
        #text = font.render("Game Over")
        #text_rect = text.get_rect()
        #text_x = screen.get_width() / 2 - text_rect.width / 2
        #text_y= screen.get_height() / 2 - text_rect.height / 2
        #screen.blit(text, [text_x, text_y])
        #pygame.time.delay(10000)
        #pygame.QUIT(100)
    #else:
        #PROJECT LIVESYSTEM#
        
            



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

                         
class Stopblock(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = pygame.image.load("resources\Textures\Platforms\Stopblock.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(16*3,16*3))
        self.rect = Rect(x, y, 16*3, 16*3)
        
    

class ExitBlock(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = pygame.image.load("resources\Textures\Platforms\Greenblock.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(16*3,16*3))
        self.rect = Rect(x, y, 16*3, 16*3)
        
        
class Spikes(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = pygame.image.load("resources\Textures\Platforms\Spikes.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(16*3, 16*3))
        self.rect = Rect(x, y, 16*3, 16*3)
        

if __name__ == "__main__":
    main()
