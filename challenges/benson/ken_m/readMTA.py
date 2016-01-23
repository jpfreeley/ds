import csv
import datetime
from collections import defaultdict
import matplotlib.pyplot as plt
import os.path
import pandas as pd
%matplotlib inline
import seaborn as sns

def read_file(filename):
    d = []
    with open(filename) as file:
        data = csv.reader(file)
        for row in data:
            d.append(row)
    
    for item in d:
        item[-1] = item[-1].rstrip()
        
    d = d[1:]
    return d
    #print(d)

def get_turnstiles(filename):
    data = read_file(filename)
    #print(data[1])
    newDict = defaultdict(list)
    for item in data:
        newDict[tuple(item[:4])].append(item[4:])
        
    return newDict

def print_x_dict_kv(dictionary, numKeys):
    for key in sorted(dictionary)[:numKeys]:
        print("{}: {}".format(key,dictionary[key]))
        
def get_ts_timeseries(filename):
    data = get_turnstiles(filename)
    newDict = defaultdict(list)
    for k,v in data.items():
        for item in v:
            dt = item[2] + ' ' + item[3]
            dt = datetime.datetime.strptime(dt, "%m/%d/%Y %H:%M:%S")
            entries = int(item[5])
            ts = [dt, entries]
            newDict[k].append(ts)
    
    for k,v in newDict.items():
        newDict[k] = sorted(v)
    
    for item in newDict.values():
        assert item == sorted(item)        

    return newDict

#IMPORTANT, returns a dict with [datetime,count between times,timedelta] value
def get_ts_timeblock_entries(filename):
    data = get_ts_timeseries(filename)
    
    newDict = {turnstile: [[v[i][0],
                            v[i+1][1]-v[i][1],
                            v[i+1][0]-v[i][0]] for i in range(len(v)-1) 
                            if 0 <= v[i+1][1]-v[i][1] <= 5000] 
                            for turnstile,v in data.items()}
    
    return newDict

def get_ts_daily_entries(filename):
    #data = get_ts_timeseries(filename)
    data = get_ts_timeblock_entries(filename)
    
    newDict = defaultdict(dict)
    
    for k,v in data.items():
        dayDict = {}
        t_entries = 0
        
        for item in v:
            day = item[0].date()
            t_entries += item[1]
            #hour_gap = item[2].total_seconds() / 60 / 60
            #avg_entries = item[1] / hour_gap'''
            dayDict[day] = dayDict.get(day, 0) + item[1]
        
        newDict[k] = sorted(dayDict.items())
        
    return newDict

def plot_a_ts_daily_ent(filename, ts):
    data = get_ts_daily_entries(filename)
    dates = []
    counts = []
    
    for item in data[ts]:
        dates.append(item[0])
        counts.append(item[1])
    
    dates, counts = (list(t) for t in zip(*sorted(zip(dates, counts))))
    
    ts_name = ", ".join(ts)
    title_name = ts_name + " " + os.path.splitext(filename)[0]
    
    plt.figure(figsize=(10,3))
    plt.title(title_name)
    plt.xlabel('Day')
    plt.ylabel('Entries')
    plt.plot(dates,counts)
    
def ts_group_daily_entry(filename):
    data = get_ts_daily_entries(filename)
    
    newDict = defaultdict(lambda : defaultdict(int))
    list = []
    for k,v in data.items():
        newKey = k[:2] + (k[3],)
        for item in v:
            newDict[newKey][item[0]] += item[1]
    
    return newDict

def group_by_station(filename):
    data = ts_group_daily_entry(filename)
    
    newDict = defaultdict(lambda: defaultdict(int))
    for k,v in data.items():
        newKey = k[2]
        for l,w in v.items():
            newDict[newKey][l] += w
            
    return newDict

def plot_station_week(filename, station):
    data = group_by_station(filename)
    dates = []
    counts = []
    
    for k,v in data[station].items():
        dates.append(k)
        counts.append(v)
    
    dates, counts = (list(t) for t in zip(*sorted(zip(dates, counts))))
    #print(dates,counts)
    
    title_name = station + " " + os.path.splitext(filename)[0]
    
    plt.figure(figsize=(10,3))
    plt.title(title_name)
    plt.xlabel('Day')
    plt.ylabel('Entries')
    plt.plot(dates,counts)
    
