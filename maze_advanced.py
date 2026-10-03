import logging
import random
from pathlib import Path

from svgwrite import Drawing

from maze import Maze
from tangram import Tangram
from test_tan import LiveSvg

logger = logging.getLogger(__name__)


def add_tangrams(maze: Maze):
    gap = 0
    tangram = Tangram(50, gap)
    maze.add_tangram(tangram, 'T')
    tangram.add(tangram.t4a)
    tangram.t4a.rotate(135)
    tangram.add(tangram.t1a)
    tangram.t1a.rotate(90)
    tangram.t1a.anchor(tangram.t4a, 2, 2)
    tangram.add(tangram.t4b)
    tangram.t4b.anchor(tangram.t1a, 1, 2)
    tangram.add(tangram.s)
    tangram.s.anchor(tangram.t4b, 0, 1)
    tangram.add(tangram.t2)
    tangram.t2.rotate(90)
    tangram.t2.anchor(tangram.s)
    tangram.add(tangram.t1b)
    tangram.t1b.rotate(45)
    tangram.t1b.anchor(tangram.s, 0, 1)
    tangram.t1b.translate(tangram.width * 0.15, 0)
    tangram.add(tangram.p)
    tangram.p.rotate(45)
    tangram.p.anchor(tangram.t1b, 1, 2)
    tangram.flip()
    tangram.rotate(180)

    tangram = Tangram(50, gap)
    maze.add_tangram(tangram, 'R')
    tangram.add(tangram.t4a)
    tangram.t4a.rotate(-135)
    tangram.add(tangram.t1a)
    tangram.t1a.rotate(-135)
    tangram.t1a.anchor(tangram.t4a, 0, 2)
    tangram.add(tangram.t4b)
    tangram.t4b.rotate(45)
    tangram.t4b.anchor(tangram.t4a, 1)
    tangram.add(tangram.t2)
    tangram.t2.anchor(tangram.t4b, 0, 1)
    tangram.add(tangram.s)
    tangram.s.rotate(45)
    tangram.s.anchor(tangram.t2, 2)
    tangram.add(tangram.p)
    tangram.p.rotate(45)
    tangram.p.flip()
    tangram.p.anchor(tangram.s, 2, 3)
    tangram.add(tangram.t1b)
    tangram.t1b.rotate(180)
    tangram.t1b.anchor(tangram.p, 0, 1)

    tangram = Tangram(50, gap)
    maze.add_tangram(tangram, 'I')
    tangram.add(tangram.p)
    tangram.add(tangram.t2)
    tangram.t2.rotate(45)
    tangram.t2.anchor(tangram.p, 1)
    h = tangram.height
    tangram.add(tangram.t4a)
    tangram.t4a.rotate(45)
    tangram.t4a.translate(h/2, -tangram.height)
    tangram.add(tangram.t1a)
    tangram.t1a.rotate(135)
    tangram.t1a.anchor(tangram.t4a)
    tangram.add(tangram.t1b)
    tangram.t1b.rotate(-90)
    tangram.t1b.anchor(tangram.t1a, 2, 2)
    tangram.add(tangram.t4b)
    tangram.t4b.rotate(90)
    tangram.t4b.anchor(tangram.t1b, 1, 2)
    tangram.add(tangram.s)
    tangram.s.anchor(tangram.t4b)

    tangram = Tangram(50, gap)
    maze.add_tangram(tangram, 'A')
    tangram.add(tangram.p)
    tangram.p.rotate(45)
    tangram.p.flip()
    tangram.add(tangram.t2)
    tangram.t2.rotate(-90)
    tangram.t2.anchor(tangram.p, 2)
    tangram.add(tangram.t4a)
    tangram.t4a.rotate(-135)
    tangram.t4a.anchor(tangram.p, 1)
    tangram.add(tangram.t4b)
    tangram.t4b.rotate(180)
    tangram.t4b.anchor(tangram.t4a, 2, 2)
    tangram.add(tangram.s)
    tangram.s.rotate(45)
    tangram.s.anchor(tangram.t4a, 1, 2)
    tangram.add(tangram.t1a)
    tangram.t1a.rotate(-45)
    tangram.t1a.anchor(tangram.t4a, 2, 2)
    l = 0.4*tangram.s.width
    tangram.s.translate(l, 0)
    tangram.t1a.translate(-l, 0)
    tangram.add(tangram.t1b)
    tangram.t1b.rotate(135)
    tangram.t1b.anchor(tangram.t1a, 1, 2)
    tangram.flip()
    tangram.rotate(180)

    tangram = Tangram(50, gap)
    maze.add_tangram(tangram, 'N')
    tangram.add(tangram.t4a)
    tangram.add(tangram.t4b)
    tangram.t4b.rotate(90)
    tangram.add(tangram.t2)
    tangram.t2.rotate(-90)
    tangram.t2.anchor(tangram.t4b, 2, 1)
    tangram.add(tangram.s)
    tangram.s.rotate(45)
    tangram.s.anchor(tangram.t2)
    tangram.add(tangram.p)
    tangram.p.rotate(45)
    tangram.p.flip()
    tangram.p.anchor(tangram.s, 1, 2)
    tangram.add(tangram.t1a)
    tangram.t1a.rotate(180)
    tangram.t1a.anchor(tangram.p, 0, 1)
    tangram.add(tangram.t1b)
    tangram.t1b.anchor(tangram.t4a, 2)
    l = 0.32*tangram.t4a.height
    tangram.t1b.translate(l, -l)

    tangram = Tangram(50, gap)
    maze.add_tangram(tangram, 'G')
    tangram.add(tangram.t2)
    tangram.t2.rotate(-90)
    tangram.add(tangram.t4a)
    tangram.t4a.rotate(90)
    tangram.t4a.anchor(tangram.t2, 1)
    tangram.add(tangram.t4b)
    tangram.t4b.rotate(45)
    tangram.t4b.anchor(tangram.t4a, 2)
    tangram.add(tangram.t1a)
    l = 0.8 * tangram.t1a.width / tangram.ROOT2
    tangram.t1a.rotate(135)
    tangram.t1a.anchor(tangram.t4a, 1)
    tangram.t1a.translate(l, l)
    tangram.add(tangram.t1b)
    tangram.t1b.rotate(-45)
    tangram.t1b.anchor(tangram.t1a, 2, 1)
    tangram.add(tangram.p)
    tangram.p.flip()
    tangram.p.anchor(tangram.t4b, 2, 3)
    l = tangram.p.width * 0.15
    tangram.p.translate(l, 0)
    tangram.add(tangram.s)
    tangram.s.anchor(tangram.p)
    tangram.s.translate(-l, 0)

    tangram = Tangram(50, gap)
    maze.add_tangram(tangram, 'L')
    tangram.add(tangram.t4a)
    tangram.t4a.rotate(-135)
    width1 = tangram.width
    tangram.add(tangram.t2)
    tangram.t2.rotate(45)
    tangram.t2.anchor(tangram.t4a, 1, 2)
    tangram.add(tangram.p)
    tangram.p.flip()
    tangram.p.anchor(tangram.t2, 1)
    width2 = tangram.width
    tangram.t2.translate((width1-width2)/2, 0)
    tangram.p.anchor(tangram.t2, 1)
    tangram.add(tangram.t4b)
    tangram.t4b.rotate(-90)
    tangram.t4b.anchor(tangram.t2)
    tangram.add(tangram.s)
    tangram.s.anchor(tangram.t4b, 0, 2)
    tangram.add(tangram.t1a)
    tangram.t1a.rotate(90)
    tangram.t1a.anchor(tangram.t4b, 1, 2)
    tangram.add(tangram.t1b)
    tangram.t1b.rotate(90)
    tangram.t1b.anchor(tangram.t4b, 2, 1)
    tangram.flip()

    tangram = Tangram(50, gap)
    maze.add_tangram(tangram, 'E')
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
    tangram.rotate(180)

    tangram = Tangram(50, gap)
    maze.add_tangram(tangram, 'S')
    tangram.add(tangram.p)
    tangram.p.rotate(45)
    tangram.p.flip()
    tangram.add(tangram.t1a)
    tangram.t1a.rotate(135)
    tangram.t1a.anchor(tangram.p, 2)
    tangram.add(tangram.s)
    tangram.s.rotate(45)
    tangram.s.anchor(tangram.t1a, 0, 2)
    tangram.add(tangram.t1b)
    tangram.t1b.rotate(45)
    tangram.t1b.anchor(tangram.s, 1)
    tangram.add(tangram.t4a)
    tangram.t4a.rotate(-45)
    tangram.t4a.anchor(tangram.s)
    tangram.add(tangram.t2)
    tangram.t2.rotate(135)
    tangram.t2.anchor(tangram.s, 3, 1)
    tangram.add(tangram.t4b)
    tangram.t4b.rotate(-135)
    tangram.t4b.anchor(tangram.t2)


