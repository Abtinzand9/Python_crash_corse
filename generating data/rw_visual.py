from matplotlib import pyplot as plt
from rendom_walk import RandomWalk
# keep making random walk untill user say no
while True:
    # make a random walk
    rw = RandomWalk(50_000)
    rw.fill_walk()

    #plot points 
    plt.style.use('_classic_test_patch')
    # resoze the plot fign
    fig , ax = plt.subplots(figsize =(11,8))
    poin_numbers = range(rw.num_points)
    ax.scatter(rw.x_values , rw.y_values , c= poin_numbers , cmap = plt.cm.Blues ,edgecolors= 'none', s =1)
    # remove axis
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    ax.set_aspect('equal')
    # emphasize the starting and ending poins
    ax.scatter(0,0,c='green',edgecolor = 'none' ,s=100) 
    ax.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolor = 'none' ,s=100) 
    plt.show()
    keep_runnig = input("make anoter:(y/n)")
    if keep_runnig == 'n':
        break
