import svgwrite
from space_tracer import LiveImageDiffer

from tangram import Tangram
from tangram_set import TangramSet
from test_tan import LiveSvg


def create_simple_tangram():
    tangram = Tangram(scale=100)
    tangram.add(tangram.t2)
    tangram.add(tangram.t1a)
    tangram.t1a.anchor(tangram.t2, 0, 2)
    tangram.t1a.rotate(-135)
    return tangram


# noinspection DuplicatedCode
def test_align_gaps(image_differ: LiveImageDiffer):
    expected = svgwrite.Drawing(size=(600, 300))
    tangram1 = create_simple_tangram()
    tangram1.translate(-250, 0)
    tangram2 = create_simple_tangram()
    tangram2.translate(-100, 0)
    tangram3 = create_simple_tangram()
    tangram3.translate(50, 0)

    tangram1.draw(expected)
    tangram2.draw(expected)
    tangram3.draw(expected)

    actual = svgwrite.Drawing(size=(600, 300))
    tangrams = [create_simple_tangram() for _ in range(3)]

    tangram_set = TangramSet(*tangrams)
    bottom = tangram_set.align(top=50, left=-300, right=100)

    tangram_set.draw(actual)

    svg1 = LiveSvg(actual.tostring())
    svg2 = LiveSvg(expected.tostring())
    image_differ.assert_equal(svg1, svg2)
    assert bottom == 0


# noinspection DuplicatedCode
def test_align_bottoms(image_differ: LiveImageDiffer):
    expected = svgwrite.Drawing(size=(600, 300))
    tangram1 = create_simple_tangram()
    tangram1.translate(-250, 0)
    tangram2 = create_simple_tangram()
    tangram2.rotate(45)
    tangram2.translate(-100, 25*Tangram.ROOT2)
    tangram3 = create_simple_tangram()
    tangram3.translate(50, 0)

    tangram1.draw(expected)
    tangram2.draw(expected)
    tangram3.draw(expected)

    actual = svgwrite.Drawing(size=(600, 300))
    tangrams = [create_simple_tangram() for _ in range(3)]
    tangrams[1].rotate(45)

    tangram_set = TangramSet(*tangrams)
    bottom = tangram_set.align(top=50*Tangram.ROOT2, left=-300, right=100)

    tangram_set.draw(actual)

    svg1 = LiveSvg(actual.tostring())
    svg2 = LiveSvg(expected.tostring())
    image_differ.assert_equal(svg1, svg2)
    assert bottom == 0


# noinspection DuplicatedCode
def test_align(image_differ: LiveImageDiffer):
    expected = svgwrite.Drawing(size=(600, 300))
    tangram1 = create_simple_tangram()
    tangram1.translate(-100, 0)

    tangram1.draw(expected)

    actual = svgwrite.Drawing(size=(600, 300))
    tangrams = [create_simple_tangram()]

    tangram_set = TangramSet(*tangrams)
    bottom = tangram_set.align(top=50, left=-300, right=100)

    tangram_set.draw(actual)

    svg1 = LiveSvg(actual.tostring())
    svg2 = LiveSvg(expected.tostring())
    image_differ.assert_equal(svg1, svg2)
    assert bottom == 0
