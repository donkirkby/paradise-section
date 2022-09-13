import svgwrite

from tangram import Tangram
from tangram_set import TangramSet


class TangramA(Tangram):
    def __init__(self, scale=1, gap=0):
        super().__init__(scale, gap)
        self.add(self.t4a)
        self.add(self.t1a)
        self.t1a.anchor(self.t4a)
        self.t1a.rotate(-90)
        self.add(self.t1b)
        self.t1b.anchor(self.t4a, 2, 1)
        self.t1b.rotate(180)
        self.add(self.t4b)
        self.t4b.anchor(self.t1b, 2, 1)
        self.t4b.rotate(180)
        self.add(self.s)
        self.s.anchor(self.t4b, 0, 1)
        self.add(self.p)
        self.p.anchor(self.s, 2, 1)
        self.add(self.t2)
        self.t2.anchor(self.p, 3)
        self.t2.rotate(-135)


class TangramD(Tangram):
    def __init__(self, scale=1, gap=0):
        super().__init__(scale, gap)
        self.add(self.t4a)
        self.t4a.rotate(-90)
        self.add(self.t4b)
        self.t4b.anchor(self.t4a, 1, 2)
        self.add(self.t1a)
        self.t1a.anchor(self.t4a, 2, 1)
        self.t1a.rotate(90)
        self.add(self.p)
        self.p.flip()
        self.p.anchor(self.t4a, 2, 1)
        self.p.rotate(90)
        self.add(self.t1b)
        self.t1b.anchor(self.t1a, 0, 2)
        self.add(self.s)
        self.s.anchor(self.t1b, 0, 3)
        self.add(self.t2)
        self.t2.anchor(self.s, 1, 1)
        self.t2.rotate(45)


class TangramG(Tangram):
    def __init__(self, scale=1, gap=0):
        super().__init__(scale, gap)
        self.add(self.t4a)
        self.add(self.t4b)
        self.t4b.anchor(self.t4a, 2)
        self.t4b.rotate(-45)
        self.add(self.t1a)
        self.t1a.anchor(self.t4b, 2, 1)
        self.t1a.rotate(135)
        self.add(self.t1b)
        self.t1b.anchor(self.t4b, 2, 1)
        self.t1b.rotate(180)
        self.add(self.t2)
        self.t2.anchor(self.t4a, 0, 2)
        self.t2.rotate(45)
        self.add(self.p)
        self.p.flip()
        self.p.anchor(self.t4a, 1)
        self.add(self.s)
        self.s.anchor(self.t4a, 1, 0)


class TangramM(Tangram):
    def __init__(self, scale=1, gap=0):
        super().__init__(scale, gap)
        self.add(self.t4a)
        self.add(self.t4b)
        self.t4b.anchor(self.t4a, 1, 2)
        self.t4b.rotate(90)
        self.add(self.s)
        self.s.anchor(self.t1a, 0, 3)
        self.add(self.t1a)
        self.t1a.anchor(self.s)
        self.t1a.rotate(-90)
        self.add(self.t2)
        self.t2.anchor(self.s, 2, 2)
        self.t2.rotate(45)
        self.add(self.t1b)
        self.t1b.anchor(self.t2, 1, 1)
        self.t1b.rotate(180)
        self.add(self.p)
        self.p.flip()
        self.p.anchor(self.t1b, 2)
        self.p.rotate(-90)


class TangramN(Tangram):
    def __init__(self, scale=1, gap=0):
        super().__init__(scale, gap)
        self.add(self.t4a)
        self.add(self.t1a)
        self.t1a.anchor(self.t4a)
        self.t1a.rotate(-90)
        self.add(self.s)
        self.s.anchor(self.t1a, 1, 3)
        self.add(self.p)
        self.p.flip()
        self.p.anchor(self.t1a, 2)
        self.add(self.t2)
        self.t2.anchor(self.t4a, 1, 2)
        self.t2.rotate(135)
        self.add(self.t1b)
        self.t1b.anchor(self.t2, 0, 2)
        self.t1b.rotate(180)
        self.add(self.t4b)
        self.t4b.anchor(self.t2, 0, 2)
        self.t4b.rotate(-45)


