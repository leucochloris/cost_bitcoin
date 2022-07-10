import matplotlib.pyplot as plt
import json
from datetime import datetime

def get_data():
    with open('market-price.json') as file:
        data = json.load(file)
        return data

def data_plot():
    data = get_data()
    x_list = []
    y_list = []
    for i in data['values']:
        x_list.append(datetime.utcfromtimestamp(i['x']))
        y_list.append(i['y'])
    return x_list, y_list

plt.title ('Graphic of cost Bitcoin', fontsize=13, fontweight='bold', color = 'blue')
plt.xlabel ('Period', fontsize=10, color='black')
plt.ylabel ('Cost', fontsize=10, color='black')
plt.plot(*data_plot(), label='Market cost')
plt.legend()
plt.grid()
plt.show()
