from datetime import datetime 

def time_fix_function(current_time):
    current_year = int(current_time[0:4])
    current_month = int(current_time[4:6])
    current_day = int(current_time[6:8])

    if current_month==1 or current_month==3 or current_month==5 or current_month==7 or current_month==8 or current_month==10 or current_month==12:

        if current_day==31:
            end_day = 1  
            result = datetime(current_year,current_month,end_day,2,00).strftime('%Y-%m-%dT%H:%M:%SZ')
        else: 
            end_day = current_day + 1  
            result = datetime(current_year,current_month,end_day,2,00).strftime('%Y-%m-%dT%H:%M:%SZ')
   
    elif current_month==4 or current_month==6 or current_month==9 or current_month==11:

        if current_day==30:
            end_day = 1  
            result = datetime(current_year,current_month,end_day,2,00).strftime('%Y-%m-%dT%H:%M:%SZ')
        else: 
            end_day = current_day + 1  
            result = datetime(current_year,current_month,end_day,2,00).strftime('%Y-%m-%dT%H:%M:%SZ')


    elif current_month==2:

        if current_year==2020 or current_year==2024: 

            if current_day==29:
                end_day = 1  
                result = datetime(current_year,current_month,end_day,2,00).strftime('%Y-%m-%dT%H:%M:%SZ')
            else: 
                end_day = current_day + 1  
                result = datetime(current_year,current_month,end_day,2,00).strftime('%Y-%m-%dT%H:%M:%SZ')

        else:

            if current_day==28:
                end_day = 1  
                result = datetime(current_year,current_month,end_day,2,00).strftime('%Y-%m-%dT%H:%M:%SZ')
            else: 
                end_day = current_day + 1  
                result = datetime(current_year,current_month,end_day,2,00).strftime('%Y-%m-%dT%H:%M:%SZ')

    endtime = result 
    endtime = datetime.strptime(endtime, '%Y-%m-%dT%H:%M:%SZ')
    return(endtime)
