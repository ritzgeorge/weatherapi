import matplotlib as mpl
import matplotlib as mpl
import numpy as np
import csv
with open('/Users/ritzgeorge/Downloads/1880-2017.csv', 'r') as f:
    wines = list(csv.reader(f, delimiter=';'))
import matplotlib.pyplot as plt
data = np.genfromtxt('/Users/ritzgeorge/Downloads/1880-2017.csv', delimiter=',', dtype=None, skip_header=5, names=('date', 'value', 'anomaly'))
plt.title('Global Land and Ocean Temperature Anomalies, June')
plt.xlabel('year')
plt.ylabel('degrees F +/- from average')
plt.bar(data['date'], data['value'], color='blue')
plt.show()