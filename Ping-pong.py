from pygame import *

win_width = 700
win_height = 500
display.set_caption("Ping-pong")
window = display.set_mode((win_width, win_height))

back = (200,255,255)
window.fill(back)
game = True
finish = False

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.sizeX = size_x
        self.sizeY = size_y
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 630: 
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 630:
            self.rect.y += self.speed

racket_l = Player('ракетка1.png', 30, 180, 50, 100, 10)
racket_r = Player('ракетка2.png', 650, 180, 50, 100, 10)
ball = GameSprite('мяч1.png', 350, 180, 30, 30, 5)

speed_y = 7
speed_x = 7
font.init()
font = font.Font(None, 35)
lose1 = font.render('Игрок 1 Проиграл!', True, (180, 0, 0))
lose2 = font.render('Игрок 2 Проиграл!', True, (180, 0, 0))

while game:
    for e in event.get():
        if e.type == QUIT:
           game = False
    if not finish:
        window.fill(back)
        racket_r.update_r()
        racket_l.update_l()

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(racket_l, ball) or sprite.collide_rect(racket_r, ball):
            speed_x *= -1
            speed_y *= -1
        if ball.rect.y > win_height or ball.rect.y < 0:
            speed_y *= -1
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
            game_over = True
        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2, (200, 200))
            game_over = True

        ball.reset()
        racket_r.reset()
        racket_l.reset()
        display.update()
    time.delay(50)
    
