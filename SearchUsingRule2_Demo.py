from probabilistic_hunting_target_found import ProbabilisticHunting_TargetFound
from gui import LandscapeGUI
from tkinter import Tk
#from tkinter import Canvas, Frame, BOTH

if __name__ == '__main__':
    bot = ProbabilisticHunting_TargetFound(5)
    print(bot.Belief_Found)
    #bot.startHunt()
    root = Tk ()
    grid = LandscapeGUI (root)
    grid.paint_map (bot.getMap())
    grid.updateData(bot.Belief_Found)
    root.mainloop ()
