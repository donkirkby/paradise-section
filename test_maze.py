import random
from textwrap import dedent

import svgwrite
from space_tracer import LiveImageDiffer

from maze import Maze
from test_tan import LiveSvg


def first_choice(seq):
    return seq[0]


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


def test_display_chamber():
    maze = Maze(width=12, height=12)
    maze.add_chamber(5.5, 5.5, 'A')

    expected_display = dedent("""\
        +-+-+-+-+-+-+-+-+-+-+-+-+
        | | | | | | | | | | | | |
        +-+-+-+-+-+-+-+-+-+-+-+-+
        | | | | | | | | | | | | |
        +-+-+-+-+=+ +=+=+-+-+-+-+
        | | | | :       : | | | |
        +-+-+-+-+ + + + +-+-+-+-+
        | | | |           | | | |
        +-+-+=+ + + + + + +=+-+-+
        | | :               : | |
        +-+-+ + + + + + + + +-+-+
        | | :                 | |
        +-+-+ + + + + + + + +-+-+
        | |                 : | |
        +-+-+ + + + + + + + +-+-+
        | | :               : | |
        +-+-+=+ + + + + + +=+-+-+
        | | | |           | | | |
        +-+-+-+-+ + + + +-+-+-+-+
        | | | | :       : | | | |
        +-+-+-+-+=+=+ +=+-+-+-+-+
        | | | | | | | | | | | | |
        +-+-+-+-+-+-+-+-+-+-+-+-+
        | | | | | | | | | | | | |
        +-+-+-+-+-+-+-+-+-+-+-+-+""")

    assert maze.display() == expected_display


def test_display_chamber_with_groups():
    maze = Maze(width=12, height=12)
    maze.add_chamber(5.5, 5.5, 'A')
    maze.add_to_group(1, 2, 'B')

    expected_display = dedent("""\
        +-+-+-+-+-+-+-+-+-+-+-+-+
        | | | | | | | | | | | | |
        +-+-+-+-+-+-+-+-+-+-+-+-+
        | | | | | |A| | | | | | |
        +-+-+-+-+=+ +=+=+-+-+-+-+
        | |B| | :A A A A: | | | |
        +-+-+-+-+ + + + +-+-+-+-+
        | | | |A A A A A A| | | |
        +-+-+=+ + + + + + +=+-+-+
        | | :A A A A A A A A: | |
        +-+-+ + + + + + + + +-+-+
        | | :A A A A A A A A A| |
        +-+-+ + + + + + + + +-+-+
        | |A A A A A A A A A: | |
        +-+-+ + + + + + + + +-+-+
        | | :A A A A A A A A: | |
        +-+-+=+ + + + + + +=+-+-+
        | | | |A A A A A A| | | |
        +-+-+-+-+ + + + +-+-+-+-+
        | | | | :A A A A: | | | |
        +-+-+-+-+=+=+ +=+-+-+-+-+
        | | | | | | |A| | | | | |
        +-+-+-+-+-+-+-+-+-+-+-+-+
        | | | | | | | | | | | | |
        +-+-+-+-+-+-+-+-+-+-+-+-+""")

    assert maze.display(show_groups=True) == expected_display


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


def test_draw_with_chamber(image_differ: LiveImageDiffer):
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
    maze.add_chamber(4.5, 4.5, 'A')
    maze.draw(actual)

    svg1 = LiveSvg(actual.tostring())
    svg2 = LiveSvg(expected.tostring())
    image_differ.assert_equal(svg1, svg2)


def test_add_to_group():
    maze = Maze(width=5, height=3)
    maze.add_to_group(2, 3, 'A1')
    maze.add_to_group(3, 3, 'A1')
    maze.add_to_group(4, 3, 'B1')

    a1_nodes = maze.get_group('A1')

    assert a1_nodes == {(2, 3), (3, 3)}


