from probabilistic_hunting_target_present import ProbabilisticHunting_TargetPresent

if __name__ == '__main__':
    bot = ProbabilisticHunting_TargetPresent(50)
    required_time = int(input("Enter the timestep at which you want to compute Belief : "))
    given_cell_row = int(input("Enter the row of cell for which you want to compute Belief : "))
    given_cell_col = int(input("Enter the col of cell for which you want to compute Belief : "))
    current_time = 0
    while(bot.currentTime < required_time):
        row_index = int(input("Enter the row of cell to search: "))
        col_index = int(input("Enter the col of cell to search: "))
        bot.updateBelief(row_index, col_index)
        print("Belief for target being present at cell (%d, %d) after time %d is %f." % (given_cell_row, given_cell_col,
              bot.currentTime, bot.Belief[given_cell_row][given_cell_col]))