class TangramO(Tangram):
    def __init__(self, scale=1, gap=0):
        super().__init__(scale, gap)
        self.add(self.t4a)
        self.add(self.p)
        self.p.anchor(self.t4a, 2, 0)
        self.p.rotate(-45)
        self.add(self.s)
        self.s.anchor(self.p, 3, 3)
        self.s.rotate(45)
        self.add(self.t4b)
        self.t4b.anchor(self.s, 2, 1)
        self.t4b.rotate(180)
        self.add(self.t1a)
        self.t1a.anchor(self.t4b, 2, 0)
        self.t1a.rotate(135)
        self.add(self.t2)
        self.t2.anchor(self.t4b, 2, 1)
        self.t2.rotate(90)
        self.add(self.t1b)
        self.t1b.anchor(self.t4a, 1, 0)
        self.t1b.rotate(45)


class TangramR(Tangram):
    def __init__(self, scale=1, gap=0):
        super().__init__(scale, gap)
        self.add(self.t4a)
        self.t4a.rotate(-90)
        self.add(self.t2)
        self.t2.anchor(self.t4a, 2)
        self.t2.rotate(-135)
        self.add(self.s)
        self.s.anchor(self.t2, 2, 2)
        # self.s.rotate(45)
        self.add(self.t1a)
        self.t1a.anchor(self.t4a, 1, 2)
        self.t1a.rotate(90)
        self.add(self.t4b)
        self.t4b.anchor(self.t4a, 1)
        self.t4b.rotate(-90)
        self.add(self.p)
        self.p.flip()
        self.p.anchor(self.t4b, 2, 1)
        self.p.rotate(90)
        self.add(self.t1b)
        self.t1b.anchor(self.t4b, 1, 2)
        self.t1b.rotate(90)


class TangramT(Tangram):
    def __init__(self, scale=1, gap=0):
        super().__init__(scale, gap)
        self.add(self.t4a)
        self.t4a.rotate(-90)
        self.add(self.t4b)
        self.t4b.anchor(self.t4a, 2, 1)
        self.t4b.rotate(180)
        self.add(self.t2)
        self.t2.anchor(self.t4a, 2)
        self.t2.rotate(-135)
        self.add(self.t1a)
        self.t1a.anchor(self.t4b, 2, 1)
        self.t1a.rotate(45)
        self.add(self.s)
        self.s.anchor(self.t1a, 2, 1)
        self.t1a.anchor(self.s, 1, 2)
        self.t1a.rotate(-135)
        self.add(self.p)
        self.p.anchor(self.s, 1, 3)
        self.p.rotate(-90)
        self.add(self.t1b)
        self.t1b.anchor(self.p, 2, 1)
        self.t1b.rotate(90)


class TangramU(Tangram):
    def __init__(self, scale=1, gap=0):
        super().__init__(scale, gap)
        self.add(self.t4a)
        self.t4a.rotate(-45)
        self.add(self.t1a)
        self.t1a.anchor(self.t4a, 2, 2)
        self.t1a.rotate(-90)
        self.add(self.p)
        self.p.flip()
        self.p.anchor(self.t4a, 1, 2)
        self.p.rotate(90)
        self.add(self.s)
        self.s.anchor(self.t4a, 1, 3)
        self.add(self.t2)
        self.t2.anchor(self.s, 1, 2)
        self.t2.rotate(135)
        self.add(self.t4b)
        self.t4b.anchor(self.t2, 0, 1)
        self.t4b.rotate(-45)
        self.add(self.t1b)
        self.t1b.anchor(self.t4b, 2, 2)
        self.t1b.rotate(-90)


class TangramY(Tangram):
    def __init__(self, scale=1, gap=0):
        super().__init__(scale, gap)
        self.add(self.t2)
        self.add(self.t4a)
        self.t4a.anchor(self.t2, 2)
        self.t4a.rotate(-45)
        self.add(self.t4b)
        self.t4b.anchor(self.t2, 2, 1)
        self.t4b.rotate(-90)
        self.add(self.p)
        self.p.flip()
        self.p.anchor(self.t4b, 2, 2)
        self.add(self.t1a)
        self.t1a.anchor(self.t4b, 0)
        self.t1a.rotate(180)
        self.add(self.s)
        self.s.anchor(self.t4b, 0, 1)
        self.add(self.t1b)
        self.t1b.anchor(self.s, 3)
        self.t1b.rotate(180)