def main() -> None:
    random.seed(0)
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(levelname)s %(message)s')
    logger.info('Starting.')
    spacing = 20
    grid_size = 4*spacing - 11
    maze = Maze(width=grid_size, height=grid_size)
    maze.scale = 15
    maze.offset_x = 10
    maze.offset_y = 10
    group_names = ('TRI', 'ANG', 'LES')
    for y, line in enumerate(group_names):
        for x, group_name in enumerate(line):
            maze.add_chamber(spacing*(x+1)-6, spacing*(y+1)-6, group_name)
    text_legs = {
        # start - G
        (2, 0): 'lddddrururulurrdrrdrdldrruuurdrrdrrruuurrdrddrrdrurdrrulurrrd'
                'ldrrurruuurddrrdrdldrrrrulururdrrruuurdrurdrdldlldldrddrurdru'
                'rddlldrddrdrrdllddrdlllullddrrrdrdldddrdrrurrrdrdrurdrrrrddrdddd',
        # G - N
        (50, 30): 'uurullldrddldllddldlllll',
        # N - A
        (30, 30): 'uldlddluuulldldddrdlldldrrdlldllldlu',
        # A - R
        (18, 30): 'urruurururrrurdddrrrrulurrrddrruruuluuurul',
        # R - L
        (30, 18): 'llulddldrrddldllldluuluuldlddddllllluullldddlluldlddddddlld'
                  'drdldldrdddddrddddruurddrdldldddddd',
        # L - I
        (14, 48): 'rruuuuuulururrdrrdrrurdddrrdldrddlldrdrruuuruurrrurrdrdrrrr'
                  'uuurddruurruuuuurrdrrurdrddddddrurdrrrurrruururrruuruururul'
                  'uruuuullluuruluulurrulllllulllluluulur',
        # I - E
        (54, 20): 'lldrrrrdrrruruurrrdrrrrdldlldrddddlddldddrddldddrrddrdldldl'
                  'lldrrdldluldldllllldlulldlullddrdllllluuulllddlldld',
        # E - S
        (40, 54): 'drururrdrrruuruurr',
        # S - T
        (60, 54): 'urdrrddrdrddddllllluullddddllulldluldlllllluulddlldlllululd'
                  'luldllulllllldllurulldlulullulllddrurddllddllllulddluuluruu'
                  'ldldlllluururuuululuuruuuuluuluuluuruuuluruluuuuuruurrulull'
                  'uruluruururrrrruurdrruu',
        # T - end
        (10, 18): 'llulddldrrddlllldddlldrddlulddrddrrdldddddlddrdlldrdrddddrd'
                  'dddrrdllllulddrrdldrddllldrdddddddlddddruurrrrurulurrrrrddd'
                  'rrrrurrdrdrdrurruurddrrrrdrurulurrdddrrurruurdrururdrrrdrrd'
                  'rdruurrdrrrruuurdrrrdrrrddrrrrrururdrrd',

        # red herrings
        # G - R
        (54, 28): 'urdrruluulllddluulldluldllululululllululuu',
        # A - L
        (10, 50): 'lururururruluuurullurr',
        # L - E
        (18, 58): 'rruuururrurddrurruruuurr',
        # T - R
        (18, 18): 'druruuurdrdrurruruluururrulurrrd',

        # doorways
        # T E
        (20, 14): 'rrdrruulururuluurdru',
        # T NE
        (18, 10): 'ruurrrdruurrrrururr',
        # T N
        (14, 8): 'rrurdrurrrruurrrr',
        # T NW
        (10, 10): 'lldlluulururddruuuullullldr',
        # T W
        (8, 14): 'uullluuldlldrddddlddldldr',
        # R E
        (40, 14): 'ddddddrdrurd',
        # R NE
        (38, 10): 'rrdddrurrddrd',
        # R N
        (34, 8): 'rrrrdrrrdrdr',
        # R W
        (28, 14): 'ldrdllddldllluldldldlu',
        # I E
        (60, 14): 'rrullururrurdruulluuulluurruluuurrrdrdrruu',
        # I NE
        (58, 10): 'uululurruruullurruul',
        # I N
        (54, 8): 'uurullululluuulllll',
        # I NW
        (50, 10): 'uuullullurulldlllurrur',
        # I W
        (48, 14): 'lddrdddldrrdlllul',
        # I SE
        (58, 18): 'drurruurrdrrrrddrdddlddldddddrrddldlldrdrddrdlldrdrddddldrd'
                  'ddldlllullddrrrdrrrdddlldrrdldrddlddrdddldldrrdddll',
        # A E
        (20, 34): 'rruuuuuuurrurddrrrrrr',
        # A N
        (14, 28): 'rrrrruur',
        # A NW
        (10, 30): 'luuurrrrrrrrrull',
        # A W
        (8, 34): 'ddddldddrdrurrdd',
        # A SW
        (10, 38): 'dldr',
        # N NE
        (38, 30): 'uuluruuluruurdrdr',
        # N N
        (34, 28): 'ruruuuurul',
        # N W
        (28, 34): 'uldlddrdddllu',
        # N SW
        (30, 38): 'dllddrdldrdllullluu',
        # N S
        (34, 40): 'ldlddrdru',
        # N SE
        (38, 38): 'rruurdrrrrr',
        # G E
        (60, 34): 'uuru',
        # G W
        (48, 34): 'ldrddlullullld',
        # G SW
        (50, 38): 'dllddddrrd',
        # G S
        (54, 40): 'dlddr',
        # G SE
        (58, 38): 'ddllld',
        # L E
        (20, 54): 'uuurdrurrdrur',
        # L NE
        (18, 50): 'urulluuuurdrurrdldddru',
        # L SW
        (10, 58): 'dlddll',
        # L S
        (14, 60): 'lddrurdrr',
        # E N
        (34, 48): 'rrullldlullldl',
        # E W
        (28, 54): 'ddluldllluld',
        # E SW
        (30, 58): 'dlldllllulul',
        # E S
        (34, 60): 'rdrrururrrrurdrrrrddrdru',
        # E SE
        (38, 58): 'rruurrrdrrdr',
        # S NE
        (58, 50): 'urdrdrrdrrrddldrrddddddrdlldllddrrdrrdd',
        # S N
        (54, 48): 'rrurdrrrruu',
        # S W
        (48, 54): 'dllldrdrurd',
        # S SW
        (50, 58): 'ldldrrrddl',
        # S S
        (54, 60): 'drurrdd',
        # S SE
        (58, 58): 'rrrrdrru',
    }
    for start, leg_text in text_legs.items():
        maze.add_path(start, leg_text)

    # try:
    #     logger.info(maze.link_random_walks([(58, 58), (64, 58)]))
    # except IndexError:
    #     logger.error('Dead end in random walk.')

    # maze.fill()
    add_tangrams(maze)
    image_path = Path(__file__).with_name(
        f'maze-advanced.svg')
    width = 1180
    height = 1180
    drawing = Drawing(size=(width, height))
    maze.draw(drawing)
    # maze.draw_header(drawing)
    if __name__ == '__live_coding__':
        LiveSvg(drawing.tostring()).display((-width*0.375, height*0.375))
    else:
        image_path.write_text(drawing.tostring())


if __name__ in ('__main__', '__live_coding__'):
    main()
