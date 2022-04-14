#@project:  mitmproxyDemo
#@author: heyeping
#@file: Modify_RequestDate.py
#@ide: PyCharm
#@time: 2022/2/16 11:30 AM

"""
修改请求参数
"""

from mitmproxy import ctx, http
import json

class Modify:
    def request(self, flow):
        if flow.request.url.startswith("https://xxx.com.cn"):
            ctx.log.info("modify request from")
            if flow.request.urlencoded_form:
                flow.request.urlencoded_form["code"] = "111111"
            else:
                flow.request.urlencoded_form = [
                    ("a", '111'),("b", "222")
                ]

addnos = [
    Modify()
]