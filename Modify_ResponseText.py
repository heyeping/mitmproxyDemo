#@project:  mitmproxyDemo
#@author: heyeping
#@file: Modify_ResponseText.py
#@ide: PyCharm
#@time: 2022/2/16 1:51 PM

"""
修改响应的消息体-直接修改响应字段
"""

from mitmproxy import ctx, http
import json


class Modify:
    def response(self, flow):
        if flow.request.url.startswith("https://abp-test.ayla.com.cn/api/v3/build/device/getDeviceActionOrCondition"):
            #获取响应的json字符串，转成python对象进行解析和修改
            response = json.loads(flow.response.get_text())
            response['nickName'] = "hyp"
            #修改完成后，奖python对象转成json字符串，set进请求的响应体重发送给客户端
            flow.response.set_text(json.dumps(response))
            ctx.log.info('modify nickName')

addons = [
    Modify()
]
