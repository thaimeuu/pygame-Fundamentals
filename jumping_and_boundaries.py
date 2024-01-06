# Second

# pygame version: 2.5.2
import pygame


# set up
pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('second game: jumping')

# Create character
x = 10
y = 460
width = 40
height = 40
vel = 10

running = True

# Jumping part, when jumping, don't allow go up and down
jumping = False
jump_vel = 8

while running:
    pygame.time.delay(50)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill("black")
    
    # Render your game here
    
    pygame.draw.rect(screen, 'red', (x, y, width, height))
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and x >= vel: 
        x -= vel
    if keys[pygame.K_RIGHT] and x <= 500 - width - vel: 
        x += vel
    
    # set up jumping key
    if keys[pygame.K_SPACE] and y == 500 - height:
        jumping = True
        
    if not jumping:
        if keys[pygame.K_UP] and y >= vel: 
            y -= vel
        if keys[pygame.K_DOWN] and y <= 500 - height - vel: 
            y += vel
        
    elif jumping:
        if jump_vel >= -8:
            negative = 1
            if jump_vel < 0: negative = -1
            y -= (jump_vel ** 2) / 2 * negative
            jump_vel -= 1
        else:
            jumping = False
            jump_vel = 8
    
    pygame.display.update()
    

pygame.quit()
    