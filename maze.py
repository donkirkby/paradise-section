import math
from networkx import Graph
from svgwrite import Drawing


class Maze:
    def __init__(self,
                 width: int = 0,
                 height: int = 0,
                 text: str|None = None):
        # graph has edge, if there is no wall between neighbouring nodes.
        self.graph = Graph()
        self.width = width
        self.height = height
        self.scale = 1.0
        self.offset_x = self.offset_y = 0
        self.chambers: list[tuple[float, float]] = []
        self.chamber_radius = math.sqrt(3*3 + 2*2)
        if text is None:
            lines: list[str] = []
        else:
            lines = text.splitlines()
            self.width = len(lines[0]) // 2
            self.height = len(lines) // 2
        for x in range(self.width):
            for y in range(self.height):
                self.graph.add_node((x, y))
                if text is not None:
                    wall_above = lines[y*2][x*2+1] != ' '
                    wall_to_left = lines[y*2+1][x*2] != ' '
                    if not wall_above:
                        self.graph.add_edge((x, y), (x, y-1))
                    if not wall_to_left:
                        self.graph.add_edge((x, y), (x-1, y))


    def display(self) -> str:
        lines = ['+-'*self.width + '+']
        for y in range(self.height):
            line = ['|']
            next_line = ['+']
            for x in range(self.width):
                has_wall_to_right = not self.graph.has_edge((x, y), (x+1, y))
                has_wall_below = not self.graph.has_edge((x, y), (x, y+1))
                line.append(' ')
                if has_wall_below:
                    next_line.append('-')
                else:
                    next_line.append(' ')
                if has_wall_to_right:
                    line.append('|')
                else:
                    line.append(' ')
                next_line.append('+')
            lines.append(''.join(line))
            lines.append(''.join(next_line))
        return '\n'.join(lines)

    def add_chamber(self, x: float, y: float) -> None:
        min_x = round(x - self.chamber_radius)
        max_x = round(x + self.chamber_radius)
        min_y = round(y - self.chamber_radius)
        max_y = round(y + self.chamber_radius)
        g = 1.1  # growth factor for radius
        for x2 in range(min_x, max_x+1):
            for y2 in range(min_y, max_y+1):
                if not math.sqrt((x2-x)**2 + (y2-y)**2) < self.chamber_radius*g:
                    # (x2, y2) is not inside the chamber.
                    continue
                if math.sqrt((x2+1-x)**2 + (y2-y)**2) < self.chamber_radius*g:
                    # right neighbour is also inside the chamber.
                    self.graph.add_edge((x2, y2), (x2+1, y2))
                if math.sqrt((x2-x)**2 + (y2+1-y)**2) < self.chamber_radius*g:
                    # right neighbour is also inside the chamber.
                    self.graph.add_edge((x2, y2), (x2, y2+1))
        self.graph.add_edge((max_x+1, y-0.5), (max_x, y-0.5))
        self.graph.add_edge((x-0.5, min_y-1), (x-0.5, min_y))
        self.graph.add_edge((min_x-1, y+0.5), (min_x, y+0.5))
        self.graph.add_edge((x+0.5, max_y+1), (x+0.5, max_y))

        self.chambers.append((x, y))

    def draw(self, drawing: Drawing) -> None:
        scale = self.scale
        line_style = dict(stroke='black',
                          stroke_width=round(scale / 5),
                          stroke_linecap='round')
        drawing.add(drawing.line(
            (self.offset_x, self.offset_y),
            (self.offset_x + scale*self.width, self.offset_y),
            **line_style))
        drawing.add(drawing.line(
            (self.offset_x + scale*self.width, self.offset_y),
            (self.offset_x + scale*self.width,
             self.offset_y + scale*self.height),
            **line_style))
        drawing.add(drawing.line(
            (self.offset_x + scale*self.width,
             self.offset_y + scale*self.height),
            (self.offset_x, self.offset_y + scale*self.height),
            **line_style))
        drawing.add(drawing.line(
            (self.offset_x, self.offset_y + scale*self.height),
            (self.offset_x, self.offset_y),
            **line_style))

        for x in range(self.width):
            for y in range(self.height):
                if y < self.height - 1 and not self.graph.has_edge((x, y),
                                                                   (x, y+1)):
                    drawing.add(drawing.line((self.offset_x + scale * x,
                                              self.offset_y + scale * (y + 1)),
                                             (self.offset_x + scale * (x + 1),
                                              self.offset_y + scale * (y + 1)),
                                             **line_style))
                if x < self.width - 1 and not self.graph.has_edge((x, y),
                                                                  (x+1, y)):
                    drawing.add(drawing.line((self.offset_x + scale * (x + 1),
                                              self.offset_y + scale * y),
                                             (self.offset_x + scale * (x + 1),
                                              self.offset_y + scale * (y + 1)),
                                             **line_style))

        r = round(self.chamber_radius) * scale
        for x, y in self.chambers:
            centre_x = (x + 0.5) * scale + self.offset_x
            centre_y = (y + 0.5) * scale + self.offset_y
            for dx1, dy1, dx2, dy2 in ((r, -scale, r-scale, -2*scale),
                                       (-r, -scale, -r+scale, -2*scale),
                                       (-r, scale, -r+scale, 2*scale),
                                       (r, scale, r-scale, 2*scale),
                                       (-scale, r, -2*scale, r-scale),
                                       (scale, r, 2*scale, r-scale),
                                       (scale, -r, 2*scale, -r+scale),
                                       (-scale, -r, -2*scale, -r+scale)):
                drawing.add(drawing.line((centre_x+dx1, centre_y+dy1),
                                         (centre_x+dx2, centre_y+dy2),
                                         **line_style))
