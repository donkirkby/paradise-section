import math

from tangram_set import TangramSet


class TangramCircle(TangramSet):
    def align(self, x: float, y: float, r: float) -> None:
        """ Align tangrams' bottoms with even horizontal spacing.

        :param x: x coordinate of the circle's centre
        :param y: y coordinate of the circle's centre
        :param r: radius of the circle
        """
        n = len(self.tangrams)
        for i, tangram in enumerate(self.tangrams):
            angle = math.pi / 2 - math.pi*2 * (i+1) / n
            x2 = x + r * math.cos(angle)
            y2 = y + r*math.sin(angle)

            tl, tb, tr, tt = tangram.bounds
            tangram.translate(x2 - (tl + tr) / 2, y2 - (tb + tt) / 2)
