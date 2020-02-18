# -*- coding: utf-8 -*-
# @Time : 2020/2/11 0011 2:17
# @Author : 晓丶玉女
# @Blog : https://oltd.ltd
import requests
url = 'https://mall.bilibili.com/mall-c-search/items/info?itemsId=10019220&shopId&itemsVersion=&v=1581358709598'
cookie = 'CURRENT_FNVAL=16; _uuid=EA216AA6-9866-F036-1504-C69AA4B7EF8B95087infoc; buvid3=A29460CB-2B6E-4943-8482-B649EA262415155836infoc; stardustvideo=1; laboratory=1-1; LIVE_BUVID=AUTO8515764161006825; rpdid=|(J|lllluu)k0J\'ul~YRu~lRR; CURRENT_QUALITY=116; im_notify_type_5212665=0; dy_spec_agreed=1; sid=in9vzqaq; DedeUserID=5212665; DedeUserID__ckMd5=fe7ad1fbda4c47b1; SESSDATA=3eb3238d%2C1582960966%2C8eb37711; bili_jct=13042e90da41d8271fc35c3122dde50b; bp_t_offset_5212665=354357062737584798; INTVER=1; deviceFingerprint=c729ac86a80cb5c1be34045df982edda; Hm_lvt_8d8d2f308d6e6dffaf586bd024670861=1580039147,1580884883,1581352128,1581358151; kfcSource=bilibiliapp; msource=bilibiliapp; kfcFrom=cms_qrjwf; Hm_lpvt_8d8d2f308d6e6dffaf586bd024670861=1581358708'
headers = {
    'cookie': cookie,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}
res = requests.get(url=url, headers=headers)
json = res.json()
data = json['data']
item_detail = data['itemsDepositVO']
depositPrice = item_detail['depositPrice']
price = item_detail['price']
stock = item_detail['stock']
print(data['name'])
# print(item_detail)
print('定金：%s    价格：%s\t库存：%s' % (depositPrice, price, stock))
