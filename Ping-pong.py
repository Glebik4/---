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
        if keys[K_UP] and self.rect.x > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.x < 630: 
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 630:
            self.rect.y += self.speed

rocket_l = Player('Ракетка 1.png', 30, 200, 70, 150, 4)
rocked_r = Player('Ракетка 2.png', 600, 200, 70, 150, 4)
ball = GameSprite('мяч.png', 300, 250, 50, 30, 4)

while game:
    for e in event.get():
        if e.type == QUIT:
           game = False
    if not finish:
        window.fill(back)
        rocked_r.update_r()
        rocket_l.update_l()

        ball.reset()
        rocked_r.reset()
        rocket_l.reset()
        display.update()
    time.delay(50)
