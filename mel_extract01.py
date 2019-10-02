# Import Libraries 
import pytaf
import re 
from datetime import datetime, timedelta 
from dateutil import parser
import numpy as np 
from get_functions import time_range_pull_program_3
from time_range import time_range_function_3

"""WARNING DO NOT PUT TAF IN FOR KBFM WILL NOT WORK"""

def mel_extractor_function(values,valuesxx,valueszz,valuesuu):
    print(valuesxx)
    #read values i.e. taf into the pytaf program 
    def read_taf_function(values):
        taf = pytaf.TAF(values)
        return(taf)

    taf=read_taf_function(values)

    def precip_extraction_function():

        """
        Function built for extracting precip group 
        """

        # initilzing vars
        
        precip_tf = []
        precip_type = []
        precip_groups = taf._raw_weather_groups
        print(precip_groups)
        precip = {
            'snow': r'\sSN\s|\s-SN\s|\s+SN\s',
            'pellets': r'\sPL\s|\s-PL\s|\s+PL\s|\sIC\s|\s-IC\s|\s+IC\s',
            'freezing': r'\sFZRA\s|\s-FZRA\s|\s+FZRA\s|\sFZDZ\s|\s-FZDZ\s|\s+FZDZ\s',
            'mix': r'RAPL|PLRA|SNPL|PLSN|SNFZDZ|SNFZRA|RASN|SNRA|DZSN|SNDZ'}

        for g in precip_groups:
            precip_tf.append(' '.join([k for k, v in precip.items() if re.search(v, g)]))

        for values in precip_tf:
            if values == 'snow':
                precip_type.append(100)
            elif values == 'pellets':
                precip_type.append(200)
            elif values == 'freezing':
               precip_type.append(300)
            elif values == 'mix':
                precip_type.append(400)
            elif values == '':
               precip_type.append(-999)

        return(precip_type)

    #print(precip_extraction_function())


    def datetime_range(start, end, delta):
        current = start
    
        while current < end:
            yield current
            current += delta

    def time_range_function(): 

        results=valuesuu 
        starttime=datetime.strptime(results[0],'%Y-%m-%dT%H:%M:%SZ').strftime('%Y-%m-%d %H:%M')
        endtime=datetime.strptime(results[1],'%Y-%m-%dT%H:%M:%SZ').strftime('%Y-%m-%d %H:%M')
        starttime=datetime.strptime(starttime,'%Y-%m-%d %H:%M')
        endtime=datetime.strptime(endtime,'%Y-%m-%d %H:%M')
        reference_time = [dt.strftime('%Y-%m-%d %H:%M') for dt in datetime_range(starttime, endtime, timedelta(hours=1))]

        return(reference_time)

    def winter_precip_function():

        precip_type = precip_extraction_function(taf)
        winter = re.compile(r"SN|FZ|PL|IC|SHSN")
        precip_tf=[]

        for values in precip_type:
            if not bool(winter.match(values)):
                precip_tf.append(0) 
            elif bool(winter.match(values)):
                precip_tf.append(1)
    

        return(precip_tf)

    def comparing_function():

        # winter precip is [number of line, number of reference time]  
        number_of_lines=precip_extraction_function()
        reference_time = time_range_function()
        reference_time_index = [i for i in range(len(reference_time))]
        winter_precip = np.zeros((len(number_of_lines), len(reference_time))) 
        precip_tf = precip_extraction_function()
        print(precip_tf)
        print(time_range_pull_program_3())
        # CHANGES 
        l = get_time_function_3()
        print(l)
        gotime, nogotime = zip(l)
        print('============================================================')
        print(gotime)
        print(type(gotime))
        print('============================================================')

        
        precip_tf = precip_extraction_function()
        line_reference_index = [i for i in range(len(precip_tf))]
    
        # for loop to loop thru the TAF lines 
        for values01,values02,values03,values04 in zip(gotime,nogotime,precip_tf,line_reference_index): 
            print(values01)
            startime=datetime.strptime(values01,'%Y-%m-%d %H:%M')
            endtime=datetime.strptime(values02, '%Y-%m-%d %H:%M')
            # for loop to loop thru the reference time 
            for values05,values06 in zip(reference_time,reference_time_index): 
                currenttime=datetime.strptime(values05, '%Y-%m-%d %H:%M') 

                if parser.parse(str(startime))<=parser.parse(str(currenttime))<parser.parse(str(endtime)):

                    if values03==100:
                        winter_precip[values04,values06] = 10 
                    elif values03==200: 
                        winter_precip[values04,values06] = 100
                    elif values03==300:
                        winter_precip[values04,values06] = 1000
                    elif values03==400:
                        winter_precip[values04,values06] = 10000
                    elif values03==-999:
                        winter_precip[values04,values06]= 3
        #print(winter_precip)
        winter_totals = np.sum(winter_precip,axis=0)
        #print(winter_totals)
        winter_weather = list()
        for values in winter_totals:
          if values>=10 and values<100:
              winter_weather.append('s')
          elif values>=100 and values<1000:
              winter_weather.append('p')
          elif values>=1000 and values<10000:
              winter_weather.append('f')
          elif values>=10000:
              winter_weather.append('m')
          elif values==3:
              winter_weather.append('n')
    
        return(winter_weather)



    def icao_station_info_function():
        station_id = taf._taf_header['icao_code']
        return(station_id)

    return(comparing_function(),time_range_function(valuesxx),icao_station_info_function())


#print(mel_extractor_function(values))