def test_random_walk(monkeypatch):
    monkeypatch.setattr('random.choice', first_choice)

    maze = Maze(width=5, height=3)
    maze.add_to_group(2, 1, 'start')
    maze.add_to_group(2, 0, 'target')
    steps = maze.random_walk('new', 'start', 'target')

    expected_display = dedent("""\
        +-+-+-+-+-+
        | | |t n n|
        +-+-+-+-+ +
        | | |s n n|
        +-+-+-+-+-+
        | | | | | |
        +-+-+-+-+-+""")

    assert steps == {(2, 1), (3, 1), (4, 1), (4, 0), (3, 0), (2, 0)}
    assert maze.display(show_groups=True) == expected_display


def test_random_walk_with_forbidden_edges(monkeypatch):
    monkeypatch.setattr('random.choice', first_choice)

    maze = Maze(width=5, height=3)
    maze.forbid_edge((3, 1), (4, 1))
    maze.forbid_edge((3, 1), (3, 0))
    maze.add_to_group(2, 1, 'start')
    maze.add_to_group(3, 2, 'target')
    steps = maze.random_walk('new', 'start', 'target')

    expected_display = dedent("""\
        +-+-+-+-+-+
        | | | | | |
        +-+-+-+=+-+
        | | |   : |
        +-+-+-+ +-+
        | | | | | |
        +-+-+-+-+-+""")

    assert steps == {(2, 1), (3, 1), (3, 2)}
    assert maze.display() == expected_display


def test_random_walk_hits_itself(monkeypatch):
    """ This will walk around the perimeter, and hit its own tail. """

    monkeypatch.setattr('random.choice', first_choice)

    maze = Maze(width=5, height=3)
    maze.add_to_group(2, 0, 'start')
    maze.add_to_group(2, 1, 'target')
    steps = maze.random_walk('new', 'start', 'target')

    expected_display = dedent("""\
        +-+-+-+-+-+
        | | | | | |
        +-+-+-+-+-+
        | | | | | |
        +-+-+-+-+-+
        | | | | | |
        +-+-+-+-+-+""")

    assert not steps
    assert maze.display() == expected_display


def test_random_walk_hits_other_group(monkeypatch):
    """ This will walk around the perimeter, and hit its own tail. """

    monkeypatch.setattr('random.choice', first_choice)

    maze = Maze(width=5, height=3)
    maze.add_to_group(0, 1, 'start')
    maze.add_to_group(4, 1, 'target')
    maze.add_to_group(2, 1, 'other')
    steps = maze.random_walk('new', 'start', 'target')

    expected_display = dedent("""\
        +-+-+-+-+-+
        | | | | | |
        +-+-+-+-+-+
        | | | | | |
        +-+-+-+-+-+
        | | | | | |
        +-+-+-+-+-+""")

    assert not steps
    assert maze.display() == expected_display


def test_random_walk_any_target(monkeypatch):
    """ This will walk around the perimeter, and hit its own tail. """

    monkeypatch.setattr('random.choice', first_choice)

    maze = Maze(width=5, height=3)
    maze.add_to_group(0, 1, 'start')
    maze.add_to_group(4, 1, 'A')
    maze.add_to_group(2, 1, 'B')
    steps = maze.random_walk('new', 'start')

    expected_display = dedent("""\
        +-+-+-+-+-+
        | | | | | |
        +-+-+-+-+-+
        |s n B| |A|
        +-+-+-+-+-+
        | | | | | |
        +-+-+-+-+-+""")

    assert steps
    assert maze.display(show_groups=True) == expected_display


def test_fill(monkeypatch):
    monkeypatch.setattr('random.choice', first_choice)

    maze = Maze(width=5, height=3)
    maze.add_to_group(2, 1, 'start')
    maze.fill()

    expected_display = dedent("""\
        +-+-+-+-+-+
        |         |
        + +-+-+-+ +
        |     |   |
        +-+-+-+-+ +
        |         |
        +-+-+-+-+-+""")

    assert maze.display() == expected_display


