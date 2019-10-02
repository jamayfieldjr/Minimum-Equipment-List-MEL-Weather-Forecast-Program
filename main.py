#libs
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from melextract01 import mel_extractor_function
from time_range import time_range_function_2, time_range_function_3
from get_functions import get_taf_function,get_time_function_1,get_time_function_2, get_time_function_3
"""WARNING DO NOT PUT TAF IN FOR KBFM TAF WILL NOT WORK DUE TO CONFLICTING CODE IN pytaf.py"""

station_list=['KMEM','KIND','KEWR','KAFW','KOAK','PANC','CYVR','CYEG','CYYC','CYWG','CYYZ','CYOW','CYMX','KCLE','KDAY','KLCK','KCVG','KHTS','KPIT','KBUF','KROC','KSYR','KALB','KBTV','KBGR','KPWM','KMHT','KBOS','KPVD','KBDL','KSWF','KJFK','KABE','KPHL','KMDT','KBWI','KIAD','KDCA','KRIC','KORF','KROA','KGSO','KRDU','KCLT','KGSP','KCAE','KCHS','KSAV','KATL','KCHA','KTYS','KBNA','KSDF','KHSV','KHSV','KHSV','KTLH','KJAX','KMCO','KTPA','KRSW','KPBI','KFLL','KMIA','KFAR','KFSD','KOMA','KMCI','KSGF','KSTL','KDSM','KCID','KRST','KMSP','KDLH','KATW','KMSN','KMKE','KORD','KBMI','KFWA','KSBN','KGRR','KFNT','KDTW','KGJT','KDEN','KCOS','KABQ','KELP','KLBB','KHRL','KLRD','KSAT','KAUS','KIAH','KDFW','KOKC','KTUL','KICT','KLIT','KSHV','KLFT','KMSY','KSEA','KGEG','KPDX','KBOI','KGTF','KBIL','KCPR','KTUS','KPHX','KSLC','KLAS','KRNO','KSMF','KSFO','KSJC','KFAT','KLAX','KBUR','KONT','KLGB','KSNA','KSAN']

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
        #print(time_stamp_reference)
        #print(each_array[2])
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

#print(running_mel_extractor_function())

print('')
print('Completed MEL Extractions from TAFs')
print('')


import xlwt 
from xlwt import Workbook 
  
# Workbook is created 
wb = Workbook() 

# add new colour to palette and set RGB colour value for "Surface Icing Types:"
xlwt.add_palette_colour("custom_colour1", 0x21)
wb.set_colour_RGB(0x21, 242, 242, 242)

# add new colour to palette and set RGB colour value for "sn = snow:"
xlwt.add_palette_colour("custom_colour2", 0x22)
wb.set_colour_RGB(0x22, 0, 176, 240)

# add new colour to palette and set RGB colour value for "pl=sleet:"
xlwt.add_palette_colour("custom_colour3", 0x23)
wb.set_colour_RGB(0x23, 0, 176, 80)

#
#hubs_list = mel_list[54:58]
#hubs_list_icao=station_ids[54:58]
#print(hubs_list,hubs_list_icao)
#
#print(mel_list)

# add_sheet is used to create sheet. 
sheet1 = wb.add_sheet('Sheet 1') 
#sheet1 = wb.add_sheet('Hubs') 
#sheet2 = wb.add_sheet('Canadian Stations') 
#sheet3 = wb.add_sheet('Northeast Stations') 
#sheet4 = wb.add_sheet('Southeast Stations') 
#sheet5 = wb.add_sheet('North Central Stations') 
#sheet6 = wb.add_sheet('South Central Stations') 
#sheet7 = wb.add_sheet('Northwest Stations') 
#sheet8 = wb.add_sheet('Southwest Stations') 


style=xlwt.easyxf('pattern: pattern solid, fore_colour white;' 'font: colour black, bold True, name Calibri, height 180; align: vert centre, horiz centre;border: left thin,right thin,top thin,bottom thin')

