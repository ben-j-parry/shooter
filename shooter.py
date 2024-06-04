#https://www.geeksforgeeks.org/pygame-tutorial/?ref=lbp
import pygame
import sys
import random
# Global Variables in here
BLACK = (0, 0, 0)
WHITE = (255,255,255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
COLOR = (255, 100, 98)
SURFACE_COLOR = (167, 255, 100) 
#WIDTH = 1000
#HEIGHT = 1000
SCORE = 0 

speed_x = 5
speed_y = 4

direction = 1
playersize = 20
all_sprites_list = pygame.sprite.Group()


TILE_SIZE = 64
WIDTH = TILE_SIZE * 8
HEIGHT = TILE_SIZE * 8

tiles = ['empty', 'wall', 'goal']


#main_char = pygame.image.load('sprite1.png')
#Sprite class 
class player(pygame.sprite.Sprite): 
    def __init__(self, color, height, width): 
        super().__init__() 
  
        self.image = pygame.Surface([width, height]) 
        self.image.fill(SURFACE_COLOR) 
        self.image.set_colorkey(COLOR) 
  
        pygame.draw.rect(self.image, 
                         color, 
                         pygame.Rect(0, 0, width, height)) 
  
        self.rect = self.image.get_rect() 

    def moveRight(self, pixels):
        self.rect.x += pixels
 
    def moveLeft(self, pixels):
        self.rect.x -= pixels
 
    def moveForward(self, pixels):
        self.rect.y += pixels
 
    def moveBack(self, pixels):
        self.rect.y -= pixels


def movementcontrol(player, screen):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player.moveLeft(10)
    if keys[pygame.K_d]:
        player.moveRight(10)
    if keys[pygame.K_s]:
        player.moveForward(10)
    if keys[pygame.K_w]:
        player.moveBack(10)

    x,y = screen.get_size()
    
    xedge(player, x)
    yedge(player, y)


def randommovement(object, screen):

    
    speed = random.randint(-5, 5) * 5
    xory = random.randint(0,3)


    if (xory == 0):
        object.rect.x += speed * speed/10
    elif(xory == 1):
        object.rect.y += speed * speed/10
    elif (xory == 2):
        object.rect.x -= speed * speed/10
    elif(xory == 3):
        object.rect.y -= speed * speed/10

    x,y = screen.get_size()
    
    xedge(object, x)
    yedge(object, y)

def yedge(player, height):
    if(player.rect.y >= height- playersize):
       player.rect.y = height - playersize
      
    if(player.rect.y <= 0):
        player.rect.y = 0  

def xedge(player, width):
    if(player.rect.x >= width- playersize):
       player.rect.x = width - playersize
      
    if(player.rect.x <= 0):
        player.rect.x = 0  

def randommovement2(object, screen):

    global direction, speed_x, speed_y

    if object.rect.x <= 20 or object.rect.x + playersize >= WIDTH:
        direction *= -1
        speed_x = random.randint(0, 8) * direction
        speed_y = random.randint(0, 8) * direction
 
        # Changing the value if speed_x
        # and speed_y both are zero
        if speed_x == 0 and speed_y == 0:
            speed_x = random.randint(2, 8) * direction
            speed_y = random.randint(2, 8) * direction
 
    # Changing the direction and x,y coordinate
    # of the object if the coordinate of top
    # side is less than equal to 20 or bottom side coordinate
    # is greater than equal to 580
    if object.rect.y <= 20 or object.rect.y + playersize >= HEIGHT:
        direction *= -1
        speed_x = random.randint(0, 8) * direction
        speed_y = random.randint(0, 8) * direction
 
        # Changing the value if speed_x
        # and speed_y both are zero
        if speed_x == 0 and speed_y == 0:
            speed_x = random.randint(2, 8) * direction
            speed_y = random.randint(2, 8) * direction

    object.rect.x += speed_x
    object.rect.y += speed_y
    
    x,y = screen.get_size()
    
    xedge(object, x)
    yedge(object, y)

def yedge(player, height):
    if(player.rect.y >= height- playersize):
       player.rect.y = height - playersize
      
    if(player.rect.y <= 0):
        player.rect.y = 0  

def xedge(player, width):
    if(player.rect.x >= width- playersize):
       player.rect.x = width - playersize
      
    if(player.rect.x <= 0):
        player.rect.x = 0 

#note sure how to pass a string that will become an object name
def addplayer(sprite, colour, x, y):

    sprite = player(colour, playersize, playersize)
    sprite.rect.x = x
    sprite.rect.y = y
    all_sprites_list.add(sprite) 

    return sprite

def collide(sprite1, sprite2):

    if (pygame.sprite.collide_rect(sprite1,sprite2)):
            sprite1.rect.x = random.randint(0, WIDTH)
            sprite1.rect.y = random.randint(0, HEIGHT)
            global SCORE
            SCORE += 10
            print(SCORE)



def main():
    # Initialize Pygame
    pygame.init()
    is_initialized = pygame.get_init()

    if (is_initialized == True):
        print('Booting...')

    #open screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    #
    pygame.display.set_caption("Pew Pew")
    
    mainsprite = addplayer("mainsprite", GREEN, 300, 300)
    enemy = addplayer("enemy", RED, 400, 400)    


    global SCORE
    SCORE = 0

    # Main game loop
    running = True
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Key presses handling

        movementcontrol(mainsprite, screen)
        randommovement2(enemy, screen)   
        collide(mainsprite, enemy)
        all_sprites_list.update()
        screen.fill(WHITE)
        all_sprites_list.draw(screen)

        font = pygame.font.SysFont('arial', 32)
        text = font.render(str(SCORE), True, BLACK, WHITE)
       # text.update()
        
        screen.blit(text, (30,30))
        pygame.display.flip()
        pygame.display.update()


        # Cap the frame rate
        pygame.time.Clock().tick(60)

    # Quit Pygame
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()