class TangramQuestion(Tangram):
    def __init__(self, scale=1, gap=0):
        super().__init__(scale, gap)
        self.add(self.t2)
        self.t2.rotate(-135)
        self.add(self.t4a)
        self.t4a.anchor(self.t2, 2)
        self.t4a.rotate(180)
        self.add(self.t1a)
        self.t1a.anchor(self.t4a, 1, 1)
        self.t1a.rotate(135)
        self.add(self.t4b)
        self.t4b.anchor(self.t2, 2, 1)
        self.t4b.rotate(135)
        self.add(self.p)
        self.p.anchor(self.t4a, 2, 1)
        self.p.rotate(90)
        self.add(self.t1b)
        self.t1b.anchor(self.p, 0, 1)
        self.t1b.rotate(135)
        self.add(self.s)
        self.s.anchor(self.t1b, 2, 2)
        self.t1b.rotate(-45)


class TangramSquare(Tangram):
    def __init__(self, scale=1, gap=0):
        super().__init__(scale, gap)
        self.add(self.t4a)
        self.t4a.rotate(135)
        self.add(self.t4b)
        self.t4b.rotate(45)
        self.add(self.p)
        self.p.anchor(self.t4a, 2, 1)
        self.p.rotate(-135)
        self.add(self.t1a)
        self.t1a.rotate(-135)
        self.add(self.t1b)
        self.t1b.anchor(self.t4b, 1, 2)
        self.t1b.rotate(-45)
        self.add(self.s)
        self.s.rotate(-45)
        self.add(self.t2)
        self.t2.anchor(self.s, 2, 1)
        self.t2.rotate(90)


class TangramTriangle(TangramSquare):
    def __init__(self, scale=1, gap=0):
        super().__init__(scale, gap)
        self.t4a.anchor(self.t1b, 2, 1)
        self.t4b.anchor(self.t4a)
        self.t4b.rotate(180)


class TangramSlash(TangramSquare):
    def __init__(self, scale=1, gap=0):
        super().__init__(scale, gap)
        self.t4a.anchor(self.t1b, 2, 1)
        self.t4b.anchor(self.t4a)


class TangramCorner(TangramSquare):
    def __init__(self, scale=1, gap=0):
        super().__init__(scale, gap)
        self.t4a.anchor(self.t1b, 2, 1)
        self.t4b.anchor(self.t4a, 1)
        self.t4b.rotate(-90)


class TangramUFO(Tangram):
    def __init__(self, scale=1, gap=0):
        super().__init__(scale, gap)
        self.add(self.t4a)
        self.t4a.rotate(-45)
        self.add(self.t4b)
        self.t4b.anchor(self.t4a, 1, 2)
        self.t4b.rotate(135)
        self.add(self.p)
        self.p.flip()
        self.p.anchor(self.t4a, 1, 1)
        self.p.rotate(-45)
        self.add(self.t2)
        self.t2.anchor(self.p, 0, 1)
        self.add(self.t1a)
        self.t1a.anchor(self.t2, 0, 1)
        self.t1a.rotate(-45)
        self.add(self.s)
        self.s.anchor(self.t4a, 0, 1)
        self.s.rotate(-45)
        self.add(self.t1b)
        self.t1b.anchor(self.s, 2)
        self.t1b.rotate(45)


class TangramKnife(Tangram):
    def __init__(self, scale=1, gap=0):
        super().__init__(scale, gap)
        self.add(self.t4a)
        self.t4a.rotate(-135)
        self.add(self.t2)
        self.t2.anchor(self.t4a, 0, 1)
        self.t2.rotate(180)
        self.add(self.t1a)
        self.t1a.anchor(self.t2, 2, 2)
        self.t1a.rotate(135)
        self.add(self.s)
        self.s.anchor(self.t2)
        self.s.rotate(-45)
        self.add(self.p)
        self.p.anchor(self.t4a, 0, 1)
        self.p.rotate(-135)
        self.add(self.t1b)
        self.t1b.anchor(self.s, 2)
        self.t1b.rotate(45)
        self.add(self.t4b)
        self.t4b.anchor(self.t1b, 1, 2)
        self.t4b.rotate(-135)


class TangramSnail(Tangram):
    def __init__(self, scale=1, gap=0):
        super().__init__(scale, gap)
        self.add(self.t4a)
        self.add(self.t4b)
        self.t4b.anchor(self.t4a, 2, 1)
        self.t4b.rotate(90)
        self.add(self.t1a)
        self.t1a.anchor(self.t4b, 2, 1)
        self.t1a.rotate(180)
        self.add(self.s)
        self.s.anchor(self.t1a, 0, 3)
        self.add(self.t1b)
        self.t1b.anchor(self.s, 2)
        self.t1b.rotate(-90)
        self.add(self.p)
        self.p.flip()
        self.p.anchor(self.t4a, 1, 1)
        self.add(self.t2)
        self.t2.anchor(self.t4b, 2)
        self.t2.rotate(-135)