# writing title 
sheet1.write_merge(3, 3, 0, 17, 'Winter Weather Forecast', xlwt.easyxf('pattern: pattern solid, fore_colour white;' 'font: colour black, bold True, name Calibri, height 400; align: vert centre, horiz centre'))
sheet1.write_merge(4, 4, 0, 17, 'October 2, 2019 - 02Z', xlwt.easyxf('pattern: pattern solid, fore_colour white;' 'font: colour black, bold True, name Calibri, height 400;align: vert centre, horiz centre'))
sheet1.write_merge(0, 0, 0, 2, 'Surface Icing Types:',xlwt.easyxf('pattern: pattern solid, fore_colour custom_colour1;' 'font: colour black, bold True, name Calibri, height 220;align: vert centre, horiz centre;border: left thin,right thin,top thin,bottom thin'))
sheet1.write_merge(0, 0, 3, 4, 'sn=snow',xlwt.easyxf('pattern: pattern solid, fore_colour custom_colour2;' 'font: colour black, bold True, name Calibri, height 220;align: vert centre, horiz centre;border: left thin,right thin,top thin,bottom thin'))
sheet1.write_merge(0, 0, 5, 6, 'pl=sleet',xlwt.easyxf('pattern: pattern solid, fore_colour custom_colour3;' 'font: colour black, bold True, name Calibri, height 220;align: vert centre, horiz centre;border: left thin,right thin,top thin,bottom thin'))
sheet1.write_merge(0, 0, 7, 10, 'fz=freezing rain/drizzle',xlwt.easyxf('pattern: pattern solid, fore_colour red;' 'font: colour black, bold True, name Calibri, height 220;align: vert centre, horiz centre;border: left thin,right thin,top thin,bottom thin'))
sheet1.write_merge(0, 0, 11, 13, 'mix = mix of 2 or more',xlwt.easyxf('pattern: pattern solid, fore_colour yellow;' 'font: colour black, bold True, name Calibri, height 220;align: vert centre, horiz centre;border: left thin,right thin,top thin,bottom thin'))


whitestyle=xlwt.easyxf('font: colour black, bold True, name Calibri, height 180; align: vert centre, horiz centre;border: left thin,right thin,top thin,bottom thin')

snowstyle=xlwt.easyxf('pattern: pattern solid, fore_colour custom_colour2; font: colour black, bold True, name Calibri, height 180; align: vert centre, horiz centre;border: left thin,right thin,top thin,bottom thin')

mixstyle=xlwt.easyxf('pattern: pattern solid, fore_colour yellow; font: colour black, bold True, name Calibri, height 180; align: vert centre, horiz centre;border: left thin,right thin,top thin,bottom thin')

plstyle=xlwt.easyxf('pattern: pattern solid, fore_colour custom_colour3; font: colour black, bold True, name Calibri, height 180; align: vert centre, horiz centre;border: left thin,right thin,top thin,bottom thin')

fzstyle=xlwt.easyxf('pattern: pattern solid, fore_colour red; font: colour black, bold True, name Calibri, height 180; align: vert centre, horiz centre;border: left thin,right thin,top thin,bottom thin')

print('Completed Title Info on MEL Excel File')
print('')

#writing icao 

sheet1.write(6,0, "Station : ", style=style) 
#print(station_ids_extractor_function())
for row, data in enumerate(station_list):
    sheet1.write(7+row,0, data, style=style) 

# writing time 
row = 0
#print(time_range_function_3())
for col, data in enumerate(time_range_function_2()):
    sheet1.write(6+row, 1+col, data, style=style) 

print('Completed Time Setup for Winter Weather MEL Excel File')
print('')

# writing MEL data  
row = 1
#print(mel_list)
mel_list=running_mel_extractor_function()
for values in mel_list:
    #print(values)
    for col, data in enumerate(values):
        if data=='w': 
            sheet1.write(6+row, 1+col, data, snowstyle) 
        elif data=='NaN':
            sheet1.write(6+row, 1+col,'', whitestyle) 
        elif data=='n':
            sheet1.write(6+row, 1+col,'', whitestyle) 
        elif data=='sn':
            sheet1.write(6+row, 1+col,'sn', snowstyle) 
        elif data=='pl':
            sheet1.write(6+row, 1+col,'pl', plstyle) 
        elif data=='fz':
            sheet1.write(6+row, 1+col,'fz', fzstyle) 
        elif data=='m':
            sheet1.write(6+row, 1+col,'mix', mixstyle) 
        #    sheet1.write(6+row, 1+col, data, xlwt.easyxf('font: colour white, bold True, name Calibri, height 180; align: vert centre, horiz centre;border: left thin,right thin,top thin,bottom thin')) 

    row = row + 1 
  
wb.save('test2.xls') 

print('Completed Winter Weather MEL Excel File')
print('')
