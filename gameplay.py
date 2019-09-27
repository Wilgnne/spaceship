import pygame as pg
import time, random

def game(screen:pg.surface):
    print("IsInGameplay")
    size = width, height = screen.get_size()
    black = 0, 0, 0
    red = 255, 0, 0
    color = 20, 30, 30
    branco = 255, 255, 255
    font = pg.font.Font('freesansbold.ttf', 32)

    points = 0
    pointsText = font.render(str(points), True, branco)
    pointsRect = pointsText.get_rect()
    pointsRect.midtop = (width//2, 0)

    coracaoImage = pg.image.load("coracao.png")

    life = 3
    
    lifeText = font.render(str(life), True, red)

    inimigoImage = pg.image.load("inimigo.png")
    inimigoPos = []

    tiroImage = pg.image.load("tiro.png")
    tiroPos = []
    fireTime = 0.30
    fireCont = 0
    isFired = False

    playerImage = pg.image.load("nave.png")
    playerPos = playerImage.get_rect()
    playerPos.center = (width//2, 3*height//4)
    velocity = 32 * 15
    
    deltatime = 1/60
    isExit = False
    isPlay = True
    while isExit == False and isPlay == True:
        init = time.time()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                isExit = True

        key=pg.key.get_pressed()  #checking pressed keys
        if key[pg.K_ESCAPE]:
            isPlay = False

        deltaVel = velocity * deltatime
        if key[pg.K_a] and playerPos.left > 0:
            playerPos = playerPos.move(-deltaVel, 0)
        if key[pg.K_d] and playerPos.right < width:
            playerPos = playerPos.move(deltaVel, 0)
        if key[pg.K_w] and playerPos.top > 0:
            playerPos = playerPos.move(0, -deltaVel)
        if key[pg.K_s] and playerPos.bottom < height:
            playerPos = playerPos.move(0, deltaVel)
        
        if key[pg.K_SPACE] and isFired == False:
            t = tiroImage.get_rect()
            t.center = playerPos.midtop
            tiroPos.append(t)
            isFired = True
        
        if isFired == True:
            fireCont += deltatime
        if fireCont > fireTime:
            isFired = False
            fireCont = 0
        
        if random.random() < 0.005:
            newInimigo = inimigoImage.get_rect()
            newInimigo.midbottom = ( random.randint(30, width - 30) ,-10)
            inimigoPos.append(newInimigo)
        
        colPlayer = playerPos.collidelist(inimigoPos)
        if colPlayer != -1:
            inimigoPos.pop(colPlayer)
            life -= 1
            lifeText = font.render(str(life), True, red)
        
        if life == 0:
            isPlay = False

        screen.fill(color)

        for tiro in tiroPos:
            for col in tiro.collidelistall(inimigoPos):
                inimigoPos.pop(col)
                tiroPos.remove(tiro)
                points += random.randint(10, 50)
                pointsText = font.render(str(points), True, branco)
                pointsRect = pointsText.get_rect()
                pointsRect.midtop = (width//2, 0)
            if tiro.bottom < 0:
                tiroPos.remove(tiro)
            tiro.move_ip(0, -20 * 32 * deltatime)
            screen.blit(tiroImage, tiro)

        for inimigo in inimigoPos:
            if inimigo.top > height:
                inimigoPos.remove(inimigo)
            inimigo.move_ip(0, 15 * 32 * deltatime)
            screen.blit(inimigoImage, inimigo)
        
        screen.blit(playerImage, playerPos)
        screen.blit(lifeText, lifeText.get_rect())

        screen.blit(pointsText, pointsRect)

        for i in range(life):
            rec = coracaoImage.get_rect()
            rec.right = width - (i * coracaoImage.get_width())

            screen.blit(coracaoImage, rec)


        pg.display.flip()
        deltatime = time.time() - init

    return isExit