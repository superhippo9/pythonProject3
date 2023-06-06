import pygame, random
from settings import tile_size, screen_height, screen_width
from tile import Tile
from player import Player
from enemy import Enemy
from bullet import Bullet

class Level:

    def __init__(self, level_data, surface):

        self.display_surface = surface
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.enemies = pygame.sprite.Group()
        self.setup_level(level_data)

        pygame.mixer.music.load("sounds/music/overture.mp3")
        pygame.mixer.music.play(-1)


    def setup_level(self, layout):

        for row_index, row in enumerate(layout):
            for cell_index, cell in enumerate(row):
                x = cell_index * tile_size
                y = row_index * tile_size
                if cell == "x":
                    tile = Tile((x,y), tile_size)
                    self.tiles.add(tile)
                elif cell == "p":
                    player_sprite = Player((x,y))
                    self.player.add(player_sprite)

        for i in range(10):
            enemy = Enemy((random.randint(300, screen_width), random.randint(0, screen_height)))
            self.enemies.add(enemy)



    def run(self):
        self.tiles.draw(self.display_surface)

        self.player.update(self.enemies)
        self.player.draw(self.display_surface)
        self.player.sprite.draw_bullets(self.display_surface)
        self.enemies.draw(self.display_surface)
        self.enemies.update()

        # Detect collisions between player and enemy
        bullet_collided_with_enemy = pygame.sprite.groupcollide(self.player.sprite.bullets, self.enemies, False, True)

        collided_with = pygame.sprite.spritecollide(self.player.sprite, self.enemies, False)
        for enemy in collided_with:
            exit()