def test_random_walk_between_chambers(monkeypatch):
    monkeypatch.setattr('random.choice', first_choice)

    maze = Maze(width=30, height=12)
    maze.add_chamber(5.5, 5.5, 'start')
    maze.add_chamber(20.5, 5.5, 'target')
    maze.random_walk('new', 'start', 'target')

    expected_display = dedent("""\
        +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
        | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
        +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
        | | | | | |                               | | | | | | | | | |
        +-+-+-+-+=+ +=+=+-+-+-+-+-+-+-+-+-+-+-+=+ +=+=+-+-+-+-+-+-+-+
        | | | | :       : | | | | | | | | | | :       : | | | | | | |
        +-+-+-+-+ + + + +-+-+-+-+-+-+-+-+-+-+-+ + + + +-+-+-+-+-+-+-+
        | | | |           | | | | | | | | | |           | | | | | | |
        +-+-+=+ + + + + + +=+-+-+-+-+-+-+-+=+ + + + + + +=+-+-+-+-+-+
        | | :               : | | | | | | :               : | | | | |
        +-+-+ + + + + + + + +-+-+-+-+-+-+-+ + + + + + + + +-+-+-+-+-+
        | | :                 | | | | | | :                 | | | | |
        +-+-+ + + + + + + + +-+-+-+-+-+-+-+ + + + + + + + +-+-+-+-+-+
        | |                 : | | | | | |                 : | | | | |
        +-+-+ + + + + + + + +-+-+-+-+-+-+-+ + + + + + + + +-+-+-+-+-+
        | | :               : | | | | | | :               : | | | | |
        +-+-+=+ + + + + + +=+-+-+-+-+-+-+-+=+ + + + + + +=+-+-+-+-+-+
        | | | |           | | | | | | | | | |           | | | | | | |
        +-+-+-+-+ + + + +-+-+-+-+-+-+-+-+-+-+-+ + + + +-+-+-+-+-+-+-+
        | | | | :       : | | | | | | | | | | :       : | | | | | | |
        +-+-+-+-+=+=+ +=+-+-+-+-+-+-+-+-+-+-+-+=+=+ +=+-+-+-+-+-+-+-+
        | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
        +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
        | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
        +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+""")

    assert maze.display() == expected_display


def xtest_draw_random_walk_between_chambers(image_differ: LiveImageDiffer):
    random.seed(1)
    maze = Maze(width=38, height=20)
    maze.add_chamber(7.5, 6.5, 'start')
    maze.add_chamber(27.5, 10.5, 'target')
    expected = svgwrite.Drawing(size=(400, 220))
    maze.offset_x = maze.offset_y = 10
    maze.scale = 10
    maze.draw(expected)

    while True:
        steps = maze.random_walk('new', 'start', 'target')
        if steps:
            break

    actual = svgwrite.Drawing(size=(400, 220))
    maze.draw(actual)

    svg1 = LiveSvg(actual.tostring())
    svg2 = LiveSvg(expected.tostring())
    image_differ.assert_equal(svg1, svg2)


def xtest_draw_filled_maze(image_differ: LiveImageDiffer):
    random.seed(111)
    maze = Maze(width=38, height=20)
    maze.add_chamber(7.5, 6.5, 'A1')
    maze.add_chamber(27.5, 10.5, 'B2')
    maze.add_chamber(16.5, 13.5, 'C3')
    expected = svgwrite.Drawing(size=(400, 220))
    maze.offset_x = maze.offset_y = 10
    maze.scale = 10
    maze.draw(expected)

    while True:
        steps = maze.random_walk('a to b',
                                 'A1',
                                 'B2')
        if steps:
            break
    while True:
        steps = maze.random_walk('b to c',
                                 'B2',
                                 'C3')
        if steps:
            break
    while True:
        steps = maze.random_walk('a to c',
                                 'A1',
                                 'C3')
        if steps:
            break

    maze.fill()

    actual = svgwrite.Drawing(size=(400, 220))
    maze.draw(actual)

    svg1 = LiveSvg(actual.tostring())
    svg2 = LiveSvg(expected.tostring())
    image_differ.assert_equal(svg1, svg2)
