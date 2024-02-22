from matplotlib import pyplot as plt
from rendom_walk import RandomWalk

# make a random walk
rw = RandomWalk()
rw.fill_walk()

#plot points 
plt.style.use('_classic_test_patch')
fig , ax = plt.subplots()
ax.scatter(rw.x_values , rw.y_values , s =15)
ax.set_aspect('equal')
plt.show()