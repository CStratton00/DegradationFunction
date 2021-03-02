"""
Collin Stratton
CST-305
Topic 4 Project 4: Degradation of Data Integrity
Dr. Ricardo Citro

For this project, the equation in this program were solved by hand as detailed from 
the documentation and the following program serves as the visual representation of 
the data degredation over time

Implementation approach:
- Solved the by hand problem from the assignment
- Developed a function based on the answer in the assignment
- Created a t space and x space for graphing
- Graphed the function
"""

# Packages used: time, numpy, matplotlib
import numpy as np                  # import numpy for array space
import matplotlib.pyplot as plt     # import matplotlib for graphing functions

# Function from Part 2: x(t) = e^((1 / 20) * t)
def func(t):
    return np.exp((-1 / 20) * t)    # return the time

# Array creation
ts = []         # tspace containing the time on the x axis
xs = []         # xspace containing the data on the y axis

ts = np.linspace(0, 150, 1000)  # create a t space
for i in ts :                   # create x values for every value of t
    xs.append(func(i))          # append all the values of x into the xspace

plt.title("Function Analysis")          # set the title of the graph
plt.xlabel("t")                         # set the x label on the graph
plt.ylabel("x")                         # set the y label on the graph
plt.plot(ts, xs, 'r-', linewidth = 2)   # set the line to be red and label it
plt.show()                              # displays the graph