class TangramBoxCutter(Tangram):
    def __init__(self, scale=1, gap=0):
        super().__init__(scale, gap)
        self.add(self.t4a)
        self.t4a.rotate(90)
        self.add(self.s)
        self.s.anchor(self.t4a)
        self.add(self.t4b)
        self.t4b.anchor(self.s, 3, 2)
        self.t4b.rotate(90)
        self.add(self.t1a)
        self.t1a.anchor(self.s, 3, 1)
        self.t1a.rotate(-90)
        self.add(self.p)
        self.p.flip()
        self.p.anchor(self.t1a, 0, 3)
        self.add(self.t1b)
        self.t1b.anchor(self.t4b, 0, 2)
        self.t1b.rotate(-90)
        self.add(self.t2)
        self.t2.anchor(self.t4b, 1, 1)
        self.t2.rotate(135)


class TangramEraser(Tangram):
    def __init__(self, scale=1, gap=0):
        super().__init__(scale, gap)
        self.add(self.t4a)
        self.t4a.rotate(90)
        self.add(self.t4b)
        self.t4b.anchor(self.t4a, 0, 1)
        self.t4b.rotate(-90)
        self.add(self.s)
        self.s.anchor(self.t4a, 2, 3)
        self.add(self.t1a)
        self.t1a.anchor(self.s, 1)
        self.add(self.t2)
        self.t2.anchor(self.t1a, 1)
        self.t2.rotate(45)
        self.add(self.t1b)
        self.t1b.anchor(self.t4b, 1, 2)
        self.t1b.rotate(90)
        self.add(self.p)
        self.p.anchor(self.t1b, 0, 3)
        self.p.rotate(90)


class TangramBarge(Tangram):
    def __init__(self, scale=1, gap=0):
        super().__init__(scale, gap)
        self.add(self.t4a)
        self.t4a.rotate(-45)
        self.add(self.t4b)
        self.t4b.anchor(self.t4a, 2, 1)
        self.t4b.rotate(135)
        self.add(self.t2)
        self.t2.anchor(self.t4a, 1, 1)
        self.add(self.s)
        self.s.anchor(self.t4a, 2, 3)
        self.s.rotate(45)
        self.add(self.t1a)
        self.t1a.anchor(self.s, 0)
        self.t1a.rotate(-45)
        self.add(self.t1b)
        self.t1b.anchor(self.s, 1)
        self.t1b.rotate(45)
        self.add(self.p)
        self.p.flip()
        self.p.anchor(self.t1a, 1, 3)
        self.p.rotate(45)


class TangramBarn(Tangram):
    def __init__(self, scale=1, gap=0):
        super().__init__(scale, gap)
        self.add(self.t4a)
        self.add(self.t4b)
        self.t4b.anchor(self.t4a, 2, 1)
        self.t4b.rotate(180)
        self.add(self.t2)
        self.t2.anchor(self.t4a, 1, 2)
        self.t2.rotate(135)
        self.add(self.t1a)
        self.t1a.anchor(self.t4a, 1, 2)
        self.t1a.rotate(90)
        self.add(self.p)
        self.p.flip()
        self.p.anchor(self.t1a, 1, 3)
        self.p.rotate(90)
        self.add(self.s)
        self.s.anchor(self.t4b, 0, 1)
        self.add(self.t1b)
        self.t1b.anchor(self.s)
        self.t1b.rotate(90)


class TangramTent(Tangram):
    def __init__(self, scale=1, gap=0):
        super().__init__(scale, gap)
        self.add(self.t4a)
        self.add(self.t4b)
        self.t4b.anchor(self.t4a, 2, 1)
        self.t4b.rotate(180)
        self.add(self.s)
        self.s.anchor(self.t4a, 0, 1)
        self.add(self.t1a)
        self.t1a.anchor(self.s, 2)
        self.t1a.rotate(90)
        self.add(self.t2)
        self.t2.anchor(self.t4b, 0, 2)
        self.t2.rotate(-135)
        self.add(self.p)
        self.p.flip()
        self.p.anchor(self.t4b, 0, 3)
        self.p.rotate(-90)
        self.add(self.t1b)
        self.t1b.anchor(self.t4b, 2)


