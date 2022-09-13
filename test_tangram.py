import svgwrite
from space_tracer import LiveImageDiffer

from tangram import Tangram
from test_tan import LiveSvg


# noinspection DuplicatedCode
def test_draw(image_differ: LiveImageDiffer):
    expected = svgwrite.Drawing(size=(200, 200))
    expected.add(expected.polygon([(100, 100), (200, 100), (100, 0)],
                                  fill='black',
                                  stroke='black'))

    actual = svgwrite.Drawing(size=(200, 200))

    tangram = Tangram()
    tangram.scale(400/Tangram.ROOT2)
    tangram.add(tangram.t1a)
    tangram.draw(actual)

    svg1 = LiveSvg(actual.tostring())
    svg2 = LiveSvg(expected.tostring())
    image_differ.assert_equal(svg1, svg2)


def test_draw_trimmed(image_differ: LiveImageDiffer):
    expected = svgwrite.Drawing(size=(200, 200))
    expected.add(expected.polygon([(103, 97), (200 - 7.24, 97), (103, 7.24)],
                                  fill='black',
                                  stroke='black'))

    actual = svgwrite.Drawing(size=(200, 200))

    tangram = Tangram(scale=400/Tangram.ROOT2, gap=6)
    tangram.add(tangram.t1a)
    tangram.draw(actual)

    svg1 = LiveSvg(actual.tostring())
    svg2 = LiveSvg(expected.tostring())
    image_differ.assert_equal(svg1, svg2)


def test_draw_square(image_differ: LiveImageDiffer):
    expected = svgwrite.Drawing(size=(200, 200))
    expected.add(expected.polygon([(100, 100), (150, 100), (150, 50), (100, 50)],
                                  fill='black',
                                  stroke='black'))

    actual = svgwrite.Drawing(size=(200, 200))

    tangram = Tangram()
    tangram.scale(200/Tangram.ROOT2)
    tangram.add(tangram.s)
    tangram.draw(actual)

    svg1 = LiveSvg(actual.tostring())
    svg2 = LiveSvg(expected.tostring())
    image_differ.assert_equal(svg1, svg2)


def test_draw_square_gap(image_differ: LiveImageDiffer):
    expected = svgwrite.Drawing(size=(200, 200))
    expected.add(expected.polygon([(103, 97), (147, 97), (147, 53), (103, 53)],
                                  fill='black',
                                  stroke='black'))

    actual = svgwrite.Drawing(size=(200, 200))

    tangram = Tangram(scale=200/Tangram.ROOT2, gap=6)
    tangram.add(tangram.s)
    tangram.draw(actual)

    svg1 = LiveSvg(actual.tostring())
    svg2 = LiveSvg(expected.tostring())
    image_differ.assert_equal(svg1, svg2)


def test_draw_both_triangles(image_differ: LiveImageDiffer):
    expected = svgwrite.Drawing(size=(200, 200))
    expected.add(expected.polygon([(100, 100), (200, 100), (100, 0)],
                                  fill='black',
                                  stroke='black'))
    expected.add(expected.polygon([(0, 100), (100, 100), (0, 0)],
                                  fill='black',
                                  stroke='black'))

    actual = svgwrite.Drawing(size=(200, 200))

    tangram = Tangram()
    tangram.scale(400/Tangram.ROOT2)
    tangram.add(tangram.t1a)
    tangram.add(tangram.t1b)
    tangram.t1b.translate(-100, 0)
    tangram.draw(actual)

    svg1 = LiveSvg(actual.tostring())
    svg2 = LiveSvg(expected.tostring())
    image_differ.assert_equal(svg1, svg2)


