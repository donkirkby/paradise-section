import svgwrite

from tangram import Tangram


def build_drawing():
    drawing = svgwrite.Drawing(size=(500, 400))

    gap = 4
    square = build_square(gap)
    square.translate(150, -100)
    square.draw(drawing)
    d = build_d(gap)
    d.translate(-200, 100)
    d.draw(drawing)

    return drawing


def build_square(gap=0):
    tangram = Tangram(scale=200, gap=gap)
    tangram.add(tangram.t4a)
    tangram.t4a.rotate(45)
    tangram.add(tangram.t4b)
    tangram.t4b.rotate(-45)
    tangram.add(tangram.p)
    tangram.p.flip()
    tangram.p.rotate(-45)
    tangram.p.anchor(tangram.t4b, 1, 1)
    tangram.add(tangram.t1a)
    tangram.t1a.rotate(-135)
    tangram.add(tangram.t1b)
    tangram.t1b.anchor(tangram.t4a, 2, 1)
    tangram.t1b.rotate(135)
    tangram.add(tangram.s)
    tangram.s.rotate(135)
    tangram.add(tangram.t2)
    tangram.t2.anchor(tangram.s, 2, 2)
    return tangram


def build_d(gap=0):
    tangram = Tangram(scale=200, gap=gap)
    tangram.add(tangram.t4a)
    tangram.t4a.rotate(-90)
    tangram.add(tangram.t4b)
    tangram.t4b.anchor(tangram.t4a, 1, 2)
    tangram.add(tangram.t1a)
    tangram.t1a.anchor(tangram.t4a, 2, 1)
    tangram.t1a.rotate(90)
    tangram.add(tangram.p)
    tangram.p.flip()
    tangram.p.anchor(tangram.t4a, 2, 1)
    tangram.p.rotate(90)
    tangram.add(tangram.t1b)
    tangram.t1b.anchor(tangram.t1a, 0, 2)
    tangram.add(tangram.s)
    tangram.s.anchor(tangram.t1b, 0, 3)
    tangram.add(tangram.t2)
    tangram.t2.anchor(tangram.s, 1, 1)
    tangram.t2.rotate(45)
    return tangram


def demo():
    from test_tan import LiveSvg
    drawing = build_drawing()
    svg1 = LiveSvg(drawing.tostring())
    svg1.display((-200, 200))


def main():
    drawing = build_drawing()
    with open('front.svg', 'w') as f:
        f.write(drawing.tostring())


if __name__ == '__main__':
    main()
elif __name__ == '__live_coding__':
    demo()
