from io import StringIO
from pathlib import Path

import svgwrite
from reportlab.graphics import renderPM
from svglib.svglib import svg2rlg

from tangram import Tangram
from tangram_circle import TangramCircle


class TangramRat(Tangram):
    def __init__(self, scale=1, gap=0):
        super().__init__(scale, gap)
        self.add(self.s)
        self.s.rotate(45)
        self.add(self.t2)
        self.t2.anchor(self.s, 0, 2)
        self.t2.rotate(90)
        self.add(self.t1a)
        self.t1a.anchor(self.t2, 0, 2)
        self.t1a.rotate(135)
        self.add(self.t4a)
        self.t4a.anchor(self.t2, 0, 0)
        self.t4a.rotate(180)
        self.t4a.translate(-1/4*scale, 0)
        self.add(self.t4b)
        self.t4b.anchor(self.t4a, 2, 0)
        self.add(self.p)
        self.p.flip()
        self.p.anchor(self.t4b, 1, 1)
        self.p.rotate(180)
        self.add(self.t1b)
        self.t1b.anchor(self.p, 2, 0)
        self.flip()
        self.rotate(180)


class TangramOx(Tangram):
    def __init__(self, scale=1, gap=0):
        super().__init__(scale, gap)
        self.add(self.t1a)
        self.add(self.s)
        self.s.anchor(self.t1a, 1, 3)
        self.add(self.t1b)
        self.t1b.anchor(self.s, 2, 2)
        self.t1b.rotate(90)
        self.add(self.t4a)
        self.t4a.anchor(self.t1b, 2, 1)
        self.t4a.rotate(135)
        self.add(self.t2)
        self.t2.anchor(self.t4a, 0, 0)
        self.t2.rotate(-135)
        self.add(self.t4b)
        self.t4b.anchor(self.t4a, 2, 2)
        self.t4b.rotate(180)
        self.t4b.translate(scale, 0)
        self.add(self.p)
        self.p.flip()
        self.p.anchor(self.t4b, 0, 1)
        self.p.rotate(90)
        self.flip()
        self.rotate(180)


class TangramTiger(Tangram):
    def __init__(self, scale=1, gap=0):
        super().__init__(scale, gap)
        self.add(self.t1a)
        self.t1a.rotate(135)
        self.add(self.t1b)
        self.t1b.anchor(self.t1a, 0, 0)
        self.t1b.rotate(-45)
        self.add(self.s)
        self.s.anchor(self.t1b, 0, 0)
        self.s.rotate(-135)
        self.add(self.t2)
        self.t2.anchor(self.s, 2, 1)
        self.t2.rotate(45)
        self.add(self.t4a)
        self.t4a.anchor(self.t2, 0, 1)
        self.t4a.rotate(-135)
        self.add(self.t4b)
        self.t4b.anchor(self.t2, 2, 0)
        self.t4b.rotate(-135)
        self.add(self.p)
        self.p.flip()
        self.p.anchor(self.t4b, 1, 1)
        self.p.rotate(-135)


class TangramRabbit(Tangram):
    def __init__(self, scale=1, gap=0):
        super().__init__(scale, gap)
        self.add(self.s)
        self.add(self.t2)
        self.t2.anchor(self.s, 3, 2)
        self.t2.rotate(195)
        self.t2.translate(self.ROOT2/8*scale, 0)
        self.add(self.p)
        self.p.flip()
        self.p.anchor(self.t2, 2, 1)
        self.p.rotate(210)
        self.add(self.t4a)
        self.t4a.rotate(-90)
        self.t4a.translate(self.ROOT2/8*scale, 0)
        self.add(self.t1a)
        self.t1a.anchor(self.t4a, 0, 1)
        self.t1a.rotate(90)
        self.add(self.t4b)
        self.t4b.anchor(self.s, 1, 1)
        self.t4b.rotate(-135)
        self.add(self.t1b)
        self.t1b.anchor(self.t4b, 0, 1)
        self.t1b.rotate(-180)


class TangramDragon(Tangram):
    def __init__(self, scale=1, gap=0):
        super().__init__(scale, gap)
        self.add(self.t2)
        self.t2.rotate(90)
        self.add(self.t1a)
        self.add(self.t1b)
        self.t1b.anchor(self.t1a, 0, 1)
        self.t1b.rotate(180)
        self.add(self.s)
        self.s.anchor(self.t1b, 2, 0)
        self.add(self.t4a)
        self.t4a.anchor(self.s, 0, 2)
        self.t4a.rotate(45)
        self.add(self.t4b)
        self.t4b.anchor(self.s, 1, 1)
        self.t4b.rotate(-90)
        self.add(self.p)
        self.p.flip()
        self.p.anchor(self.s, 1, 3)


