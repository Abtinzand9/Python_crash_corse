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
fig = px.bar(x=poss_results , y=frequencies)
fig.show()