class TangramRectangle(Tangram):
    def __init__(self, scale=1, gap=0):
        super().__init__(scale, gap)
        self.add(self.t4a)
        self.add(self.t4b)
        self.t4b.anchor(self.t4a, 1, 2)
        self.t4b.rotate(180)
        self.add(self.s)
        self.s.anchor(self.t4a, 0, 3)
        self.add(self.t1a)
        self.t1a.anchor(self.s, 0, 0)
        self.t1a.rotate(-90)
        self.add(self.t2)
        self.t2.anchor(self.t1a, 1, 1)
        self.t2.rotate(-135)
        self.add(self.p)
        self.p.flip()
        self.p.anchor(self.s, 2, 1)
        self.p.rotate(90)
        self.add(self.t1b)
        self.t1b.anchor(self.s, 2, 1)
        self.t1b.rotate(180)


def build_drawing(width=1300, height=1500, gap=0):
    drawing = svgwrite.Drawing(size=(width, height))

    y = height/2
    scale = width/10
    line_spacing = width/20
    tangram_set = TangramSet(TangramD(scale, gap),
                             TangramO(scale, gap),
                             Tangram(scale, gap),
                             TangramY(scale, gap),
                             TangramO(scale, gap),
                             TangramU(scale, gap))
    right = width/2
    left = -right
    y = tangram_set.align(y, left, right)
    tangram_set.draw(drawing)

    tangram_set = TangramSet(TangramT(scale, gap),
                             TangramA(scale, gap),
                             TangramN(scale, gap),
                             TangramG(scale, gap),
                             TangramR(scale, gap),
                             TangramA(scale, gap),
                             TangramM(scale, gap))
    y = tangram_set.align(y - line_spacing, left, right)
    tangram_set.draw(drawing)

    tangram_set = TangramSet(TangramQuestion(scale, gap))
    y = tangram_set.align(y - line_spacing, left, right)
    tangram_set.draw(drawing)

    tangram_set = TangramSet(TangramSquare(scale, gap),
                             TangramTriangle(scale, gap),
                             TangramTent(scale, gap),
                             TangramBarn(scale, gap),
                             TangramUFO(scale, gap),
                             TangramCorner(scale, gap),
                             TangramRectangle(scale, gap))
    y = tangram_set.align(y - line_spacing/2, left, right)
    tangram_set.draw(drawing)

    tangram_set = TangramSet(TangramSlash(scale, gap),
                             TangramBoxCutter(scale, gap),
                             TangramEraser(scale, gap),
                             TangramSnail(scale, gap),
                             TangramKnife(scale, gap),
                             TangramBarge(scale, gap))
    y = tangram_set.align(y - line_spacing, left, right)
    tangram_set.draw(drawing)

    scale /= 5
    gap /= 1.5
    tangram_set = TangramSet(TangramA(scale, gap),
                             TangramT(scale, gap),
                             TangramT(scale, gap),
                             TangramR(scale, gap),
                             TangramR(scale, gap),
                             TangramRectangle(scale, gap),
                             TangramBarge(scale, gap),
                             TangramBarge(scale, gap),
                             TangramD(scale, gap),
                             TangramO(scale, gap),
                             TangramN(scale, gap),
                             TangramR(scale, gap),
                             TangramRectangle(scale, gap),
                             TangramR(scale, gap),
                             TangramR(scale, gap),
                             TangramD(scale, gap),
                             TangramY(scale, gap),
                             TangramSquare(scale, gap),
                             TangramG(scale, gap),
                             TangramRectangle(scale, gap),
                             TangramT(scale, gap),
                             TangramA(scale, gap),
                             TangramU(scale, gap),
                             TangramD(scale, gap),
                             TangramSquare(scale, gap),
                             TangramRectangle(scale, gap),
                             TangramO(scale, gap))
    tangram_set.align(y - line_spacing, left, right)
    # tangram_set.draw(drawing)

    return drawing


def demo():
    from test_tan import LiveSvg
    width = 700
    height = 800
    drawing = build_drawing(width, height, gap=0)
    svg1 = LiveSvg(drawing.tostring())
    svg1.display((-width/2, height/2))


def main():
    front_drawing = build_drawing()
    with open('front.svg', 'w') as f:
        f.write(front_drawing.tostring())
    back_drawing = build_drawing(gap=4)
    with open('back.svg', 'w') as f:
        f.write(back_drawing.tostring())


if __name__ == '__main__':
    main()
elif __name__ == '__live_coding__':
    demo()
