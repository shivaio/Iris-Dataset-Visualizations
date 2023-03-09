import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import PercentFormatter

df = pd.read_csv("Iris.csv")

species_list = list(set(list(df[:]['Species'])))
print(species_list)
species_count_dict = dict(df[:]["Species"].value_counts())
print(species_count_dict)


species_count = list(species_count_dict.values())

df2 = pd.DataFrame({'count': species_count})
df2.index = species_list

df2 = df2.sort_values(by='count', ascending=False)


df2['cumperc'] = df2['count'].cumsum()/df2['count'].sum()*100

print(df2)


color1 = 'green'
color2 = 'blue'
line_size = 4


fig, ax = plt.subplots()
ax.bar(df2.index, df2['count'], color=color1,width=0.2)


ax2 = ax.twinx()
ax2.plot(df2.index, df2['cumperc'], color=color2, marker="D", ms=line_size)
ax2.yaxis.set_major_formatter(PercentFormatter())


ax.tick_params(axis='y', colors=color1)
ax2.tick_params(axis='y', colors=color2)


plt.show()