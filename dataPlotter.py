import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import csvWorker
from seaborn import barplot

sns.set_style('darkgrid') # darkgrid, white grid, dark, white and ticks
plt.rc('axes', titlesize=18)     # fontsize of the axes title
plt.rc('axes', labelsize=14)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=13)    # fontsize of the tick labels
plt.rc('ytick', labelsize=13)    # fontsize of the tick labels
plt.rc('legend', fontsize=13)    # legend fontsize
plt.rc('font', size=10)          # controls default text sizes

global list
list = [
    ['t-shirt', 'trousers', 'pullover shirt', 'dress', 'coat', 'sandal', 'shirt', 'sneakers', 'bag/backpack', 'boots'],
    [],
    [],
    []
]

# update the data list for graphs, called everytime when use all the graphing functions
def update_list():
    csvWorker.read_data()
    global list
    temp = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    total = 0
    for row in csvWorker.data:
        str = row[1]
        id = -1
        if  str == "t-shirt":
            id = 0
        if  str == "trousers":
            id = 1
        if str == "pullover shirt":
            id = 2
        if str == "dress":
            id = 3
        if str == "coat":
            id = 4
        if str == "sandal":
            id = 5
        if str == "shirt":
            id = 6
        if str == "sneakers":
            id = 7
        if str == "bag/backpack":
            id = 8
        if str == "boots":
            id = 9
        temp[id] = temp[id] + 1
        total = total + 1
    list[1] = temp
    x = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(10):
        x[i] = float(temp[i])/total
    list[2] = x

    for row in csvWorker.data:
        list[3].append(row[3])

def bar_graph():
    update_list()
    plt.figure(figsize=(8,4), tight_layout=True)
    colors = sns.color_palette('pastel')
    plt.bar(list[0], list[1], color=colors[:5])
    plt.xlabel('Type')
    plt.ylabel('Quantity')
    plt.title('Bar Graph')
    # plt.savefig('graphs/bar_graph.png')
    plt.show()

def pie_graph():
    update_list()
    colors = sns.color_palette('pastel')
    plt.figure(figsize=(8, 6), tight_layout=True)

    plt.pie(list[1], labels=list[0], autopct='%.0f %%', pctdistance=.7,
              colors=colors, shadow=True)

    plt.title('Pie Chart', weight='bold')
    # plt.savefig('graphs/pie_graph.png')
    plt.show()

def line_graph():
    update_list()
    plt.figure(figsize=(10,6), tight_layout=True)

    plt.plot(list[3], 'o-', linewidth=2)

    plt.xlabel('Time picture taken')
    plt.ylabel('Price')
    plt.title('Clothes Price Over Time')

    # plt.savefig('graphs/line_graph.png')
    plt.show()

# update_list()
# print(list[0])
# print(list[1])
# print(list[2])

# line_graph()