class TangramSnake(Tangram):
    def __init__(self, scale=1, gap=0):
        super().__init__(scale, gap)
        self.add(self.p)
        self.p.flip()
        self.p.rotate(-45)
        self.add(self.t4a)
        self.t4a.rotate(-135)
        self.t4a.anchor(self.p, 0, 2)
        self.add(self.t4b)
        self.t4b.rotate(45)
        self.t4b.anchor(self.p, 3, 1)
        self.add(self.t2)
        self.t2.anchor(self.t4b, 2)
        self.add(self.s)
        self.s.anchor(self.t2, 2, 2)
        self.add(self.t1a)
        self.t1a.rotate(90)
        self.t1a.anchor(self.s)
        self.add(self.t1b)
        self.t1b.rotate(45)
        self.t1b.anchor(self.t1a, 1, 1)


class TangramHorse(Tangram):
    def __init__(self, scale=1, gap=0):
        super().__init__(scale, gap)
        self.add(self.t2)
        self.t2.rotate(-135)
        self.add(self.s)
        self.s.anchor(self.t2, 2, 2)
        self.add(self.t4a)
        self.t4a.rotate(180)
        self.t4a.anchor(self.s, 1, 0)
        self.add(self.t1a)
        self.t1a.rotate(-135)
        self.t1a.anchor(self.t4a, 1)
        self.add(self.t4b)
        self.t4b.rotate(135)
        self.t4b.anchor(self.t4a, 0, 1)
        self.add(self.t1b)
        self.t1b.rotate(90)
        self.t1b.anchor(self.t4a, 2, 1)
        self.t1b.translate(0, -0.15*scale)
        self.add(self.p)
        self.p.flip()
        self.p.anchor(self.t4b, 0, 3)
        self.p.rotate(-90)


class TangramGoat(Tangram):
    def __init__(self, scale=1, gap=0):
        super().__init__(scale, gap)
        self.add(self.p)
        self.p.flip()
        self.add(self.t2)
        self.t2.rotate(-90)
        self.t2.anchor(self.p, 3)
        self.add(self.s)
        self.s.rotate(45)
        self.s.anchor(self.t2, 2, 2)
        self.add(self.t4a)
        self.t4a.rotate(-135)
        self.t4a.anchor(self.s, 1, 0)
        self.add(self.t1a)
        self.t1a.rotate(-90)
        self.t1a.anchor(self.t4a, 1, 0)
        self.t1a.translate(scale*self.ROOT2/4, 0)
        self.add(self.t4b)
        self.t4b.rotate(180)
        self.t4b.anchor(self.t4a, 0, 1)
        self.t4b.translate(scale / 8, -scale / 8)
        self.add(self.t1b)
        self.t1b.rotate(135)
        self.t1b.anchor(self.t4b, 0, 1)
        self.t1b.translate(0, scale/4)


class TangramMonkey(Tangram):
    def __init__(self, scale=1, gap=0):
        super().__init__(scale, gap)
        self.add(self.s)
        self.add(self.t4a)
        self.t4a.rotate(-90)
        self.t4a.anchor(self.s, 1)
        self.t4a.translate(0, scale*self.ROOT2/16)
        self.add(self.t2)
        self.t2.rotate(180)
        self.t2.anchor(self.t4a, 2, 1)
        self.add(self.t4b)
        self.t4b.rotate(-135)
        self.t4b.anchor(self.t2, 0, 2)
        self.add(self.p)
        self.p.flip()
        self.p.rotate(-90)
        self.p.anchor(self.t4b, 0, 1)
        self.p.translate(scale * self.ROOT2 / 8, -scale * self.ROOT2 / 8)
        self.add(self.t1a)
        self.t1a.rotate(90)
        self.t1a.anchor(self.p, 2)
        self.add(self.t1b)
        self.t1b.rotate(135)
        self.t1b.anchor(self.t2, 0, 1)
        self.t1b.translate(0, -scale * self.ROOT2 / 8)


