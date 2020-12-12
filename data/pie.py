import matplotlib.pyplot as plt
import numpy as np

ratio = [274, 49, 158]
labels = ['Ice Hockey', 'Curling', 'Skating']
explode = [0.05, 0.05, 0.05]
colors = ['#ff9999', '#ffc000', '#8fd9b6']

plt.title("The percentage of total medal in 3 different sports from Canada")
plt.pie(ratio, labels=labels, autopct='%.1f%%', startangle=260, counterclock=False, explode=explode, shadow=True, colors=colors)
plt.show()