from tkinter import Canvas, Frame, BOTH
from custom_enums import Terrain

class LandscapeGUI (Frame):

    def __init__ (self, parent):
        self.HEIGHT = 1000
        self.WIDTH = 1000
        self.parent = parent
        self.parent.title ("MAP")
        self.canvas = Canvas (height=self.HEIGHT, width=self.WIDTH, bg='white')
        self.canvas.pack (fill=BOTH)

    def paint_map (self, matrix):

        rows = len (matrix)
        cols = len (matrix[0])

        deltax = self.HEIGHT / (cols+2)
        deltay = self.WIDTH / (rows+2)

        for i in range (0, rows):
            for j in range (0, cols):
                if (matrix[i][j] == Terrain.FLAT):
                    _cell_color = 'white'
                elif (matrix[i][j] == Terrain.HILLY):
                    _cell_color = 'grey'
                elif (matrix[i][j] == Terrain.FOREST):
                    _cell_color = 'green'
                else:
                    _cell_color = 'brown'

                self._paint_cell (i, j, _cell_color, deltax, deltay)

    def _paint_cell (self, rw, cl, color, deltax, deltay):
        x0 = cl * deltax
        x1 = x0 + deltax
        y0 = rw * deltay
        y1 = y0 + deltay
        self.canvas.create_rectangle (
            x0, y0, x1, y1,
            fill=color, tags="cursor"
        )

    def updateLandscape(self, matrix):

        rows = len (matrix)
        cols = len (matrix[0])

        deltax = self.HEIGHT / (cols+2)
        deltay = self.WIDTH / (rows+2)

        for i in range (0, rows):
            for j in range (0, cols):
                x0 = i * deltax
                x1 = x0 + deltax
                y0 = j * deltay
                y1 = y0 + deltay
                self.canvas.create_text ((y0 + y1) // 2, (x0 + x1) // 2,  text= "(%.10f)" % (matrix[i][j]))