from textwrap import dedent

import svgwrite
from space_tracer import LiveImageDiffer

from maze import Maze
from test_tan import LiveSvg


def test_display_blank():
    maze = Maze(width=5, height=3)

    expected_display = dedent("""\
        +-+-+-+-+-+
        | | | | | |
        +-+-+-+-+-+
        | | | | | |
        +-+-+-+-+-+
        | | | | | |
        +-+-+-+-+-+""")

    assert maze.display() == expected_display


def test_display_walls():
    expected_display = dedent("""\
        +-+-+-+-+-+
        | |   |   |
        +-+-+ + +-+
        | | |     |
        +-+-+ +-+-+
        |     | | |
        +-+-+-+-+-+""")

    maze = Maze(text=expected_display)

    assert maze.display() == expected_display


def test_draw(image_differ: LiveImageDiffer):
    expected = svgwrite.Drawing(size=(200, 200))
    expected.add(expected.line((7, 5),
                               (187, 5),
                               stroke='black',
                               stroke_width=12,
                               stroke_linecap='round'))
    expected.add(expected.line((187, 5),
                               (187, 125),
                               stroke='black',
                               stroke_width=12,
                               stroke_linecap='round'))
    expected.add(expected.line((187, 125),
                               (7, 125),
                               stroke='black',
                               stroke_width=12,
                               stroke_linecap='round'))
    expected.add(expected.line((7, 5),
                               (7, 125),
                               stroke='black',
                               stroke_width=12,
                               stroke_linecap='round'))
    for x in range(7, 188, 60):
        for y in range(5, 126, 60):
            if 7 < x < 187 and y < 125:
                expected.add(expected.line((x, y),
                                           (x, y+60),
                                           stroke='black',
                                           stroke_width=12,
                                           stroke_linecap='round'))
            if x < 187 and 5 < y < 125:
                expected.add(expected.line((x, y),
                                           (x+60, y),
                                           stroke='black',
                                           stroke_width=12,
                                           stroke_linecap='round'))

    actual = svgwrite.Drawing(size=(200, 200))

    maze = Maze(width=3, height=2)
    maze.offset_x = 7
    maze.offset_y = 5
    maze.scale = 60
    maze.draw(actual)

    svg1 = LiveSvg(actual.tostring())
    svg2 = LiveSvg(expected.tostring())
    image_differ.assert_equal(svg1, svg2)


def test_draw_with_path(image_differ: LiveImageDiffer):
    expected = svgwrite.Drawing(size=(200, 200))
    expected.add(expected.line((7, 5),
                               (187, 5),
                               stroke='black',
                               stroke_width=12,
                               stroke_linecap='round'))
    expected.add(expected.line((187, 5),
                               (187, 125),
                               stroke='black',
                               stroke_width=12,
                               stroke_linecap='round'))
    expected.add(expected.line((187, 125),
                               (7, 125),
                               stroke='black',
                               stroke_width=12,
                               stroke_linecap='round'))
    expected.add(expected.line((7, 5),
                               (7, 125),
                               stroke='black',
                               stroke_width=12,
                               stroke_linecap='round'))
    for x in range(7, 188, 60):
        for y in range(5, 126, 60):
            if 7 < x < 187 and y < 125 and (x, y) not in ((127, 5), ):
                expected.add(expected.line((x, y),
                                           (x, y+60),
                                           stroke='black',
                                           stroke_width=12,
                                           stroke_linecap='round'))
            if x < 187 and 5 < y < 125 and (x, y) not in ((127, 65), ):
                expected.add(expected.line((x, y),
                                           (x+60, y),
                                           stroke='black',
                                           stroke_width=12,
                                           stroke_linecap='round'))

    actual = svgwrite.Drawing(size=(200, 200))

    maze = Maze(text=dedent("""\
        +-+-+-+
        | |   |
        +-+-+ +
        | | | |
        +-+-+-+"""))
    maze.offset_x = 7
    maze.offset_y = 5
    maze.scale = 60
    maze.draw(actual)

    svg1 = LiveSvg(actual.tostring())
    svg2 = LiveSvg(expected.tostring())
    image_differ.assert_equal(svg1, svg2)


def test_draw_with_diagonal_chamber(image_differ: LiveImageDiffer):
    expected = svgwrite.Drawing(size=(220, 220))
    maze1 = Maze(width=10, height=10)
    maze1.scale = 20
    maze1.offset_x = maze1.offset_y = 10
    for x, y in ((3, 1), (4, 1), (5, 1),
                 (2, 2), (3, 2), (4, 2), (5, 2), (6, 2),
                 (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3), (7, 3),
                 (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4), (7, 4), (8, 4),
                 (0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5), (7, 5),
                 (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6),
                 (2, 7), (3, 7), (4, 7), (5, 7), (6, 7),
                 (3, 8), (4, 8), (5, 8)):
        maze1.graph.add_edge((x, y), (x+1, y))
    for x, y in ((4, 0), (3, 1), (4, 1), (5, 1), (6, 1),
                 (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2),
                 (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3), (7, 3), (8, 3),
                 (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4), (7, 4), (8, 4),
                 (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5), (7, 5), (8, 5),
                 (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6),
                 (3, 7), (4, 7), (5, 7), (6, 7), (5, 8)):
        maze1.graph.add_edge((x, y), (x, y+1))
    maze1.draw(expected)
    expected.add(expected.path('M 30 90 L 50 70'
                               'M 70 50 L 90 30'
                               'M 130 30 L 150 50'
                               'M 170 70 L 190 90'
                               'M 190 130 L 170 150'
                               'M 150 170 L 130 190'
                               'M 90 190 L 70 170'
                               'M 50 150 L 30 130',
                               stroke='black',
                               fill='none',
                               stroke_width=4,
                               stroke_linecap='round'))

    actual = svgwrite.Drawing(size=(220, 220))

    maze = Maze(width=10, height=10)
    maze.offset_x = maze.offset_y = 10
    maze.scale = 20
    maze.add_chamber(4.5, 4.5)
    maze.draw(actual)

    svg1 = LiveSvg(actual.tostring())
    svg2 = LiveSvg(expected.tostring())
    image_differ.assert_equal(svg1, svg2)
