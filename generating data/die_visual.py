from die import Die
import plotly.express as px
# genrating date
die = Die()
results = []
for num_rols in range(1000):
    result=die.roll()
    results.append(result)

# analizing the date
frequencies =[]
poss_results = range(1 , die.sides +1)
for value in poss_results:
    frequencie = results.count(value)
    frequencies.append(frequencie)

# visulize the result
title = "roll a 6-side die for 1000 times"
labels = {'x' : 'results' , 'y' : 'frequenci of resultes' }
fig = px.bar(x=poss_results , y=frequencies , title = title , labels = labels)
fig.show()