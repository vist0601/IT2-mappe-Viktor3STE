import pygame as pg


class Kollisjon:
    def ball_racket1(self, ball, racket1):
        if ball._posy + ball._radius > racket1._posy and ball._posy - ball._radius < racket1._posy + racket1._hoyde:
            if ball._posx - ball._radius <= racket1._posx + racket1._bredde:
                return True
        else:
            return False
    def ball_racket2(self, ball, racket2):
        if ball._posy + ball._radius > racket2._posy and ball._posy - ball._radius < racket2._posy + racket2._hoyde:
            if ball._posx + ball._radius >= racket2._posx:
                return True
        else:
            return False

    def ball_vegger(self, ball):
        if ball._posy - ball._radius <= 0:
            return True

        if ball._posy + ball._radius >= 500:
            return True

        else:
            return False

    def ball_sidevegger(self, ball):
        if ball._posx - ball._radius <= 0:
            return True
        if ball._posx + ball._radius >= 900:
            return True
        else:
            return False

