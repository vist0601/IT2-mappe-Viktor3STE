import pygame as pg
from ball import Ball
from racket import Racket
from kollisjon import Kollisjon


pg.init()

BREDDE = 900
HOYDE = 500
SORT = (0, 0, 0)
HVIT = (255, 255, 255)

skjerm = pg.display.set_mode((BREDDE, HOYDE))

def main():

    skjerm.fill(SORT)

    ball = Ball(skjerm, HVIT, BREDDE/2, HOYDE/2, 15)
    racket1 = Racket(skjerm, HVIT, 15, HOYDE/2 - 60, 20, 120)
    racket2 = Racket(skjerm, HVIT, BREDDE - 35, HOYDE/2 - 60, 20, 120)
    kollisjon = Kollisjon()

    spiller = False

    font = pg.font.Font('freesansbold.ttf', 17)
    text = font.render('P = start   SPILLER 1: W = oppover, S = nedover   SPILLER 2: Piltast opp = oppover, Piltast ned = nedover', True, HVIT, SORT)
    textRect = text.get_rect()
    textRect.center = (BREDDE // 2, 50)

    fortsett = True
    clock = pg.time.Clock()
    while fortsett:

        clock.tick(60)
        for event in pg.event.get():

            skjerm.blit(text, textRect)
            
            if event.type == pg.QUIT:
                fortsett = False

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_p:
                    ball.startfart()
                    spiller = True

                if event.key == pg.K_w:
                    racket1._tilstand = "opp"

                if event.key == pg.K_s:
                    racket1._tilstand = "ned"

                if event.key == pg.K_UP:
                    racket2._tilstand = "opp"

                if event.key == pg.K_DOWN:
                    racket2._tilstand = "ned"

            if event.type == pg.KEYUP:
                racket1._tilstand = "stille"
                racket2._tilstand = "stille"


        if spiller:
            skjerm.fill(SORT)

            ball.beveg()
            ball.vis()

            racket1.beveg()
            racket1.racket_kollisjon()
            racket1.vis()
            racket2.beveg()
            racket2.racket_kollisjon()
            racket2.vis()

            if kollisjon.ball_racket1(ball, racket1):
                ball.racket_kollisjon()
                

            if kollisjon.ball_racket2(ball, racket2):
                ball.racket_kollisjon()

            if kollisjon.ball_vegger(ball):
                ball.vegg_kollisjon()

            if kollisjon.ball_sidevegger(ball):
                fortsett = False
                main()
                

        pg.display.update()


main()










