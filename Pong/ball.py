import pygame as pg

class Ball:
    def __init__(self, skjerm, farge, posx, posy, radius):
        self._skjerm = skjerm
        self._farge = farge
        self._posx = posx
        self._posy = posy
        self._radius = radius
        self._xfart = 0
        self._yfart = 0
        self.vis()

    def vis(self):
        pg.draw.circle(self._skjerm, self._farge, (self._posx, self._posy), self._radius)

    def startfart(self):
        self._xfart = 4
        self._yfart = 1.5
        
        

    def beveg(self):
        self._posx += self._xfart
        self._posy += self._yfart

    def racket_kollisjon(self):
        self._xfart = -self._xfart * 1.1
        self._yfart * 1.1


    def vegg_kollisjon(self):
        self._yfart = -self._yfart
    

    

