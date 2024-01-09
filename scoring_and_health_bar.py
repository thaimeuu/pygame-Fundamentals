# Eighth

# pygame version: 2.5.2
import pygame


pygame.init()

horizontal, vertical = (512, 512)
screen = pygame.display.set_mode((horizontal, vertical))
pygame.display.set_caption("seventh game: collisions and hit boxes")
clock = pygame.time.Clock()
FPS = 27
font = pygame.font.SysFont('calibri', 30, bold=True)

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
background = pygame.image.load("background/summoner_rift.jpg")


class Character:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.velocity = 5
        self.right = True
        self.left = False
        self.walkCount = 0

        self.jumping = False
        self.jumpCount = 7
        
        self.hitbox = (self.x + 20, self.y + 12, 26, 50)  # hitbox is a rectangle

    def draw_motion(self, surface):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if self.right:
            surface.blit(walkRight[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        elif self.left:
            surface.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        else:
            self.walkCount = 0
            
        self.hitbox = (self.x + 20, self.y + 12, 26, 50)  # Update hitbox's position with hero's
        # pygame.draw.rect(surface, 'red', self.hitbox, 1)  # 1 is rectangle line thickness


class Enemy:
    walkRight = [
        pygame.image.load("enemy/R1E.png"),
        pygame.image.load("enemy/R2E.png"),
        pygame.image.load("enemy/R3E.png"),
        pygame.image.load("enemy/R4E.png"),
        pygame.image.load("enemy/R5E.png"),
        pygame.image.load("enemy/R6E.png"),
        pygame.image.load("enemy/R7E.png"),
        pygame.image.load("enemy/R8E.png"),
        pygame.image.load("enemy/R9E.png"),
        pygame.image.load("enemy/R10E.png"),
        pygame.image.load("enemy/R11E.png"),
    ]
    walkLeft = [
        pygame.image.load("enemy/L1E.png"),
        pygame.image.load("enemy/L2E.png"),
        pygame.image.load("enemy/L3E.png"),
        pygame.image.load("enemy/L4E.png"),
        pygame.image.load("enemy/L5E.png"),
        pygame.image.load("enemy/L6E.png"),
        pygame.image.load("enemy/L7E.png"),
        pygame.image.load("enemy/L8E.png"),
        pygame.image.load("enemy/L9E.png"),
        pygame.image.load("enemy/L10E.png"),
        pygame.image.load("enemy/L11E.png"),
    ]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end

        self.path = [x, end]
        self.velocity = 2
        self.walkCount = 0
        
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health = 10
        self.visible = True
        self.respawnCount = 30

    def move(self):
        if self.velocity > 0:
            if self.x <= self.path[1] - self.velocity:
                self.x += self.velocity
            else:
                self.velocity *= -1
                self.walkCount = 0
        else:
            if self.x >= self.path[0] + self.velocity:
                self.x += self.velocity
            else:
                self.velocity *= -1
                self.walkCount = 0

    def draw_motion(self, surface):
        self.move()
        self.respawn()
        
        if self.visible:
            if self.walkCount + 1 >= 33:
                self.walkCount = 0

            if self.velocity > 0:
                surface.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            else:
                surface.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1

            self.hitbox = (self.x + 17, self.y + 2, 31, 57)
            # pygame.draw.rect(surface, 'red', self.hitbox, 1)  # 1 is rectangle line thickness
            
            # health bar
            pygame.draw.rect(surface, 'red', (self.hitbox[0], self.hitbox[1] - 10, self.width - 30, 5))
            pygame.draw.rect(surface, 'green', (self.hitbox[0], self.hitbox[1] - 10, (self.width - 30) * self.health//10, 5))
        
            
    def hit(self):
        if self.health > 1:
            self.health -= 1
        else:
            self.visible = False
            
    def respawn(self):
        if not self.visible:
            self.respawnCount -= 1
            if self.respawnCount == 0:
                self.visible = True
                self.health = 10
                self.respawnCount = 30

class Projectile:
    def __init__(self, x, y, color, radius, direction):
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
        self.direction = direction  # 1 or -1

        self.velocity = 8 * direction

    def draw_motion(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)


def drawing():
    screen.blit(background, (0, 0))
    hero.draw_motion(screen)
    goblin.draw_motion(screen)
    for bullet in bullets:
        bullet.draw_motion(screen)
        
    text = font.render(f'Score: {score}', 1, 'black')
    screen.blit(text, (380, 10))
    
    pygame.display.update()


hero = Character(50, 512 - 64, 64, 64)
goblin = Enemy(150, 512 - 60, 64, 64, 350)
score = 0
bullets = []
bullet_cooldown = 0
running = True

while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for bullet in bullets:
        if bullet.x <= horizontal and bullet.x >= 0:
            bullet.x += bullet.velocity
        else:
            bullets.pop(bullets.index(bullet))
        
        # Collisions when bullets hit goblin's hitbox
        if goblin.visible:
            if (bullet.y + bullet.radius) >= goblin.hitbox[1] and (bullet.y - bullet.radius) <= goblin.hitbox[1] + goblin.hitbox[3]:
                if bullet.x >= goblin.hitbox[0] and bullet.x <= goblin.hitbox[0] + goblin.hitbox[2]:
                    bullets.pop(bullets.index(bullet))
                    goblin.hit()
                    score += 1
    
    if bullet_cooldown > 0:
        bullet_cooldown += 1            
    if bullet_cooldown == 5:
        bullet_cooldown = 0
            
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and bullet_cooldown == 0:
        bullet_cooldown += 1
        if hero.left:
            direction = -1
        else:
            direction = 1

        if len(bullets) < 5:
            bullets.append(
                Projectile(
                    hero.x + hero.width // 2,
                    hero.y + hero.height // 2,
                    "red",
                    3,
                    direction,
                )
            )

    if keys[pygame.K_LEFT] and hero.x >= 0 + hero.velocity:
        hero.left = True
        hero.right = False
        hero.x -= hero.velocity
    elif keys[pygame.K_RIGHT] and hero.x <= horizontal - hero.width - hero.velocity:
        hero.right = True
        hero.left = False
        hero.x += hero.velocity
    else:
        hero.walkCount = 0

    if not hero.jumping:
        if keys[pygame.K_UP] and hero.y == vertical - hero.height:
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
