import math
import random
from collections import defaultdict
from itertools import count
from typing import Any

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

    def random_walk(self,
                    new_group: str,
                    start_group: str,
                    target_group: str|None = None) -> set[tuple[int, int]]:
        start_nodes = list(self.get_group(start_group))
        good_start_nodes = []
        for node in start_nodes:
            if self.find_available_neighbours(node, self.graph):
                good_start_nodes.append(node)
        if target_group is None:
            target_nodes = self.all_groups
        else:
            target_nodes = self.get_group(target_group)
        location = random.choice(good_start_nodes)
        steps = {location}
        new_graph = self.graph.copy()
        new_nodes = []
        while True:
            neighbours = self.find_available_neighbours(location, new_graph)
            # choose a random step
            neighbour = random.choice(neighbours)
            if neighbour in steps:
                # We retraced a step from the random walk, fail!
                return set()

            steps.add(neighbour)
            new_graph.add_edge(location, neighbour)

            if neighbour in target_nodes:
                # Success!
                break
            if neighbour in self.all_groups:
                # Hit a different group, fail!
                return set()

            new_nodes.append(neighbour)
            location = neighbour

        self.graph = new_graph
        for x, y in new_nodes:
            self.add_to_group(x, y, new_group)
        return steps

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
            while True:
                path_name = f'path{path_num}'
                steps = self.random_walk(path_name, start_name)
                if steps:
                    break

    def find_available_neighbours(self, node, graph: Graph) -> list[Any]:
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
                    not self.is_forbidden_edge(node, neighbour)):
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