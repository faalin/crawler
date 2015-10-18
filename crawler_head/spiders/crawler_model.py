#coding:utf-8
class Modelzhua(object):

    def __init__(self,message):
        self.message = message

    def startspider(self):
        json_data = json.loads(self.message)
        command = json_data['command']
        return command

    def messagedata():
        def fget(self):
            return self.message
        def fset(self):
            self.messagedata = message
        return locals()
    messagedata = property(**messagedata())