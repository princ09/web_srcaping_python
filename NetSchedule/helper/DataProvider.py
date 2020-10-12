from datetime import date
import helper.GetMaxRevision as get_max_revision
import helper.get_encoded_seller as encoded_seller

today = date.today()
d1 = today.strftime("%d-%m-%Y")


def get_header():
    return {
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


def get_get_max_revision_params():
    return {
        'regionId': 2,
        'scheduleDate': d1,
    }


def get_schedule_params(seller_or_buyer, date_pass, region, is_buyer):
    region_id = get_region_id(region)
    max_revision = 0;
    if date_pass == d1:
        max_revision=get_max_revision.get_max_revision()
    else:
        max_revision = get_max_revision.get_max_revision_by_date({'scheduleDate': date_pass, 'regionId': region_id})
        print(max_revision)
    print(encoded_seller.get_encoded_seller_or_buyer(seller_or_buyer, is_buyer))
    parameters = {
        'regionId': region_id,
        'scheduleDate': date_pass,
        'sellerId': encoded_seller.get_encoded_seller_or_buyer(seller_or_buyer, is_buyer),
        'revisionNumber': max_revision,
        'byDetails': 0,
        'isBuyer': is_buyer
    }
    return parameters


def get_region_id(region):
    region_dict = {
        "EAST": 1,
        "WEST": 2,
        "NORTH": 3,
        "SOUTH": 4,
        "NORTH EAST": 5,
        "NLDC": 6
    }
    return region_dict[region]


def get_seller_header():
    return {
        'Host': 'wbes.wrldc. in',
        'Connection': 'keep - alive',
        'Cache - Control': 'max - age = 0',
        'Upgrade - Insecure - Requests': 1,
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
        'Accept': 'text/html, */*; q=0.01',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://wbes.wrldc.in/ReportNetSchedule/GetNetScheduleIndex',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7'

    }
