# Third

# pygame version: 2.5.2
import pygame


pygame.init()

screen = pygame.display.set_mode((512, 512))
pygame.display.set_caption("third game: sprite")

walkRight = [
    pygame.image.load("sprite/R1.png"),
    pygame.image.load("sprite/R2.png"),
    pygame.image.load("sprite/R3.png"),
    pygame.image.load("sprite/R4.png"),
    pygame.image.load("sprite/R5.png"),
    pygame.image.load("sprite/R6.png"),
    pygame.image.load("sprite/R7.png"),
    pygame.image.load("sprite/R8.png"),
    pygame.image.load("sprite/R9.png"),
]
walkLeft = [
    pygame.image.load("sprite/L1.png"),
    pygame.image.load("sprite/L2.png"),
    pygame.image.load("sprite/L3.png"),
    pygame.image.load("sprite/L4.png"),
    pygame.image.load("sprite/L5.png"),
    pygame.image.load("sprite/L6.png"),
    pygame.image.load("sprite/L7.png"),
    pygame.image.load("sprite/L8.png"),
    pygame.image.load("sprite/L9.png"),
]
standing = pygame.image.load('sprite/standing.png')
background = pygame.image.load('sprite/heaven.jpg')

# Set up character
width = 40
height = 60
x = 50
y = 512 - height
vel = 5

# Set up clock
clock = pygame.time.Clock()

# Set up moving variable
jumping = False
jump_vel = 7

right = left = False
walkCount = 0

def drawing():
    global walkCount
    
    # Insert background picture
    screen.blit(background, (0, 0))
    
    # Drawing walking motions
    if walkCount + 1 >= 27:
        walkCount = 0
        
    if left:  
        screen.blit(walkLeft[walkCount//3], (x,y))
        walkCount += 1                          
    elif right:
        screen.blit(walkRight[walkCount//3], (x,y))
        walkCount += 1
    else:
        screen.blit(standing, (x, y))
        walkCount = 0
        
    pygame.display.update() 
    
    

running = True

while running:
    clock.tick(27)
     
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and x >= vel: 
        x -= vel
        left = True
        right = False
        
    elif keys[pygame.K_RIGHT] and x <= 512 - width - vel: 
        x += vel
        left = False
        right = True
    
    else:
        left = False
        right = False
        walkCount = 0
        
    # set up jumping key
    if keys[pygame.K_SPACE] and y == 512 - height:
        jumping = True
        left = False
        right = False
        walkCount = 0
        
    if jumping:
        if jump_vel >= -7:
            negative = 1
            if jump_vel < 0: negative = -1
            y -= (jump_vel ** 2) / 2 * negative
            jump_vel -= 1
        else:
            jumping = False
            jump_vel = 7
            
    drawing()
    
    
pygame.quit()
