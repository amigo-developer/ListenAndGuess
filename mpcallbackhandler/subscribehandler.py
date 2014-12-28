#coding=utf-8 
import time
from util.mylogger import CMyLogger
from users.UsersDao import CUsersDao

class CSubscribeHandler(object) :
    def handle(self, oXmlReader) :
        dUsersInfo = {}
        dUsersInfo['openid'] = oXmlReader.getValue('/xml/FromUserName')
        dUsersInfo['subscribe'] = 1
        
        oUsersDao = CUsersDao()
        strQueryRet=oUsersDao.query(dUsersInfo)
        if strQueryRet=={}:
            oUsersDao.insert(dUsersInfo)
        elif strQueryRet['subscribe']==0:
            oUsersDao.update(dUsersInfo, strQueryRet)
            
        return '此号已被wuyao拿来当测试号'