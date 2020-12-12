import matplotlib.pyplot as plt

ratio = [107, 203, 315]
labels = ['BRONZE', 'SILVER', 'GOLD']
colors = ['#ff9999', '#ffc000', '#8fd9b6']
wedgeprops={'width': 0.7, 'edgecolor': 'w', 'linewidth': 5}


plt.title("The figure of 3 medal in Canada")
plt.pie(ratio, labels=labels, autopct='%.1f%%', startangle=260, counterclock=False, colors=colors, wedgeprops=wedgeprops)
plt.show()