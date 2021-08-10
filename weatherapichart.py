import requests
import json
import matplotlib as mpl
import matplotlib.pyplot as plt

url = "http://www.7timer.info/bin/api.pl?lon=113.17&lat=23.09&product=astro&output=json"

headers = {
    'x-rapidapi-key': "61cd17ac53mshf4140b8efd02cc0p1500d1jsn1b0f279eec5f",
    'x-rapidapi-host': "dark-sky.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers)

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())
data_as_string= response.json()['dataseries']
jprint(data_as_string)
#create a list for temperature values
Temperatures = []

for d in data_as_string:
    temp = d['temp2m']
    Temperatures.append(temp)

#create a list for timepoints
Timepoints = []

for d in data_as_string:
    time = d['timepoint']
    Timepoints.append(time)

#plotting the chart
plt.title('Temperatures obtained from 7timer')
plt.xlabel('Timepoint')
plt.ylabel('degrees F +/- from average')
plt.bar(Timepoints, Temperatures, color='blue')
plt.show()