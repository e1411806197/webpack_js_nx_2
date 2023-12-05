import requests
import execjs
from datetime import datetime
account='12345535222@163.com'
password='5555555555'
with open('tyy.js','r',encoding='utf8') as f:
    content=f.read()
password_en=execjs.compile(content).call('get_password',account,password)
cookies = {
    'ct_tgc': '18f45727-ff35-41fa-9ad9-a2f45136318e',
    'Hm_lvt_4b4ce93f1c92033213556e55cb65769f': '1701763659',
    'Hm_lpvt_4b4ce93f1c92033213556e55cb65769f': '1701763659',
    'sid1': '1701763659413-51A80A86AEE69600EC9AA8A980438A29',
    'sid2': '1701763659413-51A80A86AEE69600EC9AA8A980438A29',
    'pvid': '1',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    # 'Cookie': 'ct_tgc=18f45727-ff35-41fa-9ad9-a2f45136318e; Hm_lvt_4b4ce93f1c92033213556e55cb65769f=1701763659; Hm_lpvt_4b4ce93f1c92033213556e55cb65769f=1701763659; sid1=1701763659413-51A80A86AEE69600EC9AA8A980438A29; sid2=1701763659413-51A80A86AEE69600EC9AA8A980438A29; pvid=1',
    'Origin': 'https://m.ctyun.cn',
    'Referer': 'https://m.ctyun.cn/wap/main/auth/login',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'x-riskdevicesign': '88d37dde76806c0f5e895ff07820c331',
}

params = {
    'referrer': 'wap',
    'mainVersion': '300031500',
    'comParam_curTime': str(int(datetime.now().timestamp()*1000)),
    # 'comParam_seqCode': 'C27554A3DDBB26C27CC68DB9183C2A2C',
    # 'comParam_signature': 'ab139f5afa65f48720946b1b751495a0',
    'isCheck': 'true',
    'locale': 'zh-cn',
}

data = {
    'userName': account,
    'password': password_en,
}

response = requests.post('https://m.ctyun.cn/account/login', params=params, cookies=cookies, headers=headers, data=data)
print(response.json())