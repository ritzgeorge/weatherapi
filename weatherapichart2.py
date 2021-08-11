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


# create a formatted string of the Python JSON object
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    #print(text)

jprint(response.json())
data_as_string= response.json()['dataseries']
jprint(data_as_string)



#create a list for temperature and timepoint values
#class obtain_values:
    #def __init__(self,temperatures,timepoints):
        #self.temperatures=temperatures
        #self.timepoints=timepoints 
temp_key='temp2m'
time_key='timepoint'

#class values(obtain_values):
   # def __init__(self,temperatures,timepoints):
        #values.__init__(self,temperatures,timepoints)

    
def value1(temperatures,timepoints):
    for d in data_as_string:
        if temp_key=='temp2m':
            temp = d['temp2m']
            temperatures.append(temp)
        if time_key=='timepoint':
            time = d['timepoint']
            timepoints.append(time)
           
    return temperatures,timepoints

    #plotting the chart
def plot(t,ti):
    plt.title('Temperatures obtained from 7timer')
    plt.xlabel('Timepoint')
    plt.ylabel('degrees F +/- from average')
    plt.bar(ti,t, color='blue')
    plt.show()

T1=[]
T2=[]

if __name__=="__main__":
    value1(T1,T2)
    print(T1)
    print(T2)
    plot(T1,T2)
        
        



