from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

station_list=['KMEM','KIND','KEWR','KAFW','KOAK','PANC','CYVR','CYEG','CYYC','CYWG','CYYZ','CYOW','CYMX','KCLE','KDAY','KLCK','KCVG','KHTS','KPIT','KBUF','KROC','KSYR','KALB','KBTV','KBGR','KPWM','KMHT','KBOS','KPVD','KBDL','KSWF','KJFK','KABE','KPHL','KMDT','KBWI','KIAD','KDCA','KRIC','KORF','KROA','KGSO','KRDU','KCLT','KGSP','KCAE','KCHS','KSAV','KATL','KCHA','KTYS','KBNA','KSDF','KHSV','KBHM','KBHM','KTLH','KJAX','KMCO','KTPA','KRSW','KPBI','KFLL','KMIA','KFAR','KFSD','KOMA','KMCI','KSGF','KSTL','KDSM','KCID','KRST','KMSP','KDLH','KATW','KMSN','KMKE','KORD','KBMI','KFWA','KSBN','KGRR','KFNT','KDTW','KGJT','KDEN','KCOS','KABQ','KELP','KLBB','KHRL','KLRD','KSAT','KAUS','KIAH','KDFW','KOKC','KTUL','KICT','KLIT','KSHV','KLFT','KMSY','KSEA','KGEG','KPDX','KBOI','KGTF','KBIL','KCPR','KTUS','KPHX','KSLC','KLAS','KRNO','KSMF','KSFO','KSJC','KFAT','KLAX','KBUR','KONT','KLGB','KSNA','KSAN']

def remove_html_tags(text):
    """Remove html tags from a string"""
    import re
    clean = re.compile('<.*?>')
    return(re.sub(clean, '', text))

def pull_program(value):

    quote_page = 'https://www.aviationweather.gov/adds/dataserver_current/httpparam?datasource=tafs&requestType=retrieve&format=xml&mostRecentForEachStation=true&hoursBeforeNow=2&stationString=' + value
    html = urlopen(quote_page)
    soup = BeautifulSoup(html,"html.parser")
    text = str(soup.find_all('raw_text'))
    cleantext=remove_html_tags(text) 
    cleantext=cleantext.replace('[', '')
    cleantext=cleantext.replace(']', '')
    cleantext=cleantext + ' ='
    #print(type(cleantext))
    #print(cleantext)
    return(cleantext)

def time_issued_pull_program(value):

    quote_page = 'https://www.aviationweather.gov/adds/dataserver_current/httpparam?datasource=tafs&requestType=retrieve&format=xml&mostRecentForEachStation=true&hoursBeforeNow=2&stationString=' + value
    html = urlopen(quote_page)
    soup = BeautifulSoup(html,"html.parser")
    text = str(soup.find_all('issue_time'))
    cleantext=remove_html_tags(text) 
    cleantext=re.split(",",cleantext)
    return(cleantext)

def time_range_pull_program_1(value):

    quote_page = 'https://www.aviationweather.gov/adds/dataserver_current/httpparam?datasource=tafs&requestType=retrieve&format=xml&mostRecentForEachStation=true&hoursBeforeNow=2&stationString=' + value
    html = urlopen(quote_page)
    soup = BeautifulSoup(html,"html.parser")
    text = str(soup.find_all('fcst_time_from'))
    fcst_time_from=remove_html_tags(text) 
    fcst_time_from=fcst_time_from.replace('[', '')
    fcst_time_from=fcst_time_from.replace(']', '')
    fcst_time_from=re.split(',',fcst_time_from)
 
    return(fcst_time_from)

def time_range_pull_program_2(value):

    quote_page = 'https://www.aviationweather.gov/adds/dataserver_current/httpparam?datasource=tafs&requestType=retrieve&format=xml&mostRecentForEachStation=true&hoursBeforeNow=2&stationString=' + value
    html = urlopen(quote_page)
    soup = BeautifulSoup(html,"html.parser")
    text = str(soup.find_all('fcst_time_to'))
    fcst_time_to=remove_html_tags(text) 
    fcst_time_to=fcst_time_to.replace('[', '')
    fcst_time_to=fcst_time_to.replace(']', '')
    fcst_time_to=re.split(',',fcst_time_to)

    return(fcst_time_to)

def time_range_pull_program_3(value):

    quote_page = 'https://www.aviationweather.gov/adds/dataserver_current/httpparam?datasource=tafs&requestType=retrieve&format=xml&mostRecentForEachStation=true&hoursBeforeNow=2&stationString=' + value
    html = urlopen(quote_page)
    soup = BeautifulSoup(html,"html.parser")
    text = str(soup.find_all('valid_time_from'))
    valid_time_from=remove_html_tags(text) 
    valid_time_from=valid_time_from.replace('[', '')
    valid_time_from=valid_time_from.replace(']', '')
    text = str(soup.find_all('valid_time_to'))
    valid_time_to=remove_html_tags(text) 
    valid_time_to=valid_time_to.replace('[', '')
    valid_time_to=valid_time_to.replace(']', '')
    return(valid_time_from,valid_time_to)

def get_taf_function():
    val = []
    for value in station_list:
        val.append(pull_program(value))
    return(val)

#print(get_taf_function())

def get_time_function_1():
    val = []
    for value in station_list:
        val.append(time_range_pull_program_1(value))
    return(val)

def get_time_function_2():
    val = []
    for value in station_list:
        val.append(time_range_pull_program_2(value))
    return(val)

def get_time_function_3():
    val = []
    for value in station_list:
        val.append(time_range_pull_program_3(value))
    return(val)
