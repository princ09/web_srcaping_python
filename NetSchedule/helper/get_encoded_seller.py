import requests
import helper.DataProvider as dp

url = "https://wbes.wrldc.in/ReportNetSchedule/GetUtils?"
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
    'regionId': 2
}
response = requests.get(url, headers=header, params=parameters).json()


def get_encoded_seller_or_buyer(seller_pram, is_buyer):
    response_seller_or_buyer = []
    if is_buyer == 1:
        response_seller_or_buyer = response['sellers']
    if is_buyer == 0:
        response_seller_or_buyer = response['buyers']

    for seller in response_seller_or_buyer:
        if seller['Acronym'] == seller_pram:
            return seller['UtilId']


