#@project:  mitmproxyDemo
#@author: heyeping
#@file: Modify_ResponseCode.py
#@ide: PyCharm
#@time: 2022/2/16 11:39 AM

from mitmproxy import ctx, http
import json


class Modify:
    def response(self, flow):
        if flow.request.url.startswith("https://abp-test.ayla.com.cn/api/v1/build/a6/transfer/update1"):
            flow.response = http.HTTPResponse.make(500)
            ctx.log.info("modify status code")


addons = [
    Modify()
]
