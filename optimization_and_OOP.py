# Fourth

# pygame version: 2.5.2
import pygame

pygame.init()

screen = pygame.display.set_mode((512, 512))
pygame.display.set_caption("fourth game: OOP")
clock = pygame.time.Clock()

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
standing = pygame.image.load("sprite/standing.png")
background = pygame.image.load("sprite/heaven.jpg")


class Player:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.vel = 5
        self.jumping = False
        self.jumpCount = 7
        self.left = False
        self.right = False
        self.walkCount = 0

    def draw(self, screen):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if self.left:
            screen.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        elif self.right:
            screen.blit(walkRight[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        else:
            screen.blit(standing, (self.x, self.y))
            self.walkCount = 0


def drawing():
    screen.blit(background, (0, 0))
    character.draw(screen)
    pygame.display.update()


# Main loop

character = Player(50, 512 - 64, 64, 64)
running = True

while running:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and character.x >= character.vel:
        character.x -= character.vel
        character.left = True
        character.right = False

    elif keys[pygame.K_RIGHT] and character.x <= 512 - character.width - character.vel:
        character.x += character.vel
        character.left = False
        character.right = True

    else:
        character.left = False
        character.right = False
        character.walkCount = 0

    if not character.jumping:
        if keys[pygame.K_SPACE] and character.y == 512 - character.height:
            character.jumping = True
            character.left = False
            character.right = False
            character.walkCount = 0

    elif character.jumping:
        if character.jumpCount >= -7:
            character.y -= (character.jumpCount * abs(character.jumpCount)) / 2
            character.jumpCount -= 1
        else:
            character.jumping = False
            character.jumpCount = 7

    drawing()


pygame.quit()
