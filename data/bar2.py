import matplotlib.pyplot as plt
import numpy as np

y = np.arange(4)
country = ['Germany', 'US', 'Korea', 'Canada']
values = [9, 243, 45, 239]


plt.title("The figure of Gold medal in four different countries")
plt.grid(True, axis='x', color='#D9E4E7', alpha=0.5, linestyle='--')
plt.barh(y, values, height=-0.6, align='edge', color="#537D7F",
       linewidth=3, tick_label=country)

plt.show()