# noinspection DuplicatedCode
def test_draw_triangle_sizes(image_differ: LiveImageDiffer):
    root2 = Tangram.ROOT2
    expected = svgwrite.Drawing(size=(200, 200))
    expected.add(expected.polygon([(100, 100), (125, 100), (100, 75)],
                                  fill='black',
                                  stroke='black'))
    expected.add(expected.polygon([(0, 100), (25*root2, 100), (0, 100-25*root2)],
                                  fill='black',
                                  stroke='black'))
    expected.add(expected.polygon([(0, 200), (50, 200), (0, 150)],
                                  fill='black',
                                  stroke='black'))

    actual = svgwrite.Drawing(size=(200, 200))

    tangram = Tangram()
    tangram.scale(100/Tangram.ROOT2)
    tangram.add(tangram.t1a)
    tangram.add(tangram.t2)
    tangram.add(tangram.t4a)
    tangram.t4a.translate(-100, -100)
    tangram.t2.translate(-100, 0)
    tangram.draw(actual)

    svg1 = LiveSvg(actual.tostring())
    svg2 = LiveSvg(expected.tostring())
    old_tolerance = image_differ.tolerance
    image_differ.tolerance = 5
    try:
        image_differ.assert_equal(svg1, svg2)
    finally:
        image_differ.tolerance = old_tolerance


# noinspection DuplicatedCode
def test_draw_triangles_gap(image_differ: LiveImageDiffer):
    expected = svgwrite.Drawing(size=(200, 200))
    expected.add(expected.polygon([(102, 98), (120.17, 98), (102, 79.83)],
                                  fill='black',
                                  stroke='black'))
    expected.add(expected.polygon([(98, 98),
                                   (98, 69.475),
                                   (69.475, 98)],
                                  fill='black',
                                  stroke='black'))
    expected.add(expected.polygon([(98, 102),
                                   (98, 145.17),
                                   (54.83, 102)],
                                  fill='black',
                                  stroke='black'))

    actual = svgwrite.Drawing(size=(200, 200))

    tangram = Tangram(scale=100/Tangram.ROOT2, gap=4)
    tangram.add(tangram.t1a)
    tangram.add(tangram.t2)
    tangram.add(tangram.t4a)
    tangram.t2.rotate(90)
    tangram.t4a.rotate(180)
    print(tangram.t2.display.points)
    tangram.draw(actual)

    svg1 = LiveSvg(actual.tostring())
    svg2 = LiveSvg(expected.tostring())
    old_tolerance = image_differ.tolerance
    image_differ.tolerance = 5
    try:
        image_differ.assert_equal(svg1, svg2)
    finally:
        image_differ.tolerance = old_tolerance


def test_draw_parallelogram(image_differ: LiveImageDiffer):
    expected = svgwrite.Drawing(size=(200, 200))
    expected.add(expected.polygon([(100, 100), (200, 100), (100, 0), (0, 0)],
                                  fill='black',
                                  stroke='black'))

    actual = svgwrite.Drawing(size=(200, 200))

    tangram = Tangram(scale=400/Tangram.ROOT2)
    tangram.add(tangram.p)
    tangram.draw(actual)

    svg1 = LiveSvg(actual.tostring())
    svg2 = LiveSvg(expected.tostring())
    image_differ.assert_equal(svg1, svg2)


def test_draw_gap(image_differ: LiveImageDiffer):
    expected = svgwrite.Drawing(size=(200, 200))
    expected.add(expected.polygon([(103, 97), (200 - 7.24, 97), (103, 7.24)],
                                  fill='black',
                                  stroke='black'))
    expected.add(expected.polygon([(3, 97), (97, 97), (97, 3), (3, 3)],
                                  fill='black',
                                  stroke='black'))

    actual = svgwrite.Drawing(size=(200, 200))

    tangram = Tangram(scale=400/Tangram.ROOT2, gap=6)
    tangram.add(tangram.t1a)
    tangram.add(tangram.s)
    tangram.s.translate(-100, 0)
    tangram.draw(actual)

    svg1 = LiveSvg(actual.tostring())
    svg2 = LiveSvg(expected.tostring())
    old_tolerance = image_differ.tolerance
    image_differ.tolerance = 5
    try:
        image_differ.assert_equal(svg1, svg2)
    finally:
        image_differ.tolerance = old_tolerance


def test_draw_parallelogram_gap(image_differ: LiveImageDiffer):
    expected = svgwrite.Drawing(size=(200, 200))
    expected.add(expected.polygon([(102, 98), (194, 98), (98, 2), (6, 2)],
                                  fill='black',
                                  stroke='black'))

    actual = svgwrite.Drawing(size=(200, 200))

    tangram = Tangram(scale=400/Tangram.ROOT2, gap=4)
    tangram.add(tangram.p)
    tangram.draw(actual)

    svg1 = LiveSvg(actual.tostring())
    svg2 = LiveSvg(expected.tostring())
    image_differ.assert_equal(svg1, svg2)


