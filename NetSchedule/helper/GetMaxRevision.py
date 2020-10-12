import time
import requests
from datetime import date

today = date.today()
d1 = today.strftime("%d-%m-%Y")

url = "https://wbes.wrldc.in/Report/GetCurrentDayFullScheduleMaxRev"
header = {
    'Host': 'wbes.wrldc.in',
    'Connection': 'keep-alive',
    'Accept': 'text/html, */*; q=0.01',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://wbes.wrldc.in/ReportNetSchedule/GetNetScheduleIndex',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7'
}
parameters = {
    'regionId': 2,
    'scheduleDate': d1,
}


def get_max_revision():
    response = requests.get(url, headers=header, params=parameters).json()
    return response['MaxRevision']


def get_max_revision_by_date(parameters_arg):
    response = requests.get('https://wbes.wrldc.in/ReportNetSchedule/GetNetScheduleRevisionNo', headers=header, params=parameters_arg).json()
    print(response)
    return max(response)


# too keep calling method
'''while True:
    getMaxRevision()
    time.sleep(5.0 - ((time.time() - startTime) % 5.0))'''

