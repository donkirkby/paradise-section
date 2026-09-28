import random
from textwrap import dedent

import svgwrite
from space_tracer import LiveImageDiffer

from maze import Maze, draw_arcs
from tangram import Tangram
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
    maze = Maze(width=16, height=16)
    maze.add_chamber(7, 7, 'A')

    expected_display = dedent("""\
        +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
        | | | | | | | | | | | | | | | | |
        +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
        | | | | | | | | | | | | | | | | |
        +-+-+-+-+=+=+=+ +=+=+=+-+-+-+-+-+
        | | | | :             : | | | | |
        +-+-+-+-+ + + + + + + +-+-+-+-+-+
        | | | |                 | | | | |
        +-+-+=+ + + + + + + + + +=+-+-+-+
        | | :                     : | | |
        +-+-+ + + + + + + + + + + +-+-+-+
        | | :                     : | | |
        +-+-+ + + + + + + + + + + +-+-+-+
        | | :                     : | | |
        +-+-+ + + + + + + + + + + +-+-+-+
        | |                         | | |
        +-+-+ + + + + + + + + + + +-+-+-+
        | | :                     : | | |
        +-+-+ + + + + + + + + + + +-+-+-+
        | | :                     : | | |
        +-+-+ + + + + + + + + + + +-+-+-+
        | | :                     : | | |
        +-+-+=+ + + + + + + + + +=+-+-+-+
        | | | |                 | | | | |
        +-+-+-+-+ + + + + + + +-+-+-+-+-+
        | | | | :             : | | | | |
        +-+-+-+-+=+=+=+ +=+=+=+-+-+-+-+-+
        | | | | | | | | | | | | | | | | |
        +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
        | | | | | | | | | | | | | | | | |
        +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
        | | | | | | | | | | | | | | | | |
        +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+""")

    assert maze.display() == expected_display


def test_display_chamber_with_groups():
    maze = Maze(width=15, height=15)
    maze.add_chamber(7, 7, 'A')
    maze.add_to_group(1, 2, 'B')

    expected_display = dedent("""\
        +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
        | | | | | | | | | | | | | | | |
        +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
        | | | | | | | |A| | | | | | | |
        +-+-+-+-+=+=+=+ +=+=+=+-+-+-+-+
        | |B| | :A A A A A A A: | | | |
        +-+-+-+-+ + + + + + + +-+-+-+-+
        | | | |A A A A A A A A A| | | |
        +-+-+=+ + + + + + + + + +=+-+-+
        | | :A A A A A A A A A A A: | |
        +-+-+ + + + + + + + + + + +-+-+
        | | :A A A A A A A A A A A: | |
        +-+-+ + + + + + + + + + + +-+-+
        | | :A A A A A A A A A A A: | |
        +-+-+ + + + + + + + + + + +-+-+
        | |A A A A A A A A A A A A A| |
        +-+-+ + + + + + + + + + + +-+-+
        | | :A A A A A A A A A A A: | |
        +-+-+ + + + + + + + + + + +-+-+
        | | :A A A A A A A A A A A: | |
        +-+-+ + + + + + + + + + + +-+-+
        | | :A A A A A A A A A A A: | |
        +-+-+=+ + + + + + + + + +=+-+-+
        | | | |A A A A A A A A A| | | |
        +-+-+-+-+ + + + + + + +-+-+-+-+
        | | | | :A A A A A A A: | | | |
        +-+-+-+-+=+=+=+ +=+=+=+-+-+-+-+
        | | | | | | | |A| | | | | | | |
        +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
        | | | | | | | | | | | | | | | |
        +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+""")

    assert maze.display(show_groups=True) == expected_display


