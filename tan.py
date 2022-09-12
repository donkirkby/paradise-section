import math


class Tan:
    def __init__(self, *points, copy: 'Tan' = None, display: 'Tan' = None):
        if copy is not None:
            self.points = copy.points
            if copy.display is None:
                self.display = None
            else:
                self.display = Tan(copy=copy.display)
        else:
            self.points = ((0, 0), ) + points
            self.display = None
        if display is not None:
            self.display = display

    def draw(self, drawing):
        if self.display is not None:
            self.display.draw(drawing)
        else:
            x0 = drawing['width']//2
            y0 = drawing['height']//2
            flipped_points = [(x0+x, y0-y) for x, y in self.points]
            drawing.add(drawing.polygon(flipped_points,
                                        fill='black',
                                        stroke='black'))

    def translate(self, dx, dy):
        self.points = tuple((x+dx, y+dy) for x, y in self.points)
        if self.display:
            self.display.translate(dx, dy)

    def rotate(self, angle, cx=0, cy=0):
        """ Rotate the tan through an angle, centred on (cx, cy).

        :param angle: in degrees, not radians
        :param cx: the x coordinate of the centre of rotation
        :param cy: the y coordinate of the centre of rotation
        """
        theta = angle*math.pi / 180
        ct = math.cos(theta)
        st = math.sin(theta)
        relative_points = ((x-cx, y-cy) for x, y in self.points)
        rotated_points = ((x*ct-y*st, x*st+y*ct) for x, y in relative_points)
        self.points = tuple((x+cx, y+cy) for x, y in rotated_points)
        if self.display:
            self.display.rotate(angle, cx, cy)

    def scale(self, scale):
        self.points = tuple((scale*x, scale*y) for x, y in self.points)
        if self.display:
            self.display.scale(scale)

    def flip(self):
        self.points = tuple((x, -y) for x, y in self.points)
        if self.display:
            self.display.flip()
