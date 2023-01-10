# Import libraries
from matplotlib import pyplot as plt
import numpy as np


# Creating dataset
cars = ['bp', 'ld', 'wsd','pf']

data = [20,40,10,30]

# Creating plot
fig = plt.figure(figsize =(10, 7))
plt.pie(data, labels = cars)

# show plot
plt.savefig('books_read.png')