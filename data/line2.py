import matplotlib.pyplot as plt

title_font = {
	'fontsize' : 10,
	'fontweight' : 'bold'
}

x = [2002, 2006, 2010, 2014]
y = [17, 24, 26, 25]



plt.plot(x, y, color='#A68E75', linestyle='dashed', linewidth = 3, 
         marker='o', markerfacecolor='#9CCBD1', markersize=12)

plt.ylim(17, 30)
plt.xlim(2002, 2014)


plt.grid(True, axis='y', color='#3F6845', alpha=0.5, linestyle='--')

plt.ylabel("The amoount of total medals in CANADA")
plt.xlabel("Year")

plt.title("The figure of total medals in Canada over the period", pad="20", fontdict=title_font)

plt.show()