import matplotlib.pyplot as plt

# x = [0, 1, 2, 3, 4, 5]
# y = [0, 2, 4, 6, 8, 10]

#plt.plot(x, y) # oppretter et plott
#plt.show() # viser plottet

x = []
y = []

for i in range(6):
    x.append(i)
    y.append(3*i + 2)

plt.plot(x, y) # linjer
plt.scatter(x, y) # punkter
plt.show()

