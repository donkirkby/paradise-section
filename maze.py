import logging
import math
import random
from collections import defaultdict
from itertools import count
from pathlib import Path
from typing import Any

from networkx import Graph
from svgwrite import Drawing

from tangram import Tangram

logger = logging.getLogger(__name__)

class Maze:
    ARROW = '\u21E9'

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

        # [ (x, y, group_name) ]
        self.chambers: list[tuple[float, float, str]] = []

        self.chamber_radius = math.sqrt(3*3 + 2*2)

        # { chamber_group_name: tangram }
        self.tangrams: dict[str, Tangram] = {}

        # { group_name: {(x, y)} }
        self.groups: dict[str, set[tuple[int, int]]] = defaultdict(set)

        # nodes from all groups in one set.
        self.all_groups: set[tuple[int, int]] = set()

        # { ((start_x, start_y), (end_x, end_y)) }  start < end
        self.forbidden_edges: set[tuple[tuple[int, int], tuple[int, int]]] = set()

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


    def display(self, show_groups: bool = False) -> str:
        lines = ['+-'*self.width + '+']
        for y in range(self.height):
            line = ['|']
            next_line = ['+']
            for x in range(self.width):
                node = (x, y)
                right_node = (x+1, y)
                has_wall_to_right = not self.graph.has_edge(node, right_node)
                below_node = (x, y + 1)
                has_wall_below = not self.graph.has_edge(node, below_node)
                if not show_groups:
                    line.append(' ')
                else:
                    for name, nodes in self.groups.items():
                        if node in nodes:
                            line.append(name[0])
                            break
                    else:
                        line.append(' ')
                if has_wall_below:
                    if self.is_forbidden_edge(node, below_node):
                        next_line.append('=')
                    else:
                        next_line.append('-')
                else:
                    next_line.append(' ')
                if has_wall_to_right:
                    if self.is_forbidden_edge(node, right_node):
                        line.append(':')
                    else:
                        line.append('|')
                else:
                    line.append(' ')
                next_line.append('+')
            lines.append(''.join(line))
            lines.append(''.join(next_line))
        return '\n'.join(lines)

    def add_to_group(self, x: int, y: int, group_name: str) -> None:
        node = (x, y)
        group_nodes = self.groups[group_name]
        group_nodes.add(node)
        self.all_groups.add(node)

    def get_group(self, group_name: str) -> set[tuple[int, int]]:
        return self.groups[group_name]

    def add_chamber(self, x: float, y: float, group_name: str) -> None:
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
                self.add_to_group(x2, y2, group_name)
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
        self.add_to_group(max_x+1, round(y-0.5), group_name)
        self.add_to_group(round(x-0.5), min_y-1, group_name)
        self.add_to_group(min_x-1, round(y+0.5), group_name)
        self.add_to_group(round(x+0.5), max_y+1, group_name)
        r = self.chamber_radius
        for dx, dy in ((-1.5, -r-1), (0.5, -r-1), (1.5, -r-1),
                       (-r, -r+1), (r, -r+1),
                       (-r, 1.5), (r, 1.5),
                       (-1.5, r), (-0.5, r), (1.5, r)):
            self.forbid_edge((round(x+dx), round(y+dy)),
                             (round(x+dx), round(y+dy+1)))
        for dx, dy in ((-2.5, -r), (1.5, -r),
                       (-r-1, -1.5), (r, -1.5), (-r-1, -0.5),
                       (r, 0.5), (-r-1, 1.5), (r, 1.5),
                       (-2.5, r), (1.5, r)):
            self.forbid_edge((round(x+dx), round(y+dy)),
                             (round(x+dx+1), round(y+dy)))

        self.chambers.append((x, y, group_name))

    def draw(self, drawing: Drawing) -> None:
        scale = self.scale
        stroke_width = round(scale / 5)
        line_style = dict(stroke='black',
                          stroke_width=stroke_width,
                          stroke_linecap='round')
        drawing.add(drawing.line(
            (self.offset_x, self.offset_y),
            (self.offset_x + scale*2, self.offset_y),
            **line_style))
        drawing.add(drawing.line(
            (self.offset_x + scale*3, self.offset_y),
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
            (self.offset_x + scale*(self.width-2),
             self.offset_y + scale*self.height),
            **line_style))
        drawing.add(drawing.line(
            (self.offset_x + scale*(self.width-3),
             self.offset_y + scale*self.height),
            (self.offset_x, self.offset_y + scale*self.height),
            **line_style))
        drawing.add(drawing.line(
            (self.offset_x, self.offset_y + scale*self.height),
            (self.offset_x, self.offset_y),
            **line_style))
        drawing.add(drawing.text(Maze.ARROW,
                                 x=[self.offset_x +
                                    round(2.5*scale)],
                                 y=[self.offset_y - stroke_width +
                                    round(0.83*scale)],
                                 text_anchor='middle',
                                 font_family='Noto Sans Mono',
                                 font_size=self.scale))
        drawing.add(drawing.text(Maze.ARROW,
                                 x=[self.offset_x +
                                    round((self.width - 2.5)*scale)],
                                 y=[self.offset_y + stroke_width +
                                    round((self.height - 0.17)*scale)],
                                 text_anchor='middle',
                                 font_family='Noto Sans Mono',
                                 font_size=self.scale))

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

        for x, y, group_name in self.chambers:
            drawing.add(drawing.text(group_name[0],
                                     x=[round((x+0.5)*scale+self.offset_x)],
                                     y=[round((y-1.75)*scale+self.offset_y)],
                                     text_anchor='middle',
                                     font_family='FredokaOne',
                                     font_size=2*scale))
            tangram = self.tangrams.get(group_name)
            if tangram is None:
                continue
            centre_x = round((x + 0.5) * scale + self.offset_x)
            centre_y = (y + 0.5) * scale + self.offset_y
            bounds = tangram.bounds
            tangram.translate(centre_x-drawing['width']//2 -
                              round(bounds[0]+tangram.width/2),
                              -centre_y+drawing['height']//2 -
                              round(bounds[1]+tangram.height/2))
            tangram.draw(drawing)

    def draw_header(self, drawing: Drawing) -> None:
        for x, y, line in ((self.offset_x + round(1.5*self.scale),
                            self.offset_y - round(3*self.scale),
                            'Use a'),
                           (self.offset_x + round(11.5*self.scale),
                            self.offset_y - round(3*self.scale),
                            'to guide you through this maze. What secret word does'),
                           (self.offset_x + round(11.5*self.scale),
                            self.offset_y - round(1.5*self.scale),
                            'the maze turn these letters into?')):
            drawing.add(drawing.text(line,
                                     x=[x],
                                     y=[y],
                                     font_family='FredokaOne',
                                     font_size=round(1.5*self.scale)))
        tangram = Tangram(round(self.scale*5), gap=5)
        tangram.add(tangram.t4a)
        tangram.t4a.rotate(45)
        tangram.add(tangram.t4b)
        tangram.t4b.rotate(135)
        tangram.add(tangram.p)
        tangram.p.flip()
        tangram.p.rotate(45)
        tangram.p.anchor(tangram.t4a, 1, 1)
        tangram.add(tangram.t1a)
        tangram.t1a.rotate(-45)
        tangram.add(tangram.t1b)
        tangram.t1b.rotate(-135)
        tangram.t1b.anchor(tangram.t4b, 2, 1)
        tangram.add(tangram.s)
        tangram.s.rotate(45)
        tangram.s.anchor(tangram.t4a, 0, 2)
        tangram.add(tangram.t2)
        tangram.t2.rotate(90)
        tangram.t2.anchor(tangram.t1b, 2, 2)
        tangram.scale(0.9)
        tangram.translate(-drawing['width']//2, drawing['height']//2)
        tangram.translate(round(self.scale*9),
                          round(self.scale*-4))

        tangram.draw(drawing)
        drawing.add(drawing.text('\u2198',
                                   x=[self.offset_x + round(self.scale*9.94)],
                                   y=[self.offset_y - round(self.scale*1.1)],
                                   fill='white',
                                   text_anchor='middle',
                                   font_family='Noto Sans Mono',
                                   font_size=14))

    def random_walk(self,
                    new_group: str,
                    start_group: str,
                    target_group: str|None = None,
                    retries: int = 0) -> set[tuple[int, int]]:
        if target_group is None:
            target_nodes = self.all_groups
        else:
            target_nodes = self.get_group(target_group)
        start_nodes = list(self.get_group(start_group))
        good_start_nodes = []
        for node in start_nodes:
            if self.find_available_neighbours(node, self.graph, target_nodes):
                good_start_nodes.append(node)
        for retry_count in count():
            location = random.choice(good_start_nodes)
            steps = {location}
            new_graph = self.graph.copy()
            new_nodes = []
            while True:
                neighbours = self.find_available_neighbours(location,
                                                            new_graph,
                                                            target_nodes)
                if not neighbours:
                    # Dead end, fail!
                    steps.clear()
                    break

                # choose a random step
                neighbour = random.choice(neighbours)
                if neighbour in steps:
                    # We retraced a step from the random walk, fail!
                    steps.clear()
                    break

                steps.add(neighbour)
                new_graph.add_edge(location, neighbour)

                if neighbour in target_nodes:
                    # Success!
                    break
                if neighbour in self.all_groups:
                    # Hit a different group, fail!
                    steps.clear()
                    break

                new_nodes.append(neighbour)
                location = neighbour

            if steps:
                # Success!
                logger.info('Found a random walk from %s to %s after %d '
                            'retries.',
                            start_group,
                            target_group,
                            retry_count)
                self.graph = new_graph
                for x, y in new_nodes:
                    self.add_to_group(x, y, new_group)
                return steps

            # Failed. Should we retry?
            if retry_count >= retries:
                # No, return failure.
                logger.info('No random walk found from %s to %s after %d '
                            'retries.',
                            start_group,
                            target_group,
                            retry_count)
                return steps
        assert False, 'Should never fall out of the loop above.'

    def add_step(self,
                 start: tuple[int, int],
                 end: tuple[int, int],
                 group_name: str) -> None:
        self.graph.add_edge(start, end)
        for node in (start, end):
            if node not in self.all_groups:
                self.add_to_group(node[0], node[1], group_name)

    def fill(self) -> None:
        all_nodes = {(x, y)
                     for x in range(self.width)
                     for y in range(self.height)}
        for path_num in count():
            available_nodes = all_nodes - self.all_groups
            if not available_nodes:
                break

            x, y = random.choice(list(available_nodes))
            start_name = f'start{path_num}'
            self.add_to_group(x, y, start_name)
            path_name = f'path{path_num}'
            steps = self.random_walk(path_name, start_name, retries=1000)
            if not steps:
                raise RuntimeError('Failed to fill maze.')

    def find_available_neighbours(self,
                                  node: tuple[int, int],
                                  graph: Graph,
                                  target_nodes: set[tuple[int, int]]) -> list[Any]:
        """ Find all available neighbours for a given node.

        They must not already have a connection to node, and the connection must
        not be forbidden.
        """
        x, y = node
        neighbours = []
        for dx, dy in ((1, 0), (0, -1), (-1, 0), (0, 1)):
            neighbour = (x + dx, y + dy)
            if (graph.has_node(neighbour) and
                    not graph.has_edge(node, neighbour) and
                    not self.is_forbidden_edge(node, neighbour) and
                    (neighbour in target_nodes or
                     neighbour not in self.all_groups)):
                neighbours.append(neighbour)
        return neighbours

    def forbid_edge(self, start: tuple[int, int], end: tuple[int, int]) -> None:
        start2, end2 = sorted((start, end))
        self.forbidden_edges.add((start2, end2))

    def is_forbidden_edge(self,
                          start: tuple[int, int],
                          end: tuple[int, int]) -> bool:
        start2, end2 = sorted((start, end))
        return (start2, end2) in self.forbidden_edges

    def add_tangram(self, tangram: Tangram, group_name: str) -> None:
        self.tangrams[group_name] = tangram


def add_tangrams(maze: Maze):
    tangram = Tangram(50)
    tangram.add(tangram.t1a)
    tangram.add(tangram.t4a)
    tangram.t4a.rotate(-90)
    tangram.add(tangram.p)
    tangram.p.flip()
    tangram.p.anchor(tangram.t1a, 1, 3)
    tangram.add(tangram.s)
    tangram.s.anchor(tangram.p)
    tangram.add(tangram.t4b)
    tangram.t4b.rotate(90)
    tangram.t4b.anchor(tangram.s)
    tangram.add(tangram.t1b)
    tangram.t1b.anchor(tangram.s, 3)
    tangram.add(tangram.t2)
    tangram.t2.rotate(-45)
    tangram.t2.anchor(tangram.t4b, 1)
    tangram.translate(round(tangram.bounds[0] - tangram.width / 2),
                      round(tangram.height / 2 - tangram.bounds[3]))
    maze.add_tangram(tangram, 'T')

    tangram = Tangram(50)
    tangram.add(tangram.t4a)
    tangram.t4a.rotate(135)
    tangram.add(tangram.t1a)
    tangram.t1a.rotate(90)
    tangram.t1a.anchor(tangram.t4a, 2, 2)
    tangram.add(tangram.t4b)
    tangram.t4b.anchor(tangram.t1a, 1, 2)
    tangram.add(tangram.s)
    tangram.s.anchor(tangram.t4b, 0, 1)
    tangram.add(tangram.t2)
    tangram.t2.rotate(90)
    tangram.t2.anchor(tangram.s)
    tangram.add(tangram.t1b)
    tangram.t1b.rotate(45)
    tangram.t1b.anchor(tangram.s, 0, 1)
    tangram.t1b.translate(tangram.width * 0.15, 0)
    tangram.add(tangram.p)
    tangram.p.rotate(45)
    tangram.p.anchor(tangram.t1b, 1, 2)
    maze.add_tangram(tangram, 'R')

    tangram = Tangram(50)
    tangram.add(tangram.p)
    tangram.p.flip()
    tangram.p.rotate(-45)
    tangram.add(tangram.t1a)
    tangram.t1a.rotate(135)
    tangram.t1a.anchor(tangram.p, 2)
    tangram.add(tangram.t1b)
    tangram.t1b.rotate(45)
    tangram.t1b.anchor(tangram.p, 2, 2)
    tangram.add(tangram.s)
    tangram.s.rotate(45)
    tangram.s.anchor(tangram.p, 2, 2)
    tangram.add(tangram.t4a)
    tangram.t4a.rotate(-45)
    tangram.t4a.anchor(tangram.p, 1, 2)
    tangram.add(tangram.t2)
    tangram.t2.rotate(135)
    tangram.t2.anchor(tangram.t1a, 2, 1)
    tangram.add(tangram.t4b)
    tangram.t4b.rotate(-135)
    tangram.t4b.anchor(tangram.t2)
    maze.add_tangram(tangram, 'A')

    tangram = Tangram(50)
    tangram.add(tangram.t4a)
    tangram.t4a.rotate(-135)
    width1 = tangram.width
    tangram.add(tangram.t2)
    tangram.t2.rotate(45)
    tangram.t2.anchor(tangram.t4a, 1, 2)
    tangram.add(tangram.p)
    tangram.p.flip()
    tangram.p.anchor(tangram.t2, 1)
    width2 = tangram.width
    tangram.t2.translate((width1-width2)/2, 0)
    tangram.p.anchor(tangram.t2, 1)
    tangram.add(tangram.t4b)
    tangram.t4b.rotate(-90)
    tangram.t4b.anchor(tangram.t2)
    tangram.add(tangram.s)
    tangram.s.anchor(tangram.t4b, 0, 2)
    tangram.add(tangram.t1a)
    tangram.t1a.rotate(90)
    tangram.t1a.anchor(tangram.t4b, 1, 2)
    tangram.add(tangram.t1b)
    tangram.t1b.rotate(90)
    tangram.t1b.anchor(tangram.t4b, 2, 1)
    maze.add_tangram(tangram, 'C')

    tangram = Tangram(50)
    tangram.add(tangram.s)
    tangram.add(tangram.p)
    tangram.p.flip()
    tangram.p.translate(tangram.width*0.25, 0)
    tangram.add(tangram.t4a)
    tangram.t4a.rotate(45)
    tangram.t4a.anchor(tangram.p, 3, 2)
    tangram.t4a.translate(tangram.width*-0.1, 0)
    tangram.add(tangram.t4b)
    tangram.t4b.rotate(90)
    tangram.t4b.anchor(tangram.t4a, 0, 2)
    tangram.add(tangram.t2)
    tangram.t2.rotate(-90)
    tangram.t2.anchor(tangram.t4b, 0, 1)
    tangram.add(tangram.t1a)
    tangram.t1a.rotate(45)
    tangram.t1a.anchor(tangram.t4b, 1)
    tangram.t1a.translate(tangram.width*-0.02, tangram.width*-0.02)
    tangram.add(tangram.t1b)
    tangram.t1b.rotate(-135)
    tangram.t1b.anchor(tangram.t1a, 1, 2)
    maze.add_tangram(tangram, 'E')

    tangram = Tangram(50)
    tangram.add(tangram.p)
    tangram.add(tangram.t2)
    tangram.t2.rotate(45)
    tangram.t2.anchor(tangram.p, 1)
    h = tangram.height
    tangram.add(tangram.t4a)
    tangram.t4a.rotate(45)
    tangram.t4a.translate(h/2, -tangram.height)
    tangram.add(tangram.t1a)
    tangram.t1a.rotate(135)
    tangram.t1a.anchor(tangram.t4a)
    tangram.add(tangram.t1b)
    tangram.t1b.rotate(-90)
    tangram.t1b.anchor(tangram.t1a, 2, 2)
    tangram.add(tangram.t4b)
    tangram.t4b.rotate(90)
    tangram.t4b.anchor(tangram.t1b, 1, 2)
    tangram.add(tangram.s)
    tangram.s.anchor(tangram.t4b)
    maze.add_tangram(tangram, 'S')


def main() -> None:
    random.seed(0)
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(levelname)s %(message)s')
    logger.info('Starting.')
    maze = Maze(width=56, height=40)
    maze.scale = 20
    maze.offset_x = 10
    maze.offset_y = 140
    group_names = ('TRA', 'CES')
    for y, line in enumerate(group_names):
        for x, group_name in enumerate(line):
            maze.add_chamber(16*x+11.5, 16*y+11.5, group_name)
    add_tangrams(maze)
    legs = []
    text_legs = {
        # start - R
        (2, 0): 'ddruurdrrdruurrrrrrdrddlddrdlldrrrdrdrrrrurdrddrd',
        # R - E
        (30, 14): 'rdldrdlldrrrdrrdrdlldlldrddll',
        # E - C
        (25, 25): 'lululdldlldlldl',
        # C - A
        (12, 32): 'rdrdrdrururruuluurrdrdrrdrdrurdrrrururudddrrdrdrururrdrruuru'
                  'lululuuruuluuuruuuuuluruuullurr',
        # A - S
        # (48, 11): 'rrr',
        (48, 11): 'dddlddrdlddldlldrdrrrrurddrddldldl',
        # T - S
        (9, 14): 'ldrdrdllddddddrdlldlddldlddrrdlddrrdrdrurdrrdrrdrurrrurddrurr'
                 'rulurrdrrrdrrurrddrurrdrrrurrdrrruruulurur',
        # T - end
        (7, 12): 'lldldldddrdlldldrrrurdrdldllddlldlddrdrdlldrrdrrdddrrdlddrurd'
                 'drdrurrurdrdrrrrrurdrrurrdrrrrruurrdldrrurrdrrrrrrrurdrurrrrd'
                 'rrrrrrr',

        # red herrings
        # E - A
        (32, 27): 'ruuuruurdrruuruluuluullurrulluuuuurrrrrrurd',
        # E - T
        (27, 23): 'luluuuulllulluulurruullllldrrddllull',
        # T - C
        (11, 23): 'ruruuuruuuldlu',
        # A - end
        (46, 9): 'rurrdldrrrdllddrdrrdldrrururdddddllddrddrddllldrddrdldrrddlul'
                 'ldldrddrrdddrdll',
        # S - end
        (46, 30): 'ddlddlddrrurrrrddrrrdd'
    }
    for (x, y), leg_text in text_legs.items():
        new_leg = [(x, y)]
        legs.append(new_leg)
        for heading in leg_text:
            if heading == 'l':
                x -= 1
            elif heading == 'r':
                x += 1
            elif heading == 'u':
                y -= 1
            elif heading == 'd':
                y += 1
            new_leg.append((x, y))
            # print(f'({x}, {y}), ', end='')
    neighbour_diffs = {(0, 1): 'd',
                       (0, -1): 'u',
                       (1, 0): 'r',
                       (-1, 0): 'l'}
    for leg in legs:
        print()
        for node, next_node in zip(leg, leg[1:]):

            dx = next_node[0] - node[0]
            dy = next_node[1] - node[1]
            direction = neighbour_diffs.get((dx, dy))
            if direction is not None:
                maze.add_step(node, next_node, 'leg')

    maze.fill()
    image_path = Path(__file__).with_name(
        f'maze.svg')
    drawing = Drawing(size=(1140, 950))
    maze.draw(drawing)
    maze.draw_header(drawing)
    image_path.write_text(drawing.tostring())


if __name__ == '__main__':
    main()
