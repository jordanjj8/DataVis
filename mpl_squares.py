# Jordan Leung
# 5/2/2019

import matplotlib.pyplot as plt
x = [1,2,3,4,5]
squares = [1, 4, 9, 16, 25]
# controls the thickness of the line that plot() generates
plt.plot(x,squares, linewidth=5)

#Set chart title and label axes
plt.title("Square Numbers", fontsize=20)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of the Value", fontsize=14)

# set size of tick labels
plt.tick_params(axis='both', labelsize=14)



plt.show()
