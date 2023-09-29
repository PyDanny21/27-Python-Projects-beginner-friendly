import matplotlib.pyplot as plot


#set up the data
labels=('Python','C#','Java','PHP','Ruby')
index=(1,2,3,4,5)
sizes=90,20,54,76,18

#setting up bar chart
plot.bar(index,sizes,tick_label=labels)
plot.ylabel('Usage')
plot.xlabel('Programming Languages')
#display the chart
plot.show()
#pie chart set up
plot.pie(sizes,labels=labels,autopct='%1.f%%',counterclock=False,startangle=105)
plot.show()


def draw_scatterplot(x_values, y_values):
    plot.scatter(x_values, y_values, s=20)
    plot.title("Scatter Plot")
    plot.xlabel("x values")
    plot.ylabel("y values")
    plot.show()
draw_scatterplot()