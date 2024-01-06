# First

# pygame version: 2.5.2
import pygame


# pygame setup
pygame.init()  # Initialing pygame

screen = pygame.display.set_mode((500, 500))  # Creating window for our game with (width, height) = (500, 500)
# Note: The coordinate origin is on the top left of the screen
# horizontal axis is x axis and x increases along the right hand side
# vertical axis is y axis and y increases along the down side

clock = pygame.time.Clock()

pygame.display.set_caption("first game: movement")  # Set caption for window

x = 50
y = 50
width = 40
height = 60
vel = 5  # velocity

running = True
while running:
    pygame.time.delay(100)  # 100 milliseconds
    
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
                    
    # fill the screen so you don't see the 'footprint'/trace of the character
    screen.fill((0, 0, 0))  # fill background with black 
    
    # RENDER YOUR GAME HERE
    
    # draw character
    pygame.draw.rect(screen, (255, 0, 255), (x, y, width, height))  # color is RGB
    
    # move character
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and x >= vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x <= (500 - width) - vel:
        x += vel
    if keys[pygame.K_UP] and y >= vel:
        y -= vel
    if keys[pygame.K_DOWN] and y <= (500 - height) - vel:
        y += vel
    
    # flip() the display to put your work on screen
    # pygame.display.flip()
        
    clock.tick(60)  # limits FPS to 60

    pygame.display.update()
        
        
pygame.quit()
