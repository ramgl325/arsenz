from pygame import *
clock = time.Clock()
FPS = 120

#создай окно игры
window = display.set_mode((700, 500))
display.set_caption("Догонялки")
background = transform.scale(image.load("background.png"),(700, 500))
window.blit(background,(0, 0))

x1 = 450
y1 = 320

x2 = 200
y2 = 100

speed = 15
game = True
while game:
    window.blit(background,(0, 0))

    for e in event.get():
        if e.type == QUIT:
            game = False
    sprite1 = transform.scale(image.load("sprite1.png"), (150 , 150))
    window.blit(sprite1, (x1, y1))
    sprite2 = transform.scale(image.load("sprite2.png"), (100 , 100))
    window.blit(sprite2, (x2, y2))
    display.update()
    clock.tick(FPS)
    keys_pressed = key.get_pressed()
    if keys_pressed[K_LEFT] and x1 > 5:
        x1 -= speed
    if keys_pressed[K_RIGHT] and x1 < 595:
        x1 += speed
    if keys_pressed[K_UP] and y1 > 5:
        y1 -= speed
    if keys_pressed[K_DOWN] and y1 < 395:
        y1 += speed
    if keys_pressed[K_a] and x2 > 5:
        x2 -= speed
    if keys_pressed[K_d] and x2 < 595:
        x2 += speed
    if keys_pressed[K_w] and y2 > 5:
        y2 -= speed
    if keys_pressed[K_s] and y2 < 395:
        y2 += speed

    
#задай фон сцены


#создай 2 спрайта и размести их на сцене

#обработай событие «клик по кнопке "Закрыть окно"»