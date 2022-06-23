import sqlite3
import requests
import json

for schoolid in range(1,3606):
    url = 'https://static-data.gaokao.cn/www/2.0/school/{}/info.json'.format(
            schoolid)
    headers = headers = {
                         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 SLBrowser/8.0.0.3161 SLBChan/25'}
    result = requests.get(url, headers=headers)
    info = json.loads(result.text)
    if info =='':
        pass
    else:
        provinceid = info['data']['province_id']
        schoolName = info['data']['name']
        print(schoolName,provinceid)