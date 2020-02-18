# -*- coding: utf-8 -*-
# @Time : 2020/2/15 0015 16:59
# @Author : 晓丶玉女
# @Blog : https://oltd.ltd
import time

import requests

cookie = 'CURRENT_FNVAL=16; _uuid=EA216AA6-9866-F036-1504-C69AA4B7EF8B95087infoc; buvid3=A29460CB-2B6E-4943-8482-B649EA262415155836infoc; stardustvideo=1; laboratory=1-1; LIVE_BUVID=AUTO8515764161006825; rpdid=|(J|lllluu)k0J\'ul~YRu~lRR; CURRENT_QUALITY=116; im_notify_type_5212665=0; dy_spec_agreed=1; sid=in9vzqaq; DedeUserID=5212665; DedeUserID__ckMd5=fe7ad1fbda4c47b1; SESSDATA=3eb3238d%2C1582960966%2C8eb37711; bili_jct=13042e90da41d8271fc35c3122dde50b; INTVER=1; bp_t_offset_5212665=356081131331970061; Hm_lvt_8a6e55dbd2870f0f5bc9194cddf32a02=1581748185,1581749276,1581749298,1581749315; Hm_lpvt_8a6e55dbd2870f0f5bc9194cddf32a02=1581749315'
headers = {
    'cookie': cookie,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}


def renew(card_record_id):
    url = f'https://api.live.bilibili.com/xlive/web-room/v1/userRenewCard/use?card_record_id={card_record_id}&title_id=title-299-1&num=1&t={CurrentTime()}'
    res = requests.get(url=url, headers=headers)
    json = res.json()
    data = json['data']
    if data['result'] == 1:
        print('续期成功，到期时间：%s' % data['title_expire_datetime'])


def check_bag():
    url = f'https://api.live.bilibili.com/xlive/web-room/v1/userRenewCard/get_with_title?title_id=title-296-1&t={CurrentTime()}'
    res = requests.get(url=url, headers=headers)
    json = res.json()
    data = json['data']['list']
    for i in data:
        i.pop("img_url")
        i.pop("expire_desc")
        print(i)


def check_num(card_record_id):
    url = f'https://api.live.bilibili.com/xlive/web-room/v1/userRenewCard/get_with_title?title_id=title-296-1&t={CurrentTime()}'
    res = requests.get(url=url, headers=headers)
    json = res.json()
    data = json['data']['list']
    for i in data:
        if card_record_id == i['card_record_id']:
            num = i['num']
            return num


def CurrentTime():
    currenttime = int(round(time.time() * 1000))
    return str(currenttime)


def renew_all(card_record_id):
    i = 0
    num = check_num(card_record_id)
    while True:
        renew(card_record_id)
        i += 1
        if i == num:
            break


check_bag()
renew_all(17479453)