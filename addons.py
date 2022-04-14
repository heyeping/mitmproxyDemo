#@project:  mitmproxyDemo
#@author: heyeping
#@file: addons.py
#@ide: PyCharm
#@time: 2022/2/14 10:32 AM

import mitmproxy.http
from mitmproxy import ctx

class Counter:
    def __init__(self):
        self.num = 0

    def request(self, flow: mitmproxy.http.HTTPFlow):
        self.num = self.num + 1
        ctx.log.info("seen %d flows" % self.num)

addons = [
    Counter()
]