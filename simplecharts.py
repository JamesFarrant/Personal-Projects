import matplotlib.pyplot as plt

# X and Y must be the same.
x = [1, 2, 3, 4, 5]
y = [4, 7, 4, 7, 3]
# Adding a new line
y2 = [5, 3, 2, 6, 2]
# Plotting the graph and adding labels to lines
plt.plot(x, y, label='Initial Line')
plt.plot(x, y2, label='New Line')
# Labelling our axes and adding title
plt.xlabel('Plot Number')
plt.ylabel('Random Numbers')
plt.title('My Awesome Graph')
# Legends are added here
plt.legend()
# This must be last to show everything.
plt.show()
