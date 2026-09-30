import math
import typing
from collections import defaultdict

import shapely
from shapely import Point

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
            x_shift = -0.25*gap
            display = Tan((root2/4-2*gap-2*x_shift, 0),
                          (-gap-2*x_shift, root2/4-gap),
                          (-root2/4+gap, root2/4-gap))
            display.translate(gap/2+x_shift, gap/2)
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
        polygons = [tan.create_polygon(drawing)
                    for tan in self.visible_tans]
        if not polygons:
            return

        fill = self.visible_tans[0].fill
        polygon_shapes = [shapely.Polygon(polygon) for polygon in polygons]

        tangram_magnitude = math.log10(max(self.width, self.height))
        grid_magnitude = math.floor(tangram_magnitude - 3)
        grid_size = math.pow(10, grid_magnitude)
        combined = shapely.union_all(polygon_shapes, grid_size=grid_size)
        components = getattr(combined, 'geoms', None)
        if components is None:
            components = [combined]
        for component in components:
            vertex_rings: dict[int, list] = defaultdict(list)
            exterior_points = [Point(c) for c in component.exterior.coords]
            for ring in component.interiors:
                start = Point(ring.coords[0])
                closest_index = 0
                min_distance = start.distance(exterior_points[0])
                for i, point in enumerate(exterior_points[1:], 1):
                    new_distance = start.distance(point)
                    if new_distance < min_distance:
                        min_distance = new_distance
                        closest_index = i
                vertex_rings[closest_index].append(ring)
            steps = ['M']
            for i, point in enumerate(exterior_points):
                steps.append(f'{point.x} {point.y}')
                for ring in vertex_rings[i]:
                    for x2, y2, in ring.coords:
                        steps.append(f'{x2} {y2}')
                    steps.append(f'{point.x} {point.y}')
            drawing.add(drawing.path(' '.join(steps),
                                        fill=fill,
                                        fill_rule='evenodd'))

    def translate(self, dx, dy):
        for tan in self.all_tans:
            tan.translate(dx, dy)

    def flip(self):
        for tan in self.all_tans:
            tan.flip()

    def rotate(self,
               angle,
               anchor_point: None | tuple[float, float] = None):
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
