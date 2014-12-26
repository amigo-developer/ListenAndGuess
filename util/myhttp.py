#-*- coding:utf-8 -*-

import httplib2
import urllib.parse

class MyHttp(object) :
    def get(self, strUrl, dParam = {}, iTimeOut = 5) :
        '''
        入参：
        strUrl : 字符串
        dParam : 字典形式的参数，带在url后面的参数
        iTimeOut : 超时时间
        返回：
        iErrCode : 错误码，0表示正常，非0异常
        strErrMsg : 错误信息，errCode 非0有值 
        iHttpCode : http的返回码
        strContent : http的返回内容
        '''
        dRet = {'iErrCode' : -1, 'strErrMsg' : '', 'iHttpCode' : -1, 'strContent' : '' }
        
        if len(strUrl) == 0 :        
            dRet['iErrCode'] = -1
            dRet['strErrMsg'] = 'invalid strUrl'
            return dRet            
        
        try:
            strParams = ('?' + urllib.parse.urlencode(dParam)) if (dParam != None and len(dParam) != 0) else ''; 
        except TypeError :
            dRet['iErrCode'] = -1
            dRet['strErrMsg'] = 'invalid dParam'
            return dRet
            
        oHttp = httplib2.Http(timeout=iTimeOut, disable_ssl_certificate_validation=False if strUrl.find('https') != -1 else True)
        
        dRespHeaders, strRespContent = oHttp.request(strUrl + strParams)
        if 'status' in dRespHeaders :
            dRet['iHttpCode'] = dRespHeaders['status']
        dRet['strContent'] = strRespContent
        dRet['iErrCode'] = 0
        return dRet 
    
    def post(self, strUrl, dParam = {}, strBody = '', dHeaders = {}, iIsEncode = True,  iTimeOut = 5) :
        '''
        入参：
        strUrl : 字符串
        dParam : 字典形式的参数，带在url后面的参数
        iTimeOut : 超时时间
        返回：
        iErrCode : 错误码，0表示正常，非0异常
        strErrMsg : 错误信息，errCode 非0有值 
        iHttpCode : http的返回码
        strContent : http的返回内容
        '''        
        dRet = {'iErrCode' : -1, 'strErrMsg' : '', 'iHttpCode' : -1, 'strContent' : '' }
                
        if len(strUrl) == 0 :        
            dRet['iErrCode'] = -1
            dRet['strErrMsg'] = 'invalid strUrl'
            return dRet
        
        if len(strBody) == 0 :
            dRet['iErrCode'] = -1
            dRet['strErrMsg'] = 'invalid strUrl'
            return dRet            
        
        try:
            strParams = ('?' + urllib.parse.urlencode(dParam)) if (dParam != None and len(dParam) != 0) else ''; 
        except TypeError :
            dRet['iErrCode'] = -1
            dRet['strErrMsg'] = 'invalid dParam'
            return dRet        

        oHttp = httplib2.Http()
        response, content = oHttp.request(strUrl + strParams, 'POST', headers=lHeaders, body=strBody)
            
        pass
    
def test() :
    dParams = {'grant_type' : 'client_credential', 'appid' : 'wx69e477e8ba33d2de', 'secret' : '68c99c5af77a32266461d2e8ab0374e7'}
    oHttp = MyHttp()
    oRet = oHttp.get('https://api.weixin.qq.com/cgi-bin/token', dParams)
    print(oRet)

if __name__ == '__main__' :
    test()