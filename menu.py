import pygame as pg
import gameplay
pg.init()

size = width, height = 800, 600
black = 0, 0, 0
red = 255, 0, 0


font = pg.font.Font('freesansbold.ttf', 32)
screen = pg.display.set_mode(size)
pg.display.set_caption('Jogo') 

buttonOffsetW = 0
buttonOffsetH = 150
buttonW = 175
buttonH = 50


playButton = pg.Rect((width//2 - buttonW//2) + buttonOffsetW, (height//2 - buttonH//2) + buttonOffsetH, buttonW, buttonH)
playText = font.render('PLAY', True, black)
playRect = playText.get_rect()
playRect.center = playButton.center

exitButton = pg.Rect((width//2 - buttonW//2) + buttonOffsetW, (height//2 - buttonH//2) + buttonOffsetH + buttonH + 20, buttonW, buttonH)
exitText = font.render('EXIT', True, black)
exitRect = exitText.get_rect()
exitRect.center = exitButton.center

isExit = False
while isExit == False:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            isExit = True

    mouseClick = pg.mouse.get_pressed()
    mousePos = pg.mouse.get_pos()


    if exitButton.collidepoint(mousePos) and mouseClick[0] == 1:
        isExit = True

    if playButton.collidepoint(mousePos) and mouseClick[0] == 1:
        isExit = gameplay.game(screen)

    screen.fill(black)

    pg.draw.rect(screen, red, playButton, 0)
    screen.blit(playText, playRect)
    pg.draw.rect(screen, red, exitButton, 0)
    screen.blit(exitText, exitRect)

    pg.display.flip()

pg.quit()