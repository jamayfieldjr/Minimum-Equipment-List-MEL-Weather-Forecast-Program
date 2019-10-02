from datetime import datetime,timedelta
from time_fix import time_fix_function
import pandas as pd

def time_range_function_1(): 
    utc_now = lambda : datetime.utcnow().strftime('%Y-%m-%d %H:%MZ')
    current_time=pd.to_datetime(utc_now()).strftime('%Y%m%d')
    current_year = int(current_time[0:4])
    current_month = int(current_time[4:6])
    current_day = int(current_time[6:8])
    starttime=datetime(current_year,current_month,current_day,2).strftime('%Y-%m-%dT%H:%M:%SZ')
    starttime=datetime.strptime(starttime, '%Y-%m-%dT%H:%M:%SZ')
     

    endtime=time_fix_function(current_time)
    return(starttime,endtime)

def datetime_range(start, end, delta):
    current = start
    
    while current < end:
        yield current
        current += delta

def time_range_function_2(): 
    dumbtime=time_range_function_1()
    starttime = dumbtime[0]
    endtime = dumbtime[1]
    print(starttime,endtime)
    reference_time = [dt.strftime('%d %HZ') for dt in datetime_range(starttime, endtime, timedelta(hours=1))]
    results =[]
    for values in reference_time:
        values = values[0:2] + '/'+ values[3:6]
        results.append(values)
    
    #results.append(addition)
    reference_time = results
    return(reference_time)

#print(time_range_function_2())

def time_range_function_3(): 
    dumbtime=time_range_function_1()
    starttime = dumbtime[0]
    endtime = dumbtime[1]
    reference_time = [dt.strftime('%Y-%m-%d %H:%M') for dt in datetime_range(starttime, endtime, timedelta(hours=1))]

    return(reference_time)

#print(time_range_function_3())

print('')
print('Completed Range Time')