class TangramRooster(Tangram):
    def __init__(self, scale=1, gap=0):
        super().__init__(scale, gap)
        self.add(self.t1a)
        self.t1a.rotate(-135)
        self.add(self.s)
        self.s.anchor(self.t1a, 1, 2)
        self.s.translate(scale/4, 0)
        self.add(self.t4a)
        self.t4a.rotate(-90)
        self.t4a.anchor(self.s, 1, 2)
        self.add(self.t1b)
        self.t1b.rotate(-45)
        self.t1b.anchor(self.t4a, 1)
        self.t1b.translate(scale / 4, scale / 4)
        self.add(self.t4b)
        self.t4b.rotate(180)
        self.t4b.anchor(self.t4a)
        self.t4b.translate(0, scale * self.ROOT2 / 3)
        self.add(self.t2)
        self.t2.rotate(-135)
        self.t2.anchor(self.t4b, 0, 2)
        self.add(self.p)
        self.p.flip()
        self.p.rotate(90)
        self.p.anchor(self.t4b, 1, 1)


class TangramDog(Tangram):
    def __init__(self, scale=1, gap=0):
        super().__init__(scale, gap)
        self.add(self.t4a)
        self.t4a.rotate(-90)
        self.add(self.t4b)
        self.t4b.rotate(90)
        self.t4b.anchor(self.t4a, 2, 2)
        self.t4b.translate(-self.ROOT2 * scale / 4, -self.ROOT2 * scale / 4)
        self.add(self.t1a)
        self.t1a.rotate(-90)
        self.t1a.anchor(self.t4b, 0, 2)
        self.add(self.t2)
        self.t2.anchor(self.t4a, 0, 1)
        self.t2.rotate(20)
        self.add(self.s)
        a = 60
        self.s.rotate(a)
        self.s.anchor(self.t4b, 1, 0)
        self.add(self.p)
        self.p.flip()
        self.p.rotate(a-45)
        self.p.anchor(self.s, 2, 1)
        self.add(self.t1b)
        self.t1b.rotate(a+135)
        self.t1b.anchor(self.s, 2, 1)


class TangramPig(Tangram):
    def __init__(self, scale=1, gap=0):
        super().__init__(scale, gap)
        self.add(self.p)
        self.p.rotate(-45)
        self.add(self.t2)
        self.t2.rotate(180)
        self.t2.anchor(self.p, 3)
        self.add(self.t4a)
        self.t4a.rotate(-135)
        self.t4a.anchor(self.t2, 1)
        self.add(self.t4b)
        self.t4b.rotate(-90)
        self.t4b.anchor(self.t4a, 0, 2)
        self.add(self.s)
        self.s.anchor(self.t4b, 0, 1)
        self.s.translate(0, -scale / 2)
        self.add(self.t1a)
        self.t1a.rotate(90)
        self.t1a.anchor(self.s, 2)
        self.add(self.t1b)
        self.t1b.rotate(90)
        self.t1b.anchor(self.s, 0)
        self.flip()
        self.rotate(180)


def build_drawing(width=1000, height=1200, gap=0):
    drawing = svgwrite.Drawing(size=(width, height))

    scale = width * 0.08
    tangram_set = TangramCircle(TangramRat(scale, gap),
                                TangramOx(scale, gap),
                                TangramTiger(scale, gap),
                                TangramRabbit(scale, gap),
                                TangramDragon(scale, gap),
                                TangramSnake(scale, gap),
                                TangramHorse(scale, gap),
                                TangramGoat(scale, gap),
                                TangramMonkey(scale, gap),
                                TangramRooster(scale, gap),
                                TangramDog(scale, gap),
                                TangramPig(scale, gap))
    tangram_set.align(0, 0, width * 0.35)
    tangram_set.draw(drawing)

    return drawing


def write_files(drawing, svg_filepath):
    svg_text = drawing.tostring()
    with open(svg_filepath, 'w') as f:
        f.write(svg_text)
    png_filepath = svg_filepath.with_suffix('.png')
    rlg = svg2rlg(StringIO(svg_text))
    renderPM.drawToFile(rlg, png_filepath, fmt="PNG")


def demo():
    from test_tan import LiveSvg
    width = 700
    height = 800
    drawing = build_drawing(width, height, gap=0)
    svg1 = LiveSvg(drawing.tostring())
    svg1.display((-width/2, height/2))


def main():
    write_files(build_drawing(), Path('zodiac-front.svg'))
    write_files(build_drawing(gap=7), Path('zodiac-back.svg'))


if __name__ == '__main__':
    main()
elif __name__ == '__live_coding__':
    demo()
