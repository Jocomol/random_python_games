

import pygame, sys

pygame.sprite.Group()
#waderon_bilder = ["wade.ron.rightrun.png", "wade.ron.rightjump.png", "wade.ron.r1.png",
                 #"wade.ronleftrun.png", "wade.ron.leftjump.png", "wade.ron.l1.png"]

from pygame import *

WIN_WIDTH =  800
WIN_HEIGHT = 640
HALF_WIDTH = int(WIN_WIDTH / 2)
HALF_HEIGHT = int(WIN_HEIGHT / 2)

DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
DEPTH = 32
FLAGS = 0
CAMERA_SLACK = 30

test_background = "resources\Textures\Background\BGround.png"
black = (0,0,0)
skyblue = (176,228,245)
blue = (0,0,255)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
lives = 3
#jumpsnd = pygame.mixer.Sound("Jump.wav")
#hitsnd = pygame.mixer.Sound("Hit.wav")
def main():
    global cameraX, cameraY
    pygame.init()
    pygame.mixer.init()
    jumpsnd = pygame.mixer.Sound("Jump.wav")
    hitsnd = pygame.mixer.Sound("Hit.wav")
    screen = pygame.display.set_mode(DISPLAY, FLAGS, DEPTH)
    pygame.display.set_caption("Version 0\MOD(bg3)")
    timer = pygame.time.Clock()
    #Health = 3
    jumpsnd = pygame.mixer.Sound("Jump.wav")
    coinsnd = pygame.mixer.Sound("Coin.wav")
    hitsnd = pygame.mixer.Sound("Hit.wav")
    global lives
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
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "P  PP                                                                              P",
        "P                                                                                  P",
        "P  PPPPP                                                                           P",
        "P  PP                                                                              P",
        "P  PP                                                 PS                           P",
        "P  PP                                             P   SS                           P",
        "P                                            P        SS                           P",
        "P                                                     SS                           P",
        "P                                               P     SS                           P",
        "P                                                     SS                           P",
        "P                                                  P  SS                           P",
        "P                    P                                SS                           P",
        "P                                               P     SS                           P",
        "P                P            SS           P          SS                           P",
        "P                             SS              P       SS                  S        P",
        "P                    P        SS         P                                P        P",
        "P                                                                     P   P        P",
        "P                        P        SPPPS                           P       P        P",
        "P                                                                         P        P",
        "P                    PPP                                                  P        P",
        "P                                                                         P        P",
        "P             PPP                                                         P        P",
        "P   PP                                                                    P        P",
        "PPPPPPSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSPEEEEEEEEP",
        "                                                                                    ",]



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
            x += 32
        y += 32
        x = 0

    total_level_width  = len(level[0])*120
    total_level_height = len(level)*32
    camera = Camera(complex_camera, total_level_width, total_level_height)
    entities.add(player)

    while 1:
        timer.tick(60)

        

        for e in pygame.event.get():
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
        self.image = pygame.image.load("resources\Textures\Entities\Wade_Ron\Waderon.png")
        self.rect = Rect(x, y, 32, 64)

        
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
        if right:
            self.xvel = 9
        if not self.onGround:
            # only accelerate with gravity if in the air
            self.yvel += 0.4
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
                if isinstance(p, ExitBlock):
                    print "You won."

                    pygame.quit()
                if isinstance(p, Spikes):
                    print "You died. Close this tab and press f5 to try again."

                    pygame.quit()
                    sys.exit()

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
                    
    def Turn(self, screen, direction):
        self.Direction(direction)
        index = -1
        
        if(direction == up):
            index = 0
        elif(direction == right):
            index = 3
        elif(direction == left):
            index = 6
        elif(direction == down):
            index = 9
        screen.fill([255, 255, 255])
        self.RenderImage(screen, index)
        pygame.display.update()
          
class Platform(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        #self.image = Surface((32, 32))
        #self.image.convert()
        #self.image.fill(Color("blue"))
        self.image = pygame.image.load("resources\Textures\Platforms\Ground.png")
        self.rect = Rect(x, y, 32, 32)

    def update(self):
        pass

class ExitBlock(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image.fill(Color("green"))
        
class Spikes(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        #self.image.fill(Color("red"))
        self.image = pygame.image.load("resources\Textures\Platforms\Spikes.png")
        self.rect = Rect(x, y, 32, 20)
        global lives
        lives = lives - 1

    #global lives, lives_text
    #font = pygame.font.Font(None, 50)
    #lives_text = font.render(str(lives), 1, (0, 0, 0))
    #textpos = [10, 10]
    #fertig = False


if __name__ == "__main__":
    main()
