# Jordan Leung
# 6/5/2019
import pygal
from die import Die

# create an instance D6
die = Die()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# analyze the results
frequencies = []
for die_num in range(1, die.num_sides+1):
    frequency = results.count(die_num)
    frequencies.append(frequency)

# visualize the results
hist = pygal.Bar() #calls an instance of a bar graph
hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = ['1','2','3','4','5','6']
hist.y_title = "Frequency of Rolled Number"
hist.x_title = "Die Number"
hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')

