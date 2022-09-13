import math
import typing

from tan import Tan


class Tangram:
    ROOT2 = math.sqrt(2)

    def __init__(self, scale: float = 1, gap: float = 0):
        root2 = self.ROOT2
        gap /= scale
        if gap == 0:
            display = None
        else:
            display = Tan((root2/4-gap/2*(2+root2), 0),
                          (0, root2/4-gap/2*(2+root2)))
            display.translate(gap/2, gap/2)
        self.t1a = Tan((root2/4, 0), (0, root2/4), display=display)
        self.t1b = Tan(copy=self.t1a)

        if gap != 0:
            display = Tan((1/2-gap/2*(2+root2), 0), (0, 1/2-gap/2*(2+root2)))
            display.translate(gap/2, gap/2)
        self.t2 = Tan((1/2, 0), (0, 1/2), display=display)

        if gap != 0:
            display = Tan((root2/2-gap/2*(2+root2), 0),
                          (0, root2/2-gap/2*(2+root2)))
            display.translate(gap/2, gap/2)
        self.t4a = Tan((root2/2, 0), (0, root2/2), display=display)
        self.t4b = Tan(copy=self.t4a)

        if gap != 0:
            display = Tan((root2/4-2*gap, 0),
                          (-gap, root2/4-gap),
                          (-root2/4+gap, root2/4-gap))
            display.translate(gap/2, gap/2)
        self.p = Tan((root2/4, 0),
                     (0, root2/4),
                     (-root2/4, root2/4),
                     display=display)

        if gap != 0:
            display = Tan((root2/4-gap, 0),
                          (root2/4-gap, root2/4-gap),
                          (0, root2/4-gap))
            display.translate(gap/2, gap/2)
        self.s = Tan((root2/4, 0), (root2/4, root2/4), (0, root2/4),
                     display=display)

        self.visible_tans: typing.List[Tan] = []
        self.all_tans = [self.t1a,
                         self.t1b,
                         self.t2,
                         self.t4a,
                         self.t4b,
                         self.s,
                         self.p]
        for tan in self.all_tans:
            tan.scale(scale)

    def scale(self, scale):
        for tan in self.all_tans:
            tan.scale(scale)

    def add(self, tan):
        self.visible_tans.append(tan)

    def draw(self, drawing):
        for tan in self.visible_tans:
            tan.draw(drawing)

    def translate(self, dx, dy):
        for tan in self.all_tans:
            tan.translate(dx, dy)

    def rotate(self, angle, anchor_point: typing.Tuple[float, float] = None):
        if anchor_point is None:
            anchor_point = self.visible_tans[0].anchor_point
        for tan in self.all_tans:
            tan.rotate(angle, anchor_point)

    @property
    def width(self):
        left, bottom, right, top = self.bounds
        return right - left

    @property
    def height(self):
        left, bottom, right, top = self.bounds
        return top - bottom

    @property
    def bounds(self) -> typing.Tuple[float, float, float, float]:
        """ Bounding box for all visible tans.

        :return: (left, bottom, right, top)
        """
        points_source = self.visible_tans or self.all_tans
        points = [point
                  for tan in points_source
                  for point in tan.points]
        left = min(x for x, y in points)
        right = max(x for x, y in points)
        top = max(y for x, y in points)
        bottom = min(y for x, y in points)
        return left, bottom, right, top