def plot_multiple_weeks(station, *args):
    week_day_names = ["Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday"]
    x = [1,2,3,4,5,6,7] 
    labels = []
    
    plt.figure(figsize=(10,5))
    plt.xticks(x, week_day_names, rotation='vertical')    
    
    for file in args:
        data = group_by_station(file)
        
        week_day_list = []
        week_count_list = []
        for k,v in data[station].items():
            week_day_list.append(k)
            week_count_list.append(v)
        
        labels.append(station + "-" + os.path.splitext(file)[0])
            
        week_day_list, week_count_list = (list(t) for t in zip(
                *sorted(zip(week_day_list, week_count_list))))
        
        #print(week_day_list, week_count_list)
        
        plt.plot(x,week_count_list)
    
    title_name = station + ' Total Entries for Multiple Weeks'
    
    plt.title(title_name, y = 1.1)
    plt.xlabel('Day of Week')
    plt.ylabel('Entries')
    plt.legend(labels, ncol=4, loc='upper center', 
               bbox_to_anchor=[0.5, 1.1], 
               columnspacing=1.0, labelspacing=0.0,
               handletextpad=0.0, handlelength=1.5,
               fancybox=True, shadow=True)
    
def sum_tot_riders_by_station(*args):
    
    stationDict = defaultdict(int)
    
    for file in args:
        data = group_by_station(file)
        
        for k,v in data.items():
            for l,w in v.items():
                stationDict[k] += w
                
    
    stationList = list(stationDict.items())
    stationList.sort(key=lambda x: x[1])
    #print(stationList)
    
    return stationList

def plot_total_riders(*args):
    data = sum_tot_riders_by_station(*args)
    
    numStations = len(data)
    x = range(1,numStations+1)
    stationNames = []
    stationEntries = []
    
    for item in data:
        stationNames.append(item[0])
        stationEntries.append(item[1])
        
    title_name = "Top 20 Subway Stations by Entries over Four Week Period"    
        
    plt.figure(figsize=(10,5))
    plt.title(title_name)
    plt.xticks(x, stationNames, rotation='vertical')
    plt.xlabel('Station')
    plt.ylabel('Entries')
    plt.bar(x[-20:], stationEntries[-20:])
    
def dframes_of_weeks_and_hours(*args): 
    
    '''{(c/a, unit, station):
                            {day:
                                {time: count}
                            }
        }'''
    
    full_dict = defaultdict(lambda : defaultdict(lambda :defaultdict(int)))
    cols = ["Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday"]
    
    for file in args:
        data = get_ts_timeblock_entries(file)    
        
        
        for k,v in data.items():
            newKey = k[:2] + (k[3],)
            #by_day = defaultdict(lambda : defaultdict(int))
            
            for item in v:
                day_string = item[0].strftime("%A")
                time = item[0].time()
                full_dict[newKey][day_string][time] += item[1] 
    
    
    df_dict = {turnstile: pd.DataFrame.from_dict(value) 
               for turnstile, value in full_dict.items()}
    for k,v in df_dict.items():
        df_dict[k] = v[cols]
        
    return df_dict



summer_data = dframes_of_weeks_and_hours('turnstile_150530.csv',  'turnstile_150606.csv', 
                                         'turnstile_150613.csv', 'turnstile_150620.csv', 
                                         'turnstile_150627.csv', 'turnstile_150704.csv', 
                                         'turnstile_150711.csv', 'turnstile_150718.csv', 
                                         'turnstile_150725.csv', 'turnstile_150801.csv', 
                                         'turnstile_150801.csv', 'turnstile_150808.csv', 
                                         'turnstile_150815.csv', 'turnstile_150822.csv', 
                                         'turnstile_150829.csv', 'turnstile_150905.csv', 
                                         'turnstile_150912.csv')

penn = summer_data[('N069', 'R013', '34 ST-PENN STA')]
st_49 = summer_data[('A016', 'R081', '49 ST-7 AVE')]
#print(penn)

def get_heatmap_for_entryway(place):
    sns.heatmap(place)
    
get_heatmap_for_entryway(penn)
        