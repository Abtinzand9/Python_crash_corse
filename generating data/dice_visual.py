from die import Die
import plotly.express as px
# genrating date
die_1 = Die()
die_2 = Die()
results = []
for num_rols in range(1000):
    result=die_1.roll() + die_2.roll()
    results.append(result)

# analizing the date
frequencies =[]
poss_results = range(2 , die_1.sides +die_2.sides+1)
for value in poss_results:
    frequencie = results.count(value)
    frequencies.append(frequencie)

# visulize the result
title = "roll two 6-side dice for 1000 times"
labels = {'x' : 'results' , 'y' : 'frequenci of resultes' }
fig = px.bar(x=poss_results , y=frequencies , title = title , labels = labels)
# Further customize chart.
fig.update_layout(xaxis_dtick=1)
fig.show()