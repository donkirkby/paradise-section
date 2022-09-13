import math
import typing


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
        self.anchor_point = (0, 0)
        self.fill = 'black'

    def draw(self, drawing):
        if self.display is not None:
            self.display.fill = self.fill
            self.display.draw(drawing)
        else:
            x0 = drawing['width']//2
            y0 = drawing['height']//2
            flipped_points = [(x0+x, y0-y) for x, y in self.points]
            drawing.add(drawing.polygon(flipped_points,
                                        fill=self.fill,
                                        stroke=self.fill))

    def translate(self, dx, dy):
        self.points = tuple((x+dx, y+dy) for x, y in self.points)
        if self.display:
            self.display.translate(dx, dy)

    def rotate(self, angle, anchor_point: typing.Tuple[float, float] = None):
        """ Rotate the tan through an angle, centred on (cx, cy).

        :param angle: in degrees, not radians
        :param anchor_point: centre of rotation, defaults to self.anchor_point
        """
        if anchor_point is None:
            anchor_point = self.anchor_point
        cx, cy = anchor_point
        theta = angle*math.pi / 180
        ct = math.cos(theta)
        st = math.sin(theta)
        relative_points = ((x-cx, y-cy) for x, y in self.points)
        rotated_points = ((x*ct-y*st, x*st+y*ct) for x, y in relative_points)
        self.points = tuple((x+cx, y+cy) for x, y in rotated_points)
        if self.display:
            self.display.rotate(angle, anchor_point)

    def scale(self, scale):
        self.points = tuple((scale*x, scale*y) for x, y in self.points)
        if self.display:
            self.display.scale(scale)

    def flip(self):
        self.points = tuple((x, -y) for x, y in self.points)
        if self.display:
            self.display.flip()

    def anchor(self, target: 'Tan', target_point=0, moving_point=0):
        new_x, new_y = target.points[target_point]
        old_x, old_y = self.points[moving_point]
        self.translate(new_x - old_x, new_y - old_y)
        self.anchor_point = new_x, new_y
