class TangramSet:
    def __init__(self, *tangrams):
        self.tangrams = tangrams

    def align(self, top: float, left: float, right: float) -> float:
        """ Align tangrams' bottoms with even horizontal spacing.

        :param top: target y position for the top of the tallest tangram
        :param left: left edge of first tangram
        :param right: right edge of last tangram
        :return: the y position of the bottom of all the tangrams
        """
        total_width = sum(tangram.width for tangram in self.tangrams)
        max_height = max(tangram.height for tangram in self.tangrams)
        total_gaps = (right - left) - total_width
        if len(self.tangrams) < 2:
            gap = 0
            x = (left + right - total_width) / 2
        else:
            gap = total_gaps / (len(self.tangrams) - 1)
            x = left
        y = top - max_height
        for tangram in self.tangrams:
            tl, tb, tr, tt = tangram.bounds
            tangram.translate(x - tl, y - tb)
            x += tr-tl + gap

        return y

    def draw(self, drawing):
        for tangram in self.tangrams:
            tangram.draw(drawing)

    def scale(self, scale):
        for tangram in self.tangrams:
            tangram.scale(scale)
