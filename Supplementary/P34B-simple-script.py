import matplotlib.pyplot as plt

x = ["Monday", "Tuesday", "Wednesday", "Thursday"]
y = ["a bit", "some", "loads", "I'm a genius"]

plt.plot(x, y)
plt.xlabel('Day of the course')
plt.ylabel('How much python you know')
plt.show()