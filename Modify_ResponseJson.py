#@project:  mitmproxyDemo
#@author: heyeping
#@file: Modify_ResponseJson.py
#@ide: PyCharm
#@time: 2022/2/16 2:13 PM

"""
修改响应的消息体-通过读取json文件的字符串返回给客户端
"""

from mitmproxy import ctx, http
import json


class Modify:
    def response(self, flow):
        if flow.request.url.startswith("https://abp-test.ayla.com.cn/api/v3/build/device/getDeviceActionOrCondition"):
            #读取文件，在当前文件路径下执行脚本，否则需要写文件的绝对路径；不然会找不到该json文件
            with open('/Users/heyeping/Documents/testProject/mitmproxyDemo/ActionCondition.json', 'rb') as f:
                #从json文件中读取数据成python对象
                res = json.load(f)

            #将读取的python对象转成json字符串发送给客户端
            flow.response.set_text(json.dumps(res))
            ctx.log.info("modify order status")

addons = [
    Modify()
]
