import matplotlib.pyplot as plt
import numpy as np

x = np.arange(4)
country = ['Germany', 'US', 'Korea', 'Canada']
values = [8, 167, 51, 315]


plt.title("The figure of Gold medal in four different countries")

plt.bar(x, values, width=0.6, align='edge', color="#A77588",
         linewidth=3, tick_label=country)
plt.xticks(x, country)
plt.show()