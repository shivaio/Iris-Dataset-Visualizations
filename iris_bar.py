import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv("Iris.csv")


species_list = list(set(list(df[:]['Species'])))
print(species_list)
species_count_dict = dict(df[:]["Species"].value_counts())
print(species_count_dict)


species_count = list(species_count_dict.values())

fig = plt.figure(figsize=(10, 5))

plt.bar(species_list, species_count, color='green',width=0.2)

plt.xlabel("Species")
plt.ylabel("Count")
plt.title(" species and their count in dataset")
plt.show()