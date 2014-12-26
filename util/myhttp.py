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
            
        oHttp = httplib2.Http(timeout=iTimeOut)
        
        dResp, strRespContent = oHttp.request(strUrl + strParams)
        if 'status' in dResp :
            dRet['iHttpCode'] = dResp['status']
        dRet['strContent'] = strRespContent
        dRet['iErrCode'] = 0
        return dRet 
    
    def post(self, strUrl, dParam = {}, strBody = '', dHeaders = {},  iTimeOut = 5) :
        '''
        入参：
        strUrl : 字符串
        dParam : 字典形式的参数，带在url后面的参数
        strBody : post 的 body 内容
        dHeaders : 请求头的信息
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
            dRet['strErrMsg'] = 'invalid strBody'
            return dRet            
        
        try:
            strParams = ('?' + urllib.parse.urlencode(dParam)) if (dParam != None and len(dParam) != 0) else ''; 
        except TypeError :
            dRet['iErrCode'] = -1
            dRet['strErrMsg'] = 'invalid dParam'
            return dRet        

        oHttp = httplib2.Http(timeout=iTimeOut)
        dResp, strRespContent = oHttp.request(strUrl + strParams, 'POST', headers=dHeaders, body=strBody)
        if 'status' in dResp :
            dRet['iHttpCode'] = dResp['status']
        dRet['strContent'] = strRespContent
        dRet['iErrCode'] = 0
        return dRet
    
def test() :
    dParams = {'grant_type' : 'client_credential', 'appid' : 'wx69e477e8ba33d2de', 'secret' : '68c99c5af77a32266461d2e8ab0374e7'}
    oHttp = MyHttp()
    #oRet = oHttp.get('https://api.weixin.qq.com/cgi-bin/token', dParams)
    #print(oRet)
    
    dParams = {'access_token' : 'ZQ_QZW3uHNrBc1R8TPGxdNxXozytD5S9cCQ0_qoBU2MHh0TbsIzese05OjgBP4yuC9U42JKSy-6feSVq3RswCEvyQSkrh9Vi-884WGaaTt4'}
    strBody = '{"touser":"oYvUpt5h0pNLFxuS8R8OwRNQob8o", "msgtype":"text", "text":{"content":"Hello World"}}'
    oRet = oHttp.post('http://api.weixin.qq.com/cgi-bin/message/custom/send', dParams, strBody)
    print(oRet)
    
    import sys
    print(sys.path)

if __name__ == '__main__' :
    test()