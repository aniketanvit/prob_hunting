from probabilistic_hunting_move_cost import ProbabilisticHunting_WithCost_Rule2
from HuntingApp import HuntingApp

if __name__ == '__main__':
    app = HuntingApp (ProbabilisticHunting_WithCost_Rule2(5))
    app.mainloop ()
