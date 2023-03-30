import pygame as pg


class Racket:
    def __init__(self, skjerm, farge, posx, posy, bredde, hoyde):
        self._screen = skjerm
        self._farge = farge
        self._posx = posx
        self._posy = posy
        self._bredde = bredde
        self._hoyde = hoyde
        self._tilstand = "stille"
        self.vis()

    def vis(self):
        pg.draw.rect(self._screen, self._farge, (self._posx, self._posy, self._bredde, self._hoyde))


    def beveg(self):
        if self._tilstand == "opp":
            self._posy -= 4
        elif self._tilstand == "ned":
            self._posy += 4

            

    def racket_kollisjon(self):
        if self._posy <= 0:
            self._posy = 0
        if self._posy + self._hoyde >= 500:
            self._posy = 500 - self._hoyde
        