def test_draw(image_differ: LiveImageDiffer):
    expected = svgwrite.Drawing(size=(200, 200))
    expected.add(expected.line((7, 5),
                               (127, 5),
                               stroke='black',
                               stroke_width=12,
                               stroke_linecap='round'))
    expected.add(expected.line((187, 5),
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
                               (67, 125),
                               stroke='black',
                               stroke_width=12,
                               stroke_linecap='round'))
    expected.add(expected.line((7, 125),
                               (7, 125),
                               stroke='black',
                               stroke_width=12,
                               stroke_linecap='round'))
    expected.add(expected.line((7, 5),
                               (7, 125),
                               stroke='black',
                               stroke_width=12,
                               stroke_linecap='round'))
    expected.add(expected.text(Maze.ARROW,
                               x=[157],
                               y=[43],
                               text_anchor='middle',
                               font_family='Noto Sans Mono',
                               font_size=60))
    expected.add(expected.text(Maze.ARROW,
                               x=[37],
                               y=[127],
                               text_anchor='middle',
                               font_family='Noto Sans Mono',
                               font_size=60))
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
                               (127, 5),
                               stroke='black',
                               stroke_width=12,
                               stroke_linecap='round'))
    expected.add(expected.line((187, 5),
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
                               (67, 125),
                               stroke='black',
                               stroke_width=12,
                               stroke_linecap='round'))
    expected.add(expected.line((7, 125),
                               (7, 125),
                               stroke='black',
                               stroke_width=12,
                               stroke_linecap='round'))
    expected.add(expected.line((7, 5),
                               (7, 125),
                               stroke='black',
                               stroke_width=12,
                               stroke_linecap='round'))
    expected.add(expected.text(Maze.ARROW,
                               x=[157],
                               y=[43],
                               text_anchor='middle',
                               font_family='Noto Sans Mono',
                               font_size=60))
    expected.add(expected.text(Maze.ARROW,
                               x=[37],
                               y=[127],
                               text_anchor='middle',
                               font_family='Noto Sans Mono',
                               font_size=60))
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


def test_draw_arcs(image_differ: LiveImageDiffer):
    expected = svgwrite.Drawing(size=(220, 220))
    expected.add(expected.path('M 110 110 '
                               'm 50 0 '
                               'm -50 -50'
                               'a 50 50 0 0 0 -50 50 '
                               'm 50 50 '
                               'a 50 50 0 0 0 50 -50',
                               stroke='black',
                               fill='white',
                               stroke_width=2))

    actual = svgwrite.Drawing(size=(220, 220))
    draw_arcs((110, 110),
              50,
              [90, 180, 270, 360],
              actual,
              stroke='black',
              stroke_width=2,
              fill='none')

    svg1 = LiveSvg(actual.tostring())
    svg2 = LiveSvg(expected.tostring())
    image_differ.assert_equal(svg1, svg2)


def test_draw_with_chamber(image_differ: LiveImageDiffer):
    expected = svgwrite.Drawing(size=(220, 220))
    maze1 = Maze(width=19, height=19)
    maze1.scale = 10
    maze1.offset_x = maze1.offset_y = 10
    for x, y in ((6, 4), (7, 4), (8, 4), (9, 4), (10, 4), (11, 4),
                 (5, 5), (6, 5), (7, 5), (8, 5), (9, 5), (10, 5), (11, 5), (12, 5),
                 (6, 6), (7, 6), (8, 6), (9, 6), (10, 6), (11, 6), (12, 6), (13, 6),
                 (7, 7), (8, 7), (9, 7), (10, 7), (11, 7), (12, 7), (13, 7),
                 (8, 8), (9, 8), (10, 8), (11, 8), (12, 8), (13, 8),
                 (9, 9), (10, 9), (11, 9), (12, 9), (13, 9), (14, 9),
                 (10, 10), (11, 10), (12, 10), (13, 10),
                 (11, 11), (12, 11), (13, 11),
                 (12, 12), (13, 12)):
        maze1.graph.add_edge((x, y), (x+1, y))
        maze1.graph.add_edge((y, x), (y, x+1))
    for x, y in ((9, 3),
                 (6, 4), (7, 4), (8, 4), (9, 4), (10, 4), (11, 4), (12, 4),
                 (6, 5), (7, 5), (8, 5), (9, 5), (10, 5), (11, 5), (12, 5), (13, 5),
                 (7, 6), (8, 6), (9, 6), (10, 6), (11, 6), (12, 6), (13, 6), (14, 6),
                 (8, 7), (9, 7), (10, 7), (11, 7), (12, 7), (13, 7), (14, 7),
                 (9, 8), (10, 8), (11, 8), (12, 8), (13, 8), (14, 8),
                 (10, 9), (11, 9), (12, 9), (13, 9), (14, 9),
                 (11, 10), (12, 10), (13, 10), (14, 10),
                 (12, 11), (13, 11), (14, 11),
                 (13, 12)):
        maze1.graph.add_edge((x, y), (x, y+1))
        maze1.graph.add_edge((y, x), (y+1, x))
    maze1.draw(expected)
    r = 56
    theta = 6
    draw_arcs((105, 105),
              r,
              [theta, 45-theta,
               45+theta, 90-theta,
               90+theta, 135-theta,
               135+theta, 180-theta,
               180+theta, 225-theta,
               225+theta, 270-theta,
               270+theta, 315-theta,
               315+theta, 360-theta],
              expected,
              fill='none',
              stroke='black',
              stroke_width=2,
              stroke_linecap='round')
    expected.add(expected.text('A',x=[105],
                               y=[75],
                               text_anchor='middle',
                               font_family='FredokaOne',
                               font_size=25))

    actual = svgwrite.Drawing(size=(220, 220))

    maze = Maze(width=19, height=19)
    maze.offset_x = maze.offset_y = 10
    maze.scale = 10
    maze.add_chamber(9, 9, 'A')
    maze.draw(actual)

    svg1 = LiveSvg(actual.tostring())
    svg2 = LiveSvg(expected.tostring())
    image_differ.assert_equal(svg1, svg2)


