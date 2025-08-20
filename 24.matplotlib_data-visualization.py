"""
    Matplotlib, line plot
"""
import matplotlib.pyplot as plt
import numpy as np

# plt.style.use("ggplot")
plt.style.use("bmh")
 
# Line plot 
# create line y = 2 * x
arr_x = np.linspace(0, 5, 20)
arr_y = np.linspace(0, 10, 20)

# print(f'x: {arr_x}')
# print(f'y: {arr_y}')

# draw line
# Figure, Axes
fig, ax = plt.subplots() 

# draw 
ax.plot(arr_x, arr_y, color='red', linewidth=5, linestyle="dashdot") 
# ax.scatter(arr_x + np.array([1]), arr_y * np.array([2]), marker="*", color="yellow")
# save

# set attribute
ax.set_xlabel("Ox")
ax.set_ylabel("Oy")
ax.set_title("The title of the Axes")

fig.suptitle("The title of the Figure", fontsize=16)

plt.savefig("my_figure.png")

# display
plt.show()

# save
# plt.savefig("my_figure.png") # no content if you save after showing

"""
    Histogram
"""
# # create data
# data = np.random.randn(10000)

# # create figure, axes
# fig, ax = plt.subplots()

# # draw
# ax.hist(data, bins=60, color='red', alpha=0.15)

# # display
# plt.show()

"""
    Bar plot
"""
# # create data
# labels = ["class_A", "class_B", "class_C"]
# counts = [10, 15, 20]
# colors = ['red', 'green', 'blue']

# fig, ax = plt.subplots()

# ax.bar(labels, counts, color=colors)
# # ax.barh(labels, counts)
# plt.show()