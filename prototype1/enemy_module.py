import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Game")

# Set up the clock
clock = pygame.time.Clock()

# Set up the colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Set up the fonts
score_font = pygame.font.Font(None, 36)
game_over_font = pygame.font.Font(None, 72)

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load("/Users/ben/PycharmProjects/pythonProject3/prototype1/graphics/player/galaga.png")
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 8
        self.bullets = pygame.sprite.Group()
        self.firing = False

    def update(self):
        self.rect.move_ip(self.direction * self.speed)

        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > screen_width:
            self.rect.right = screen_width

        if self.firing:
            self.fire()

    def fire(self):
        bullet_rect = pygame.Rect(self.rect.centerx - 2, self.rect.top, 4, 8)
        bullet = Bullet(bullet_rect, -10)
        self.bullets.add(bullet)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, rect, speed):
        super().__init__()
        self.image = pygame.Surface((4, 8))
        self.image.fill(red)
        self.rect = rect
        self.speed = speed

    def update(self):
        self.rect.y += self.speed

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(red)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, screen_width - self.rect.width)
        self.rect.y = -self.rect.height
        self.speed = random.randint(3, 6)
        self.dead = False

def update(self):
    self.rect.move_ip(0, self.speed)

    if self.rect.top > screen_height:
        self.dead = True

def create_enemy():
    return Enemy()

def update_enemies():
    for enemy in enemies:
        enemy.update()

def check_collisions(player, enemies, score):
    for enemy in enemies:
        if pygame.sprite.collide_rect(player, enemy):
        # Player collided with an enemy
            game_over = True
            return score

    for bullet in player.bullets:
        if pygame.sprite.collide_rect(bullet, enemy):
            # Bullet collided with an enemy
            enemy.dead = True
            player.bullets.remove(bullet)
            score += 10

# Remove dead enemies
    enemies.remove(*[e for e in enemies if e.dead])
    return score

# Set up the initial game state
game_over = False
score = 0

# Main game loop
while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.firing = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                player.firing = False

    # Handle player input
    Player.direction = pygame.math.Vector2(0, 0)

keys = pygame.key.get_pressed()
if keys[pygame.K_LEFT]:
    player.direction.x = -1
elif keys[pygame.K_RIGHT]:
    player.direction.x = 1

# Update game state
Player.update()

if random.randint(1, 60) == 1:
    enemies.add(create_enemy())

update_enemies(enemies)
score = check_collisions(player, enemies, score)

# Draw the game
screen.fill(white)

screen.blit(player.image, player.rect)

for enemy in enemies:
    if not enemy.dead:
        screen.blit(enemy.image, enemy.rect)

for bullet in player.bullets:
    pygame.draw.rect(screen, black, bullet.rect)

score_text = score_font.render(f"Score: {score}", True, black)
screen.blit(score_text, (10, 10))

if game_over:
    game_over_text = game_over_font.render("Game Over", True, black)
    screen.blit(game_over_text, (screen_width/2 - game_over_text.get_width()/2, screen_height/2 - game_over_text.get_height()/2))

# Update the display
pygame.display.flip()

# Wait for the next frame
clock.tick(60)

pygame.quit()
