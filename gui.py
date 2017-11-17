from tkinter import Tk
from tkinter import Canvas, Frame, BOTH, Text
from custom_enums import Terrain

class LandscapeGUI (Frame):

    def __init__ (self, parent):
        self.HEIGHT = 1000
        self.WIDTH = 1000
        self.parent = parent
        self.parent.title ("MAZE")
        self.canvas = Canvas (height=self.HEIGHT, width=self.WIDTH, bg='white')
        self.canvas.pack (fill=BOTH, expand=True)

    def paint_map (self, matrix):
        deltax = self.HEIGHT/len(matrix)
        deltay = self.WIDTH/len(matrix[0])
        rows = len (matrix)
        cols = len (matrix[0])
        for i in range (0, rows):
            for j in range (0, cols):
                if (matrix[i][j] == Terrain.FLAT):
                    _cell_color = 'white'
                elif (matrix[i][j] == Terrain.HILLY):
                    _cell_color = 'grey'
                elif (matrix[i][j] == Terrain.FOREST):
                    _cell_color = 'pink'
                else:
                    _cell_color = 'green'

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

    def updateData(self, matrix):
        deltax = self.HEIGHT/len(matrix)
        deltay = self.WIDTH/len(matrix[0])
        rows = len (matrix)
        cols = len (matrix[0])

        for i in range (0, rows):
            for j in range (0, cols):
                x0 = i * deltax
                x1 = x0 + deltax
                y0 = j * deltay
                y1 = y0 + deltay
                self.canvas.create_text ((x0 + x1) // 2, (y0 + y1) // 2, text= "(%f)" % (matrix[i][j]))