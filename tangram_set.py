class TangramSet:
    def __init__(self, *tangrams):
        self.tangrams = tangrams

    def draw(self, drawing):
        for tangram in self.tangrams:
            tangram.draw(drawing)

    def scale(self, scale):
        for tangram in self.tangrams:
            tangram.scale(scale)
