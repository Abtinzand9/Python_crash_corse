import matplotlib.pyplot as plt

squares = [1,4,9,16,25]
input_value = [1,2,3,4,5]

fig , ax = plt.subplots()
ax.plot(input_value,squares , linewidth = 3)
# set chart title and axie
ax.set_title("Squre Numbers" , fontsize = 24)
ax.set_xlabel("Value" , fontsize = 14)
ax.set_ylabel("Squre of value" , fontsize = 14)
# set size of tick lables
ax.tick_params(labelsize =14)

plt.show()