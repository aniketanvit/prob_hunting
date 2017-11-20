import tkinter as tk
from custom_enums import Terrain
from tkinter import Canvas, Frame, BOTH, Text

class HuntingApp(tk.Tk):
    def __init__(self, bot, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.HEIGHT = 1000
        self.WIDTH = 1000
        self.delta_x = 1
        self.delta_y = 1
        self.parent = self
        self.parent.title ("MAP")
        self.canvas = Canvas (height=self.HEIGHT, width=self.WIDTH, bg='white')
        self.canvas.pack (fill=BOTH)
        self.bot = bot
        self.paint_map(bot.Map)
        self.NextSearch()

    def NextSearch(self):
        self.bot.RunStep()
        self.canvas.delete ("all")
        self.paint_map(self.bot.Map)
        self.paint_last_searched_cell()
        self.paint_target_cell()
        self.updateLandscape(self.bot.getBelief())
        self.after(1000, self.NextSearch)

    def paint_map (self, matrix):

        rows = len (matrix)
        cols = len (matrix[0])

        self.delta_x = self.HEIGHT / (cols+2)
        self.delta_y = self.WIDTH / (rows+2)

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

                self._paint_cell (i, j, _cell_color, self.delta_x, self.delta_y)

    def _paint_cell (self, rw, cl, color, deltax, deltay):
        x0 = cl * deltax
        x1 = x0 + deltax
        y0 = rw * deltay
        y1 = y0 + deltay
        self.canvas.create_rectangle (x0, y0, x1, y1, fill=color, tags="cursor")

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
                self.canvas.create_text ((x0 + x1) // 2, (y0 + y1) // 2,  text= "(%f)" % (matrix[i][j]))

    def paint_target_cell(self):

        x0 = self.bot.target_j * self.delta_x
        x1 = x0 + 20
        y0 = self.bot.target_i * self.delta_y
        y1 = y0 + 20
        self.canvas.create_rectangle (x0, y0, x1, y1, fill='red', tags="cursor")

    def paint_last_searched_cell(self):
        print(self.bot.lastSearched_i)
        print(self.bot.lastSearched_j)
        x1 = (self.bot.lastSearched_j+1) * self.delta_x
        x0 = x1 - 20
        y1 = (self.bot.lastSearched_i+1) * self.delta_y
        y0 = y1 - 20
        self.canvas.create_rectangle (x0, y0, x1, y1, fill='black', tags="cursor")
