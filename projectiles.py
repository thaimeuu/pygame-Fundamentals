# Fifth

# pygame version: 2.5.2
import pygame


pygame.init()

surf_horizontal, surf_vertical = (512, 512)
screen = pygame.display.set_mode((surf_horizontal, surf_vertical))
pygame.display.set_caption("fifth game: projectiles")
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
background = pygame.image.load("sprite/heaven.jpg")


class Character:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.velocity = 5
        self.jumping = False
        self.jumpCount = 7
        # Hero shouldn't face us when he stops,
        # so we have to initialize his first position, where his face turns right
        self.right = True
        self.left = False
        self.walkCount = 0

    def draw_motion(self, surface):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if self.right:
            surface.blit(walkRight[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        elif self.left:
            surface.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1


class Projectiles:
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing  # facing is either 1 or -1 to specify the direction
        self.velocity = 8 * facing

    def draw_motion(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)


def drawing():
    screen.blit(background, (0, 0))
    hero.draw_motion(screen)
    for bullet in bullets:
        bullet.draw_motion(screen)
        
    pygame.display.update()


hero = Character(50, 512 - 64, 64, 64)
bullets = []
running = True

while running:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for bullet in bullets:
        if bullet.x <= surf_horizontal and bullet.x >= 0:
            bullet.x += bullet.velocity
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if hero.left:
            facing = -1
        else:
            facing = 1

        if len(bullets) <= 5:
            bullets.append(
                Projectiles(
                    round(hero.x + hero.width // 2),
                    round(hero.y + hero.height // 2),
                    3,
                    "red",
                    facing,
                )
            )

    if keys[pygame.K_RIGHT] and hero.x <= surf_horizontal - hero.width - hero.velocity:
        hero.right = True
        hero.left = False
        hero.x += hero.velocity
    elif keys[pygame.K_LEFT] and hero.x >= hero.velocity:
        hero.right = False
        hero.left = True
        hero.x -= hero.velocity
    else:
        hero.walkCount = 0

    if not hero.jumping:
        if keys[pygame.K_UP] and hero.y == surf_vertical - hero.height:
            hero.jumping = True
            hero.walkCount = 0
    else:
        if hero.jumpCount >= -7:
            hero.y -= hero.jumpCount * abs(hero.jumpCount) * 0.5
            hero.jumpCount -= 1
        else:
            hero.jumping = False
            hero.jumpCount = 7

    drawing()


pygame.quit()
