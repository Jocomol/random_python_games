

import pygame, sys
from pygame import *

WIN_WIDTH =  800
WIN_HEIGHT = 640
HALF_WIDTH = int(WIN_WIDTH / 2)
HALF_HEIGHT = int(WIN_HEIGHT / 2)

game_over = False
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
#jumpsnd = pygame.mixer.Sound("Jump.wav")
#coinsnd = pygame.mixer.Sound("Coin.wav")
#hitsnd = pygame.mixer.Sound("Hit.wav")
def main():
    global cameraX, cameraY
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode(DISPLAY, FLAGS, DEPTH)
    pygame.display.set_caption("Version 0\Mod(bg1)")
    timer = pygame.time.Clock()
    Lives = 3

    up = down = left = right = running = False
    bg = Surface((32, 32))
    bg.convert()
    bg.fill(Color("skyblue"))
    #bg = pygame.image.load("bgtest2.jpg")
    screen.blit(bg, [0,0])
    entities = pygame.sprite.Group()
    player = Player(32, 32)
    platforms = []

    x = y = 0
    level = [
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "P                                                                  P",
        "P                                                                  P",
        "P                                                                  P",
        "P                                                  PPPP            P",
        "P                                     PPP          P               P",
        "P                                                          SS      P",
        "P                       PPPP                               PP      P",
        "P                                                                  P",
        "P                  B                                               P",
        "P                                                                  P",
        "P               S                                SSSS              P",
        "P           PPPPP                               PPPP        S      P",
        "P                           SSSSSSSSSS                      P      P",
        "P                           PPPPPPPPPP                      P      P",
        "P                B                                          P      P",
        "P                                                        B  P      P",
        "P                                              B            P      P",
        "P                    P                                      P      P",
        "P                    P                                      P      P",
        "P                PPPPPP                             B       P      P",
        "P                                        SSSS               P      P",
        "P                                        PPPP               P      PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "P                                                P          P                                                       P",                  
        "PPPPPPPPP                                        P          P                                                       P",
        "P                                                P          P       P      P                                        P",
        "P                                                P          P       P      P                                        P",
        "PSSSSSSSSCPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP      PPPPPPPPPPPSSSSSSPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPEP",
        "                                                   PSSSSSSP                                                          ",]




    # build the level
    for row in level:
        for col in row:
            if col == "P":
                p = Platform(x, y)
                platforms.append(p)
                entities.add(p)
            if col == "B":
                b = CBlock(x, y)
                platforms.append(b)
                entities.add(b)
            if col == "C":
                c = Stopblock(x, y)
                platforms.append(c)
                entities.add(c)
            if col == "E":
                e = Greenblock(x, y)
                platforms.append(e)
                entities.add(e)
            if col == "S":
                p = Spikes(x, y)
                platforms.append(p)
                entities.add(p)
                
            x += 32
        y += 32
        x = 0



    total_level_width  = len(level[0])*64
    total_level_height = len(level)*32
    camera = Camera(complex_camera, total_level_width, total_level_height)
    entities.add(player)

    while 1:
        timer.tick(60)

        
        for e in pygame.event.get():
            if e.type == QUIT: raise SystemExit, "QUIT"
            if e.type == KEYDOWN and e.key == K_ESCAPE:
                raise SystemExit, "ESCAPE"
            if e.type == KEYDOWN and e.key == K_w:
                up = True
            if e.type == KEYDOWN and e.key == K_s:
                down = True
            if e.type == KEYDOWN and e.key == K_a:
                left = True
            if e.type == KEYDOWN and e.key == K_d:
                right = True
            if e.type == KEYDOWN and e.key == K_SPACE:
                running = True

            if e.type == KEYUP and e.key == K_w:
                up = False
            if e.type == KEYUP and e.key == K_s:
                down = False
            if e.type == KEYUP and e.key == K_d:
                right = False
            if e.type == KEYUP and e.key == K_a:
                left = False

        

        # draw background
        for y in range(32):
            for x in range(32):
                screen.blit(bg, (x * 32, y * 32))

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
        self.onGround = False
        #self.image = Surface((32,32))
        #self.image.fill(Color("#0000FF"))
        #self.image.convert()
        self.image = pygame.image.load("resources\Textures\Entities\Wade_Ron\waderon.png")
        self.rect = Rect(x, y, 32, 64)
    def Eaten(self):
        self.rect = self.original_rect
        
    def update(self, up, down, left, right, running, platforms):
        if up:
            # only jump if on the ground
            if self.onGround: self.yvel -= 10
        if down:
            pass
        if running:
            self.xvel = 12
        if left:
            self.xvel = -8
        if right:
            self.xvel = 8
        if not self.onGround:
            # only accelerate with gravity if in the air
            self.yvel += 0.3
            # max falling speed
            if self.yvel > 100: self.yvel = 100
        if not(left or right):
            self.xvel = 0
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

    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if isinstance(p, Greenblock):
                    pygame.event.post(pygame.event.Event(QUIT))
                if isinstance(p, Spikes):
                    game_over = True
                    self.image = pygame.image.load("resources\Textures\Entities\Wade_Ron\waderon_dead.png")
                    pygame.time.delay(10000)
                    pygame.QUIT(100)

                if xvel > 0:
                    self.rect.right = p.rect.left
                    print "collide right"
                if xvel < 0:
                    self.rect.left = p.rect.right
                    print "collide left"
                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.yvel = 0
                if yvel < 0:
                    self.rect.top = p.rect.bottom


class Platform(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        #self.image = Surface((32, 32))
        #self.image.convert()
        #self.image.fill(Color("blue"))
        self.image = pygame.image.load("resources\Textures\Platforms\Ground.png")
        self.rect = Rect(x, y, 32, 32)
        
class CBlock(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        #self.image = Surface((32, 32))
        #self.image.convert()
        #self.image.fill(Color("blue"))
        self.image = pygame.image.load("resources\Textures\Platforms\CBlock(old).png")
        self.rect = Rect(x, y, 32, 32)

class Stopblock(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        #self.image = Surface((32, 32))
        #self.image.convert()
        #self.image.fill(Color("blue"))
        self.image = pygame.image.load("resources\Textures\Platforms\Stopblock(old).png")
        self.rect = Rect(x, y, 32, 32)


        
    def update(self):
        pass

class Greenblock(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        #self.image.fill(Color("red"))
        self.image = pygame.image.load("resources\Textures\Platforms\Greenblock(old).png")
        self.rect = Rect(x, y, 32, 32)
        
class Spikes(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        #self.image.fill(Color("red"))
        self.image = pygame.image.load("resources\Textures\Platforms\Spikes.png")
        self.rect = Rect(x, y, 32, 20)

if __name__ == "__main__":
    main()
