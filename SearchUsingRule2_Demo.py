from probabilistic_hunting_target_found import ProbabilisticHunting_TargetFound

from HuntingApp import HuntingApp

if __name__ == '__main__':
    app = HuntingApp (ProbabilisticHunting_TargetFound(5))
    app.mainloop ()
