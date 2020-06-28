import matplotlib.pyplot as plt
plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

from urllib.request import urlopen
from xml.etree import ElementTree as ET


def get_currencies(currencies_ids_lst=['R01010', 'R01035', 'R01100', 'R01115', 'R01235', 'R01239', 'R01350', 'R01565', 'R01625', 'R01775']):

    cur_res_str = urlopen("http://www.cbr.ru/scripts/XML_daily.asp")

    result = {}

    cur_res_xml = ET.parse(cur_res_str)

    root = cur_res_xml.getroot()
    valutes = root.findall('Valute')
    for el in valutes:
        valute_id = el.get('ID')

        if str(valute_id) in currencies_ids_lst:
            valute_cur_val = el.find('Value').text
            result[valute_id] = valute_cur_val
            #valute_cur_charcode = el.find('CharCode').text  

    return result


# TODO 0


# Вывести на графике 10 валют (получить по кодам валюты из ЦБС)


cur_vals = get_currencies()

objects = cur_vals.keys()

#print(cur_vals)

y_pos = np.arange(len(objects))

# TODO #1 переписать лямбда-функцию из следующей строки через list comprehension

# или генераторы списков (как мы их называем)   
performance = [float(x.replace(",",".")) for x in cur_vals.values()]   
print(performance)  

# TODO #2

#  Подписи должны быть у осей (x, y), у графика, у «рисок» (тиков),
# столбцы должны быть разных цветов с легендой

N = 5
menMeans = (20, 35, 30, 35, 27)
womenMeans = (25, 32, 34, 20, 25)
menStd = (2, 3, 4, 1, 2)
womenStd = (3, 5, 2, 3, 3)
ind = np.arange(N) # the x locations for the groups
width = 0.35 # the width of the bars: can also be len(x) sequence
p1 = plt.bar(ind, menMeans, width, yerr=menStd)
p2 = plt.bar(ind, womenMeans, width, bottom=menMeans, yerr=womenStd)
plt.xlabel('Groups')
plt.ylabel('Scores')
plt.title('Scores by group and gender')
plt.xticks(ind, ('G1', 'G2', 'G3', 'G4', 'G5'))
plt.yticks(np.arange(0, 81, 10))
plt.legend((p1[0], p2[0]), ('Men', 'Women'))
plt.show()
