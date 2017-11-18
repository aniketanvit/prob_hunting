from probabilistic_hunting_target_present import ProbabilisticHunting_TargetPresent
from HuntingApp import HuntingApp

if __name__ == '__main__':
    app = HuntingApp (ProbabilisticHunting_TargetPresent(5))
    app.mainloop ()
