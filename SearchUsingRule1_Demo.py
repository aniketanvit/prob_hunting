from probabilistic_hunting_target_present import ProbabilisticHunting_TargetPresent
from gui import LandscapeGUI
from tkinter import Tk
from tkinter import Canvas, Frame, BOTH

if __name__ == '__main__':
    bot = ProbabilisticHunting_TargetPresent(5)
    print(bot.Belief)
    #bot.startHunt()
    root = Tk ()
    grid = LandscapeGUI (root)
    grid.paint_map (bot.getMap())
    grid.updateData(bot.Belief)
    root.mainloop ()
