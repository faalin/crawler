#coding:utf-8
import time
import os
import stomp
from crawler_head.settings import STOMP
from crawler_head.spiders.crawler_model import Modelzhua

class MyListener(object):
    def on_error(self, headers, message):
        print('received an error %s' % message)

    def on_message(self, headers, message):
        startspider = Modelzhua(message)
        command = startspider.startspider()
        os.system(command)
def main():
    while True:
        try:
            print u'监听成功'
            conn = stomp.Connection10([(STOMP,61613)])
            conn.set_listener('', MyListener())
            conn.start()
            conn.connect(wait=True)
            conn.subscribe(destination='/queue/Python', ack='auto')
            time.sleep(60)
            conn.disconnect()
        except Exception,e:
            raise e

if __name__ == '__main__':
    main()
