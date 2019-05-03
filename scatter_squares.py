# Jordan Leung
# 5/3/2019

import matplotlib.pyplot as plt

x_values = list(range(1,1001))
y_values = [ x**2 for x in x_values]

#plt.scatter(x_values, y_values, c='red', edgecolor='none', s=40)
# using a colormap, where each y-value is assigned a color, color maped chosen by cmap
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, edgecolor='none', s=40)

#Set chart title and label axes
plt.title("Scatter Square Numbers Plot", fontsize=14)
plt.xlabel("X Value", fontsize=14)
plt.ylabel("Squared Value", fontsize=14)

#Set the range for each axis
#plt.axis([0, 1100, 0, 1100000])

plt.show()
#to save the plot automatically
#plt.savefig('squares_plot.png', bbox_inches='tight')


