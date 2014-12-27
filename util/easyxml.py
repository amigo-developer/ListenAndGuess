#coding=utf-8 

import xml.etree.ElementTree as xml

class CXmlReader(object) :
    def __init__(self, strXml) :
        self.oRoot = xml.fromstring(strXml)
        
    def getValue(self, strPath) :
        if len(strPath) == 0 : return None
        
        iSecondSlashIndex = strPath.find('/', 1)
        strPath = '' if iSecondSlashIndex == -1 else strPath[iSecondSlashIndex:]
        
        oElementFinded = self.oRoot.find('.' + strPath)
        return None if oElementFinded == None else oElementFinded.text
    
    def getValueList(self, strPath) :
        if len(strPath) == 0 : return None
        
        iSecondSlashIndex = strPath.find('/', 1)
        strPath = '' if iSecondSlashIndex == -1 else strPath[iSecondSlashIndex:]        
                
        lElementFinded = self.oRoot.findall('.' + strPath)
        if len(lElementFinded) == 0 : return []
        
        lValueFinded = []
        for ele in lElementFinded :
            lValueFinded.append(ele.text)
        return lValueFinded
    
if __name__ == '__main__' :
    strXml = '''<xml><ToUserName><![CDATA[gh_b14fcf45bd7a]]></ToUserName>
<FromUserName><![CDATA[oE1D7jrsdhHJ3U2s4iM1wYuK7O1c]]></FromUserName>
<CreateTime>1419660634</CreateTime>
<MsgType><![CDATA[text]]></MsgType>
<Content><![CDATA[魔域]]></Content>
<MsgId>6097395994651640760</MsgId>
</xml>
    '''
    strXmlList = '''<xml><users><openid>a</openid><openid>b</openid></users></xml>'''
    
    oXmlReader = CXmlReader(strXml)
    #print(oXmlReader.getValue('/xml/FromUserName'))
    #print(oXmlReader.getValue('/xml/Content'))
    #print(oXmlReader.getValue('/xml'))
    
    oXmlReaderList = CXmlReader(strXmlList)
    print(oXmlReaderList.getValueList('/xml/users1/'))
    