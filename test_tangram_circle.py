import svgwrite
from space_tracer import LiveImageDiffer

from tangram_circle import TangramCircle
from test_tan import LiveSvg
from test_tangram_row import create_simple_tangram


def test_align_gaps(image_differ: LiveImageDiffer):
    expected = svgwrite.Drawing(size=(600, 300))
    tangram1 = create_simple_tangram()
    tangram1.translate(110, -20)
    tangram2 = create_simple_tangram()
    tangram2.translate(10, -120)
    tangram3 = create_simple_tangram()
    tangram3.translate(-90, -20)
    tangram4 = create_simple_tangram()
    tangram4.translate(10, 80)

    tangram1.draw(expected)
    tangram2.draw(expected)
    tangram3.draw(expected)
    tangram4.draw(expected)

    actual = svgwrite.Drawing(size=(600, 300))
    tangrams = [create_simple_tangram() for _ in range(4)]

    tangram_set = TangramCircle(*tangrams)
    tangram_set.align(x=10, y=5, r=100)

    tangram_set.draw(actual)

    svg1 = LiveSvg(actual.tostring())
    svg2 = LiveSvg(expected.tostring())
    image_differ.assert_equal(svg1, svg2)
