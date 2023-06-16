from pygame import *
from random import randint
font.init()

window = display.set_mode((700, 500))
display.set_caption('Пинг-понг')

background = transform.scale(image.load('fonn.jpg'),(700, 500))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_speed, player_x, player_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_DOWN] and self.rect.y < 420:
            self.rect.y += self.speed
        if keys_pressed[K_UP] and self.rect.y > 10:
            self.rect.y -= self.speed

    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_s] and self.rect.y < 420:
            self.rect.y += self.speed
        if keys_pressed[K_w] and self.rect.y > 10:
            self.rect.y -= self.speed


stick_l = Player('polosa2.png', 5, 630, 250)
stick_r = Player('polosa2.png', 5, 10, 250)
ball = GameSprite('krug3.png', 3, 350, 250)

font = font.Font(None, 50)
l_lose = font.render('ЛЕВЫЙ ИГРОК ПРОИГРАЛ!!!', True, (255, 255, 255))
r_lose = font.render('ПРАВЫЙ ИГРОК ПРОИГРАЛ!!!', True, (255, 255, 255))

clock = time.Clock()
FPS = 60

speed_x = 3
speed_y = 3

run = True
finish = False
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    if finish != True:
        window.blit(background,(0,0))
        stick_l.reset()
        stick_r.reset()
        ball.reset()

        stick_l.update_l()
        stick_r.update_r()

        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if sprite.collide_rect(stick_l, ball):
            speed_x *= -1
        if sprite.collide_rect(stick_r, ball):
            speed_x *= -1
        if ball.rect.y >= 435 or ball.rect.y <= 0:
            speed_y *= -1
        
        if ball.rect.x <= 0:
            window.blit(l_lose, (100,250))
            finish = True
        if ball.rect.x >= 635:
            window.blit(r_lose, (100,250))
            finish = True


    clock.tick(FPS)
    display.update()
