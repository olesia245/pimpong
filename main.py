from pygame import *
from random import *
wids = 500
heght = 700
window = display.set_mode((700,500))
display.set_caption('Пин понг')
clock = time.Clock()

game = True

class GameSprite(sprite.Sprite):
    def __init__(self,player, player_x, player_y, speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.speed = speed
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_d] and self.rect.y < 500-150:
            self.rect.y += self.speed
        if keys_pressed[K_a] and self.rect.y > 5:
            self.rect.y -= self.speed
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y < 500-150:
            self.rect.y += self.speed
        if keys_pressed[K_s] and self.rect.y > 5:
            self.rect.y -= self.speed

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y >= wids:
            self.rect.y = 3
            self.rect.x = 3
            lost += 1

player = Player('racket.png', 645, 100, 5 ,50, 150)
player1 = Player('racket.png', 0, 200, 5 ,50, 150)


while game:
    window.fill((96, 152, 255))
    for e in event.get():
        if e.type == QUIT:
            game = False

    player.update_r()
    player.reset()
    player1.update_l()
    player1.reset()

    display.update()
