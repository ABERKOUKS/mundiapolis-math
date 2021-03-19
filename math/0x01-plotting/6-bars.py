#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4,3))

apples=fruit[0,:]
bananas=fruit[1,:]
oranges=fruit[2,:]
peaches=fruit[3,:]

labels = ['Farrah', 'Fred', 'Felicia']
legend = ['apples', 'bananas', 'oranges', 'peaches']
width = 0.5       # the width of the bars

color_list = ['red','yellow','#ff8000','#ffe5b4']
fig, ax = plt.subplots()
ax.set_ylim([0,80])
for i in range(fruit.shape[0]):
  plt.bar(labels, fruit[i],
            bottom = np.sum(fruit[:i], axis = 0),
            color=color_list[i % len(color_list)],
            width=width
  )

plt.ylabel("Quantity of Fruit") 
plt.legend(["apples", "bananas", "oranges", "peaches"]) 
plt.title("Number of Fruit per Person") 
plt.show()