def test_draw_with_tangram(image_differ: LiveImageDiffer):
    expected = svgwrite.Drawing(size=(220, 220))
    maze1 = Maze(width=17, height=17)
    maze1.scale = 12
    maze1.offset_x = maze1.offset_y = 5
    maze1.add_chamber(8, 10, 'A')
    maze1.draw(expected)
    tangram = Tangram(35)
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
    tangram.translate(round(tangram.bounds[0] - tangram.width / 2 - 3),
                      round(tangram.height / 2 - tangram.bounds[3] - 25))

    tangram.draw(expected)

    tangram.translate(100, 100)  # So it needs to be adjusted.

    actual = svgwrite.Drawing(size=(220, 220))

    maze = Maze(width=17, height=17)
    maze.offset_x = maze.offset_y = 5
    maze.scale = 12
    maze.add_chamber(8, 10, 'A')
    maze.add_tangram(tangram, 'A')
    maze.draw(actual)

    svg1 = LiveSvg(actual.tostring())
    svg2 = LiveSvg(expected.tostring())
    image_differ.assert_equal(svg1, svg2)


def test_draw_header(image_differ: LiveImageDiffer):
    expected = svgwrite.Drawing(size=(600, 220))
    for x, y, line in ((20, 40, 'Use a'),
                       (120, 40, 'to guide you through this maze. What secret word does'),
                       (120, 55, 'the maze turn these letters into?')):

        expected.add(expected.text(line,
                                   x=[x],
                                   y=[y],
                                   font_family='FredokaOne',
                                   font_size=15))
    maze1 = Maze(width=56, height=10)
    maze1.scale = 10
    maze1.offset_x = 5
    maze1.offset_y = 70
    maze1.draw(expected)
    tangram = Tangram(50, gap=5)
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
    tangram.translate(-210,
                      70)

    tangram.draw(expected)
    expected.add(expected.text('\u2198',
                               x=[104],
                               y=[59],
                               fill='white',
                               text_anchor='middle',
                               font_family='Noto Sans Mono',
                               font_size=14))

    actual = svgwrite.Drawing(size=(600, 220))

    maze = Maze(width=56, height=10)
    maze.offset_x = 5
    maze.offset_y = 70
    maze.scale = 10
    maze.draw(actual)
    maze.draw_header(actual)

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


