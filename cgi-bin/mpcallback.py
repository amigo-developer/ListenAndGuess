import cgi
import cgitb
import sys
import os
import locale
import urllib.parse
from util.easyxml import CXmlReader
from users.UsersDao import CUsersDao

cgitb.enable(display=1, logdir='e:\svn\python\log')

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
        print('Content-type: text/html \n')
        print(str)        

if __name__ == '__main__' :
    oInput = CCgiInput()
    strEcho = oInput.getValue('echostr')
    if strEcho != None :
        CCgiOutput.output(strEcho)
    else :
        strPostData = oInput.getBodyData()
        oXmlReader = CXmlReader(strPostData)
        strMsgTpye = oXmlReader.getValue('/xml/MsgType')
        
        strEventType = None
        if strMsgTpye == 'event' :
            strEventType = oXmlReader.getValue('/xml/Event')
            
        if strEventType == 'subscribe' :
            dUsersInfo = {}
            dUsersInfo['openid'] = oXmlReader.getValue('/xml/FromUserName')
            dUsersInfo['subscribe'] = 1
            
            oUsersDao = CUsersDao()
            oUsersDao.insert(dUsersInfo)
        
        