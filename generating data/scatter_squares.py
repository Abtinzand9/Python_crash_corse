import matplotlib.pyplot as plt 

# style the plot
plt.style.use("seaborn-v0_8")
x_values = range(1,1001)
y_vlaues = [x**2 for x in x_values]

fig , ax = plt.subplots()
ax.scatter(x_values , y_vlaues, c = y_vlaues , cmap= plt.cm.Blues ,s=10 )
ax.set_title("Squre Numbers" , fontsize = 24)
ax.set_xlabel("Value" , fontsize = 14)
ax.set_ylabel("Squre of Value" , fontsize = 14)
# set size of tick lables
ax.tick_params(labelsize =14)
#set the range of each arry 
ax.axis([0,1001,0,1_100_000])
ax.ticklabel_format(style='plain')
plt.savefig('squre_plot.png' , bbox_inches = "tight")
plt.show()
