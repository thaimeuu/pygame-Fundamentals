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
width = 64
height = 64
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
    
    # Uncomment for visualization but it's unnecessary
    # pygame.draw.rect(screen, 'red', (x, y, width, height))
    
    # Drawing walking motions
    
    # walkCount starts from 0 to 26, so we have to write condition like below
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
    
    # These 3 conditions are not to confuse the program
    # Without it, chances are you're moving right but left animations are drawn
    # Elif is important, without it, unexpected results happen (can't explain it yet)
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
    if not jumping:
        if keys[pygame.K_SPACE] and y == 512 - height:
            jumping = True
            left = False
            right = False
            walkCount = 0
        
    if jumping:
        if jump_vel >= -7:
            y -= (jump_vel * abs(jump_vel)) / 2
            jump_vel -= 1
        else:
            jumping = False
            jump_vel = 7
            
    drawing()
    
    
pygame.quit()
