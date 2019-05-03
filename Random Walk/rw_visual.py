# Jordan Leung
# 5/3/2019
# code to plot all the points in the walk

import matplotlib.pyplot as plt
from random_walk import RandomWalk

# keep making new walks as long as the while loop stays true
while True:

    # Make a random walk instance, and plot the points
    rw = RandomWalk()
    rw.fill_walk()

    #pass the c argument a list containing the position of each point
    # makes a list from 0 to rw.num_points
    point_num = list(range(rw.num_points))
    print(point_num)
    #prints plot
    plt.scatter(rw.x_values, rw.y_values, c=point_num, cmap=plt.cm.Blues, edgecolors='none', s=15)
    plt.show()

# ask user if another walk to be plotted is desired
    keep_running = input("Make another walk? (Y/N): ")
    if keep_running == 'N':
        break
    elif keep_running == 'Y':
        continue
    else:
        # catches any ambiguous answers
        while True:
            keep_running = input("Please type either Y or N: ")
            if keep_running == 'N' or keep_running == 'Y':
                break

# make a second random walk instance
#rj = RandomWalk(50)
#rj.fill_walk()
# s = 15 specifies the dot size
#plt.scatter(rj.x_values, rj.y_values, c=rj.x_values, cmap=plt.cm.Blues, s=15)
#plt.show()