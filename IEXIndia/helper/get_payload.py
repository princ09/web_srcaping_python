import requests
from bs4 import BeautifulSoup

url = "https://www.iexindia.com/marketdata/areaprice.aspx"
header = {
    'Host': 'www.iexindia.com',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Origin': 'https://www.iexindia.com',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://www.iexindia.com/marketdata/areaprice.aspx',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
    'X-Requested-With': 'XMLHttpRequest',

}

payload = {
        '__EVENTTARGET': '',
        '__EVENTARGUMENT': '',
        '__LASTFOCUS': '',
        '__VIEWSTATE': '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',
        '__VIEWSTATEGENERATOR': 'CF6E9D8D',
        '__VIEWSTATEENCRYPTED': '',
        '__EVENTVALIDATION': '60lI0y/FI3523MZJSHrRCWK8vPvta24kwTN7EtZ3Ykp23OOFt7j0qA3d7NROvWpBgE/oshg7aMeDl/UqflbAgZiPbqMuxJaNJ06JIuFHbPfWnzpkNOdVoaj2b7Z8e21Im6RaHx5MNDwXCQ5JNESPbXpDSVDAmmN9hmMkvGuesK8aHyjQtJnp2kvQuqDOf9bBoj2/RCyeqP0xQbwU3kTrbF5yTPgceXsRcJ4U+1USoLDsApqipIzEsxJ0ibNem52VEGT/GwC5xMpZT1IE5Xb2yyggmhnH+TzWiH41vaLGKr8RWx0WrsitiTHVHydPxv5Kxd9H/ULRdvv2QqIjXdBJFAoizWpFdegnOL0nDlB2M7bJKqM27CQnOzjexV8OKofzB+rAUGV6sOOvfozOyFrYV4ETnHVAIX88dC2HUsmwjowOgtT/f/6FH1YWXysNwo+G5CgfLTJmL0Yn0UeubZ4xZ8hW4MPsj+JgxuqZML5c/FmFTW88FevIot2q0knY6Gv6LF0VhRiGtV3ggs7LoEYbSml8oWMbetOSdbaQufTCOzVXlAElm9JG8bDbR45z5cKgn/9XJzbyhjlAJCX61VuOBuN5pqwBsubUDIebc3HdoDT9CGJkMxOlcLvYso/FHnnW809SWJY/NUOTDbUHUH0IFSmiUVEtfg4PBNfw98MtkhvvpSto8fT+jo1UUOQzv9rMrNWmWnqGFapmLaEpoGVQ1hQDnD/XUNyrVPb1gpsNhjShJXOgzj/dyWW5/nVLXMUzUN7RPZn1/KmvRvbWIc1Yd4ShlZ9KIKsNYpydfwgHsS0m+drb5Y3LwpeSWXCgXF6OTN7uB5mMKJwiHI8itUAkGKPC6K7I7x+TakDJoucke3j81tX80ioZVsgjrzgWzB6YFlQjhvx4uv4VXEIV5LeGC5hY8QctXNLoyyO52L74hV3COoP5gzrx7rxya2hcXsCWWUwDmRWnTeDj14Q4nXO97UFtuiaqyGu8ieFQrwWB+W+m72xOdJ2LWDZKadH1Q3Qtl2K50sEuM6wMIFYYVpm3mVWjAdWNBhOT+KOyFhCXFokbXOBXJkBq5NB8yK7Y7ykKyD+oCERv/EAMuVTRH8GmCBlWr7p11Wjs+aWKvamBL7tUFkz1F/SfagfddOzUdFKkrQrS1aEyL95fqVNgios0Lm/QxCkVJgeSoO8VWNkZq9FgiJmpp645zSQGY5KupquQ',
        'ctl00$InnerContent$ddlInterval': 1,
        'ctl00$InnerContent$ddlPeriod': 'SR',
        'ctl00$InnerContent$calFromDate$txt_Date': from_date,
        'ctl00$InnerContent$calToDate$txt_Date': to_date,
        'ctl00$InnerContent$cbArea': 'on',
        'ctl00$InnerContent$cblArealist$0': 'on',
        'ctl00$InnerContent$cblArealist$2': 'on',
        'ctl00$InnerContent$cblArealist$4': 'on',
        'ctl00$InnerContent$cblArealist$6': 'on',
        'ctl00$InnerContent$cblArealist$8': 'on',
        'ctl00$InnerContent$cblArealist$10': 'on',
        'ctl00$InnerContent$cblArealist$12': 'on',
        'ctl00$InnerContent$cblArealist$1': 'on',
        'ctl00$InnerContent$cblArealist$3': 'on',
        'ctl00$InnerContent$cblArealist$5': 'on',
        'ctl00$InnerContent$cblArealist$7': 'on',
        'ctl00$InnerContent$cblArealist$9': 'on',
        'ctl00$InnerContent$cblArealist$11': 'on',
        'ctl00$InnerContent$cblArealist$13': 'on',
        'ctl00$InnerContent$btnUpdateReport': 'Update Report',
        'ctl00$InnerContent$reportViewer$ctl03$ctl00': '',
        'ctl00$InnerContent$reportViewer$ctl03$ctl01': '',
        'ctl00$InnerContent$reportViewer$ctl10': 'ltr',
        'ctl00$InnerContent$reportViewer$ctl11': 'standards',
        'ctl00$InnerContent$reportViewer$AsyncWait$HiddenCancelField': 'False',
        'ctl00$InnerContent$reportViewer$ToggleParam$store': '',
        'ctl00$InnerContent$reportViewer$ToggleParam$collapse': 'false',
        'ctl00$InnerContent$reportViewer$ctl08$ClientClickedId': '',
        'ctl00$InnerContent$reportViewer$ctl07$store': '',
        'ctl00$InnerContent$reportViewer$ctl07$collapse': 'false',
        'ctl00$InnerContent$reportViewer$ctl09$VisibilityState$ctl00': 'Error',
        'ctl00$InnerContent$reportViewer$ctl09$ScrollPosition': '',
        'ctl00$InnerContent$reportViewer$ctl09$ReportControl$ctl02': '',
        'ctl00$InnerContent$reportViewer$ctl09$ReportControl$ctl03': '',
        'ctl00$InnerContent$reportViewer$ctl09$ReportControl$ctl04': '100'
    }
def get_payload():
    pass

def get_header():
    response = requests.get(url, headers=header)
    print(response.headers)
    cookie = {'Cookie': response.headers['Set-Cookie']}
    header.update(cookie)
    return header
