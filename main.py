#from melextract01 import mel_extractor_function
#from datetime import datetime, timedelta 
#from dateutil import parser
#from datetime import datetime
#import pandas as pd
#from time_fix import time_fix_function 
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from melextract01 import mel_extractor_function
from time_range import time_range_function_3
from get_functions import get_taf_function,get_time_function_1,get_time_function_2, get_time_function_3
"""WARNING DO NOT PUT TAF IN FOR KBFM TAF WILL NOT WORK DUE TO CONFLICTING CODE IN pytaf.py"""


#quote_page = 'https://www.aviationweather.gov/adds/dataserver_current/httpparam?datasource=tafs&requestType=retrieve&format=xml&mostRecentForEachStation=true&hoursBeforeNow=2&stationString=' + value

def running_mel_extractor_function():
    mel_type_list = list()
    reference_time=time_range_function_3()
    content00 = get_taf_function()
    content01 = get_time_function_1()
    content02 = get_time_function_2()
    content03 = get_time_function_3()
    for values00,valuesxx,valueszz,valuesuu in zip(content00,content01,content02,content03):
        dumby_list = ['NaN'] * len(reference_time)
        each_array=mel_extractor_function(values00,valuesxx,valueszz,valuesuu) 
        winter_precip = each_array[0]
        time_stamp_reference=each_array[1]
        print(time_stamp_reference)
        print(each_array[2])
        if len(time_stamp_reference)>len(reference_time):
            for values01,values02 in zip(time_stamp_reference, winter_precip): 
                try:
                    index=reference_time.index(values01)
                    dumby_list[index] = values02
                except:
                    print ("No index ")
        elif len(time_stamp_reference)==len(reference_time):    
            for values01,values02 in zip(time_stamp_reference, winter_precip): 
                try:
                    index=reference_time.index(values01)
                    dumby_list[index] = values02
                except:
                    print ("No index ")
        elif len(time_stamp_reference)<len(reference_time): 
            for values01,values02 in zip(time_stamp_reference, winter_precip):    
                try:
                    index=reference_time.index(values01)
                    dumby_list[index] = values02
                except:
                    print ("No index ")
        mel_type_list.append(dumby_list)
        dumby_list = []
    return(mel_type_list)

print(running_mel_extractor_function())

print('')
print('Completed MEL Extractions from TAFs')
print('')
