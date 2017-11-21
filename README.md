Packages used :
Tkinter - for visualisation, 
Matplotlib - for plots, 
Numpy - for array manipulation


Naming of files:
There is a file corresponding to each part of both questions. If you want to see the output for any part, go to the corresponding file and run the main() method in that file.

There are some files with the suffix - ‘Demo’. Run these main() method in these files if you want to see the animations for each search rule.

Main Classes : 
HuntingApp - This class is for the App inheriting from tkinter’s Tk class and is used for animating the search process. 

ProbabilisticHunting :  This class is the base class for all other classes for Question 1 and Question 2

ProbabilisticHunting_TargetPresent - This class implements the search behaviour which chooses the cell with maximum probability of the target being present in it.

ProbabilisticHunting_TargetFound - This class implements the search behaviour which chooses the cell with maximum probability of the target being found in it

ProbabilisticHunting_WithCost_Rule1 - This class implements the search behaviour which takes into account the cost of moving as well as the belief for the target being present in that cell (Rule 1 with cost for moving)

ProbabilisticHunting_WithCost_Rule2 - This class implements the search behaviour which takes into account the cost of moving as well as the belief for the target being found in that cell. (Rule 2 with cost for moving)

ProbabilisticHuntingPart2: This class is for part 2 of the assignment where the target moves after every iteration. Implemented with Rule1 and Rule2. Function def inline.
