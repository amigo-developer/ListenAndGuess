#coding=utf-8 

import cgi
import cgitb
import sys
import os
import locale
import time
import urllib.parse
from util.easyxml import CXmlReader
from users.UsersDao import CUsersDao
from util.mylogger import CMyLogger
from mpcallbackhandler.subscribehandler import CSubscribeHandler
from mpcallbackhandler.unsubscribehandler import CUnsubscribeHandler

cgitb.enable(display=0, logdir=os.environ['PYTHONPATH'] + '\log')

class CCgiInput(object) :
    def __init__(self) :
        self.lParam = {}
        self.strBody = ''
        self.method = 'GET'
        
        if 'REQUEST_METHOD' in os.environ:
            self.method = os.environ['REQUEST_METHOD'].upper()        
            
        qs = ''
        if self.method == 'GET' or self.method == 'HEAD':
            if 'QUERY_STRING' in os.environ:
                qs = os.environ['QUERY_STRING']
            elif sys.argv[1:]:
                qs = sys.argv[1] 
        else :
            self.strBody =  sys.stdin.buffer.read()
            self.strBody = self.strBody.decode('utf-8')
                
        query = urllib.parse.parse_qsl(
            qs, keep_blank_values=True, strict_parsing=False,
            encoding='utf-8', errors='replace')     
        for key, value in query:
            self.lParam[key] = value    
            
    def getValue(self, key) :
        if key in self.lParam:
            return self.lParam[key]
        else :
            return None
    
    def getBodyData(self) :
        return self.strBody

class CCgiOutput(object) :
    @classmethod
    def output(cls, str) :
        print('Content-type: text/html; charset=UTF-8\r\n')
        print(str)        
        
def main() :    
    oInput = CCgiInput()
    strEcho = oInput.getValue('echostr')
    if strEcho != None :
        CCgiOutput.output(strEcho)
    else :
        strPostData = oInput.getBodyData()
        if len(strPostData) == 0 : return 0
        CMyLogger.debug(strPostData)
        
        oXmlReader = CXmlReader(strPostData)
        strMsgTpye = oXmlReader.getValue('/xml/MsgType')
        if strMsgTpye == 'event' :
            strMsgTpye = oXmlReader.getValue('/xml/Event')
            
        dEventHandler = {}
        dEventHandler['subscribe'] = CSubscribeHandler()
        dEventHandler['unsubscribe'] = CUnsubscribeHandler()
        #dEventHandler['text'] = CSubscribeHandler()
        
        CMyLogger.debug('msgtype:%s %s' % (strMsgTpye, str(dEventHandler)))
        if strMsgTpye in dEventHandler :
            strRetMsg = dEventHandler[strMsgTpye].handle(oXmlReader)
            
            strFromId = oXmlReader.getValue('/xml/FromUserName')
            strToId = oXmlReader.getValue('/xml/ToUserName')
            strRet = '''<xml>
                    <ToUserName><![CDATA[%s]]></ToUserName>
                    <FromUserName><![CDATA[%s]]></FromUserName>
                    <CreateTime>%d</CreateTime>
                    <MsgType><![CDATA[text]]></MsgType>
                    <Content><![CDATA[%s]]></Content>
                    </xml>''' % (strFromId, strToId, int(time.time()), strRetMsg)                
            CCgiOutput.output(strRet)
            
       
 

if __name__ == '__main__' :
    main()
        
        