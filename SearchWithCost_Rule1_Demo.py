from probabilistic_hunting_move_cost import ProbabilisticHunting_WithCost_Rule1
from HuntingApp import HuntingApp

if __name__ == '__main__':
    app = HuntingApp (ProbabilisticHunting_WithCost_Rule1(5))
    app.mainloop ()

    # bot = ProbabilisticHunting_WithCost_Rule1(10)
    # print(bot.startHunt())