# noinspection DuplicatedCode
def test_anchor(image_differ: LiveImageDiffer):
    expected = svgwrite.Drawing(size=(200, 200))
    tangram1 = Tangram(scale=100)
    tangram1.add(tangram1.t1a)
    tangram1.add(tangram1.t2)
    tangram1.t1a.translate(-25*tangram1.ROOT2, 50)
    tangram1.draw(expected)

    actual = svgwrite.Drawing(size=(200, 200))
    tangram2 = Tangram(scale=100)
    tangram2.add(tangram2.t1a)
    tangram2.add(tangram2.t2)
    tangram2.t1a.anchor(tangram2.t2, target_point=2, moving_point=1)
    tangram2.draw(actual)

    svg1 = LiveSvg(actual.tostring())
    svg2 = LiveSvg(expected.tostring())
    image_differ.assert_equal(svg1, svg2)


# noinspection DuplicatedCode
def test_anchor_and_rotate(image_differ: LiveImageDiffer):
    expected = svgwrite.Drawing(size=(200, 200))
    tangram1 = Tangram(scale=100)
    tangram1.add(tangram1.t1a)
    tangram1.t1a.rotate(90)
    tangram1.add(tangram1.t2)
    tangram1.t1a.translate(0, 50-25*tangram1.ROOT2)
    tangram1.draw(expected)

    actual = svgwrite.Drawing(size=(200, 200))
    tangram = Tangram(scale=100)
    tangram.add(tangram.t1a)
    tangram.add(tangram.t2)
    tangram.t1a.anchor(tangram.t2, target_point=2, moving_point=1)
    tangram.t1a.rotate(90)
    tangram.draw(actual)

    svg1 = LiveSvg(actual.tostring())
    svg2 = LiveSvg(expected.tostring())
    image_differ.assert_equal(svg1, svg2)


# noinspection DuplicatedCode
def test_translate(image_differ: LiveImageDiffer):
    expected = svgwrite.Drawing(size=(200, 200))
    tangram1 = Tangram(scale=100)
    tangram1.add(tangram1.t1a)
    tangram1.add(tangram1.t2)
    tangram1.t1a.translate(-25*tangram1.ROOT2-50, 50)
    tangram1.t2.translate(-50, 0)
    tangram1.draw(expected)

    actual = svgwrite.Drawing(size=(200, 200))
    tangram2 = Tangram(scale=100)
    tangram2.add(tangram2.t1a)
    tangram2.add(tangram2.t2)
    tangram2.t1a.anchor(tangram2.t2, target_point=2, moving_point=1)
    tangram2.translate(-50, 0)
    tangram2.draw(actual)

    svg1 = LiveSvg(actual.tostring())
    svg2 = LiveSvg(expected.tostring())
    image_differ.assert_equal(svg1, svg2)


# noinspection DuplicatedCode
def test_rotate(image_differ: LiveImageDiffer):
    expected = svgwrite.Drawing(size=(200, 200))
    tangram1 = Tangram(scale=100)
    tangram1.add(tangram1.t1a)
    tangram1.add(tangram1.t2)
    tangram1.t1a.translate(-25*tangram1.ROOT2, 10)
    tangram1.t2.translate(0, -40)
    tangram1.t1a.rotate(90, anchor_point=(0, 10))
    tangram1.t2.rotate(90, anchor_point=(0, 10))
    tangram1.draw(expected)

    actual = svgwrite.Drawing(size=(200, 200))
    tangram2 = Tangram(scale=100)
    tangram2.add(tangram2.t1a)
    tangram2.add(tangram2.t2)
    tangram2.t2.translate(0, -40)
    tangram2.t1a.anchor(tangram2.t2, target_point=2, moving_point=1)
    tangram2.rotate(90)
    tangram2.draw(actual)

    svg1 = LiveSvg(actual.tostring())
    svg2 = LiveSvg(expected.tostring())
    image_differ.assert_equal(svg1, svg2)
