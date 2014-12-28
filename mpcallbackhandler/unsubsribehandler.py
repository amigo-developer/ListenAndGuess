#coding=utf-8 
import time
from util.mylogger import CMyLogger
from users.UsersDao import CUsersDao

class CUnsubscribeHandler(object) :
    def handle(self, oXmlReader) :
        CMyLogger.debug('unsubsribe-msg:00000') 
        dUsersInfo = {}
        dUsersInfo['openid'] = oXmlReader.getValue('/xml/FromUserName')
        dUsersInfo['subscribe'] = 0
        
        oUsersDao = CUsersDao()
        strQueryRet=oUsersDao.query(dUsersInfo)
        if strQueryRet['subscribe']==1:
            oUsersDao.update(dUsersInfo, strQueryRet)
           