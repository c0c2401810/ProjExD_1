import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg") #背景画像のSurface
    bg_img2 = pg.transform.flip(bg_img,True,False)#背景画像の反転
    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img,True,False)
    kk_rct = kk_img.get_rect()
    kk_rct.center = 300, 200
    
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        key_lst = pg.key.get_pressed()
        x = -1
        y = 0

        if key_lst[pg.K_UP]:
            x = 0
            y = -1
        elif key_lst[pg.K_DOWN]:
            x = 0
            y = +1
        elif key_lst[pg.K_RIGHT]:
            x = +2
            y = 0
        elif key_lst[pg.K_LEFT]:
            x = -2
            y = 0
        kk_rct.move_ip(x, y)

        screen.blit(bg_img, [-tmr, 0])
        screen.blit(bg_img2, [-tmr+1600, 0]) #2
        screen.blit(bg_img, [-tmr+3200, 0])#3
        screen.blit(kk_img, [-tmr, 200])
        screen.blit(kk_img, kk_rct)

        if tmr == 3199:
            tmr = 0
        
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()