def test_add_step():
    maze = Maze(width=5, height=3)
    maze.add_step((4, 2), (4, 1), 'steps')

    expected_display = dedent("""\
        +-+-+-+-+-+
        | | | | | |
        +-+-+-+-+-+
        | | | | |s|
        +-+-+-+-+ +
        | | | | |s|
        +-+-+-+-+-+""")

    assert maze.display(show_groups=True) == expected_display


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

    assert steps == [(2, 1), (3, 1), (4, 1), (4, 0), (3, 0), (2, 0)]
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

    assert steps == [(2, 1), (3, 1), (3, 2)]
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
        | |n n n n|
        +-+ +-+-+ +
        |s n|o| |t|
        +-+-+-+-+-+
        | | | | | |
        +-+-+-+-+-+""")

    assert steps == [(0, 1), (1, 1), (1, 0), (2, 0), (3, 0), (4, 0), (4, 1)]
    assert maze.display(show_groups=True) == expected_display


def test_random_walk_dead_end(monkeypatch):
    """ This will walk around the perimeter, and hit its own tail. """

    monkeypatch.setattr('random.choice', first_choice)

    maze = Maze(width=5, height=3)
    maze.add_to_group(0, 0, 'start')
    maze.add_to_group(2, 1, 'target')
    maze.add_to_group(4, 1, 'other')
    steps = maze.random_walk('new', 'start', 'target')

    expected_display = dedent("""\
        +-+-+-+-+-+
        |s| | | | |
        +-+-+-+-+-+
        | | |t| |o|
        +-+-+-+-+-+
        | | | | | |
        +-+-+-+-+-+""")

    assert not steps
    assert maze.display(show_groups=True) == expected_display


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

    maze = Maze(width=34, height=16)
    maze.add_chamber(7, 7, 'start')
    maze.add_chamber(22, 7, 'target')
    maze.random_walk('new', 'start', 'target')

    expected_display = dedent("""\
        +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
        | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
        +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
        | | | | | | | |                               | | | | | | | | | | | |
        +-+-+-+-+=+=+=+ +=+=+=+-+-+-+-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+-+-+-+
        | | | | :             : | | | | | | | :             : | | | | | | | |
        +-+-+-+-+ + + + + + + +-+-+-+-+-+-+-+-+ + + + + + + +-+-+-+-+-+-+-+-+
        | | | |                 | | | | | | |                 | | | | | | | |
        +-+-+=+ + + + + + + + + +=+-+-+-+-+-+ + + + + + + + + +-+-+-+-+-+-+-+
        | | :                     : | | | :                     : | | | | | |
        +-+-+ + + + + + + + + + + +-+-+-+-+ + + + + + + + + + + +-+-+-+-+-+-+
        | | :                     : | | | :                     : | | | | | |
        +-+-+ + + + + + + + + + + +-+-+-+-+ + + + + + + + + + + +-+-+-+-+-+-+
        | | :                     : | | | :                     : | | | | | |
        +-+-+ + + + + + + + + + + +-+-+-+-+ + + + + + + + + + + +-+-+-+-+-+-+
        | |                         | | |                         | | | | | |
        +-+-+ + + + + + + + + + + +-+-+-+-+ + + + + + + + + + + +-+-+-+-+-+-+
        | | :                     : | | | :                     : | | | | | |
        +-+-+ + + + + + + + + + + +-+-+-+-+ + + + + + + + + + + +-+-+-+-+-+-+
        | | :                     : | | | :                     : | | | | | |
        +-+-+ + + + + + + + + + + +-+-+-+-+ + + + + + + + + + + +-+-+-+-+-+-+
        | | :                     : | | | :                     : | | | | | |
        +-+-+=+ + + + + + + + + +=+-+-+-+-+-+ + + + + + + + + +-+-+-+-+-+-+-+
        | | | |                 | | | | | | |                 | | | | | | | |
        +-+-+-+-+ + + + + + + +-+-+-+-+-+-+-+-+ + + + + + + +-+-+-+-+-+-+-+-+
        | | | | :             : | | | | | | | :             : | | | | | | | |
        +-+-+-+-+=+=+=+ +=+=+=+-+-+-+-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+-+-+-+
        | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
        +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
        | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
        +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
        | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
        +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+""")

    assert maze.display() == expected_display


def xtest_draw_leg(image_differ: LiveImageDiffer):
    maze = Maze(width=56, height=40)
    group_names = ('TRA', 'CES')
    for y, line in enumerate(group_names):
        for x, group_name in enumerate(line):
            maze.add_chamber(16*x+11.5, 16*y+11.5, group_name)
    expected = svgwrite.Drawing(size=(570, 410))
    maze.offset_x = maze.offset_y = 5
    maze.scale = 10
    maze.draw(expected)

    actual = svgwrite.Drawing(size=(570, 410))
    legs = [
        # [(30, 14), (30, 15), (29, 17), (30, 16), (31, 14), (29, 18), (31, 15), (30, 17), (31, 16), (30, 18), (31, 17),
        #  (27, 23), (31, 18), (28, 23), (32, 18), (29, 23), (32, 19), (30, 23), (31, 22), (33, 19), (31, 23), (32, 22),
        #  (34, 19), (33, 21), (34, 20), (33, 22), (34, 21), (35, 20), (35, 21)]

    ]
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
    print()
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
                print(direction, end='')
            else:
                x1, y1 = node
                x2, y2 = next_node
                actual.add(actual.line(((x1+0.5)*maze.scale+maze.offset_x,
                                        (y1+0.5)*maze.scale+maze.offset_y),
                                       ((x2+0.5)*maze.scale+maze.offset_x,
                                        (y2+0.5)*maze.scale+maze.offset_y),
                                       stroke='red'))

    maze.add_to_group(35, 15, 'custom-start')
    maze.add_to_group(15, 5, 'custom-target')
    try:
        maze.random_walk('custom-leg',
                         'T',
                         'custom-target',
                         retries=1000)
    except IndexError:
        pass

    # maze.fill()
    maze.draw(actual)

    svg1 = LiveSvg(actual.tostring())
    svg2 = LiveSvg(expected.tostring())
    image_differ.assert_equal(svg1, svg2)


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
