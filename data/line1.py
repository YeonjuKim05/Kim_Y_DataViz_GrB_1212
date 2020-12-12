import matplotlib.pyplot as plt

title_font = {
	'fontsize' : 10,
	'fontweight' : 'bold'
}

year = [2006, 2010, 2014]
pop_US = [9, 7, 10]
pop_CANADA = [7, 14, 25]



plt.plot(year, pop_US, color='g')
plt.plot(year, pop_CANADA, color='orange')


plt.grid(True, axis='y', color='red', alpha=0.5, linestyle='--')

plt.ylabel("The amoount of total Gold medal")

plt.xlabel("Year")

plt.title("The figure of total gold medals between US and Canada over 12years", pad="20", fontdict=title_font)

plt.show()