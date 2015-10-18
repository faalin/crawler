# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import setting
import MySQLdb
import MySQLdb.cursors
from datetime import datetime
from spiders.crawler_model import Modelzhua

data_from = Modelzhua.messagedata
data = json.loads(data_from)
demo = str(data['datas'])
datas = json.loads(demo)
table_name = str(data['tablename'])



class MySQLStorePipeline(object):

    def __init__(self):
        try:
            self.conn= MySQLdb.connect(user=setting.MYSQL_NAME, passwd=setting.MYSQL_PASSWD, host=setting.MYSQL_HOST, db=setting.MYSQL_DB, use_unicode=True, charset='utf8')
            # self.conn= MySQLdb.connect(user='test_lottery', passwd='9Pnc7BeJ', host='182.92.191.193', db='db_lottery', use_unicode=True, charset='utf8')
            self.cursor = self.conn.cursor()
            self.conn.commit()
        except (AttributeError, MySQLdb.OperationalError), e:
            raise e

    def __del__(self):
        print 100*'*'
        self.conn.close()

    def process_item(self, item, spider):
        now = datetime.now().replace(microsecond=0).isoformat(' ')
        data_insert = str(tuple(str(data['name']) for data in datas)).replace("'","")
        data_item = list(item[str(data['name'])] for data in datas)
        data_set = list(str(data['name']) for data in datas)
        placeholder_update = []
        for data in data_set:
            placeholder_update.append(data+'='+'%s')
        primary_key = placeholder_update[-1]
        key_item = str(placeholder_update[0:-1]).replace("'","").replace("[","").replace("]","")

        if item.get(datas[0]['name']):
            self.cursor.execute("select * from "+table_name+" where "+primary_key,str(data_item[-1]))
            ret = self.cursor.fetchone()
            if ret:
                self.cursor.execute("update "+table_name+" set "+str(key_item)+" where "+primary_key,data_item)
                self.cursor.execute("update "+table_name+" set update_time=%s where "+primary_key,(now,str(data_item[-1])))
                self.conn.commit()
            else:
                placeholder_insert = []
                for i in range(len(data_item)):
                    placeholder_insert.append('%s')
                holder = str(tuple(placeholder_insert)).replace("'","")
                self.cursor.execute("insert into "+table_name+" "+str(data_insert)+"values"+holder,data_item)
                self.conn.commit()
            return item