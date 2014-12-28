class CUsersDao(object):
    '''

    '''
    def __init__(self):
        self.user='root'
        self.password='qqqq'
        self.db='workdb'
        self.cxn=None
        self.cur=None        
    def connect(self):
        import mysql.connector
        self.cxn=mysql.connector.connect(user=self.user,password=self.password,db=self.db)
        self.cur=self.cxn.cursor()
        return 0
    def close(self):
        self.cur.close()
        self.cxn.close()
        
    def modTable(self,openid):   
        import hashlib
        mod=int(hashlib.sha1(openid.encode()).hexdigest(), base=16)%2
        table='users_'+str(mod)
        return table
        
    def query(self,dWhere):
        strsql=None
        if 'openid' in dWhere:
            self.connect()
            table = self.modTable(dWhere['openid'])
            strsql='select openid, nickname, sex, subscribe, city, country, province, language, headimgurl, subscribe_time  from %s' % table
            strsql +=' where openid="%s"' % dWhere['openid']
            self.cur.execute(strsql)
            
            oneResult = self.cur.fetchone()
            if oneResult == None : return {}
            
            return {'openid' : oneResult[0], 'nickname' : oneResult[1],'sex' : oneResult[2], 'subscribe' : oneResult[3],
                    'city' : oneResult[4],'country' : oneResult[5],'province' : oneResult[6],'language' : oneResult[7],
                    'headimgurl' : oneResult[8],'subscribe_time' : oneResult[9]}
           
                
        
    def insert(self,dValue):
        strsql=None
        if 'openid' in dValue:
            self.connect()
            table = self.modTable(dValue['openid'])
            strsql='insert into %s set openid = "%s"' % (table , dValue['openid'])
            if 'subscribe' in dValue : strsql += ',subscribe = %d' % dValue['subscribe']
            if 'nickname' in dValue : strsql += ',nickname = "%s"' % dValue['nickname']
            if 'sex' in dValue : strsql += ',sex = %d' % dValue['sex']
            if 'city' in dValue : strsql += ',city = "%s"' % dValue['city']
            if 'country' in dValue : strsql += ',country = "%s"' % dValue['country']
            if 'province' in dValue : strsql += ',province = "%s"' % dValue['province']
            if 'language' in dValue : strsql += ',language = "%s"' % dValue['language']
            if 'headimgurl' in dValue : strsql += ',headimgurl = "%s"' % dValue['headimgurl']
            if 'subscribe_time' in dValue : strsql += ',subscribe_time = %d' % dValue['subscribe_time']
            self.cur.execute(strsql)   
            self.cxn.commit()
        return 0
    
    def update(self, dValue, dWhere) :
        strsql=None
        if 'openid' in dWhere:
            self.connect()
            table = self.modTable(dWhere['openid'])
            strsql='update %s set openid = "%s"' % (table , dWhere['openid'])
            if 'subscribe' in dValue : strsql += ',subscribe = %d' % dValue['subscribe']
            if 'nickname' in dValue : strsql += ',nickname = "%s"' % dValue['nickname']
            if 'sex' in dValue : strsql += ',sex = %d' % dValue['sex']
            if 'city' in dValue : strsql += ',city = "%s"' % dValue['city']
            if 'country' in dValue : strsql += ',country = "%s"' % dValue['country']
            if 'province' in dValue : strsql += ',province = "%s"' % dValue['province']
            if 'language' in dValue : strsql += ',language = "%s"' % dValue['language']
            if 'headimgurl' in dValue : strsql += ',headimgurl = "%s"' % dValue['headimgurl']
            if 'subscribe_time' in dValue : strsql += ',subscribe_time = %d' % dValue['subscribe_time']
            strsql += ' where openid = "%s"' % dWhere['openid']
            self.cur.execute(strsql)   
            self.cxn.commit()
        return 0        
    
    def delete(self, dWhere) :
        strsql=None
        if 'openid' in dWhere:
            self.connect()
            table = self.modTable(dWhere['openid'])
            strsql='delete from %s' % table
            strsql += ' where openid = "%s"' % dWhere['openid']
            self.cur.execute(strsql)   
            self.cxn.commit()
        return 0                
    
if __name__== '__main__':
    oUsersDao=CUsersDao()
    
    oUsersDao.insert({'openid' : 'bbbccwwwdd', 'nickname' : 'amjigo', 'sex' : 1, 'subscribe' : 1,
                    'city' : 'shenzhen','country' : 'china','province' : 'guangdong','language' : 'chinese',
                    'headimgurl' : 'ttttt', 'subscribe_time' : 3434545})
    #oUsersDao.update({'nickname' : 'amjigo11'}, {'openid' : 'aaaa'})
    #oUsersDao.delete({'openid' : 'aaaa'})
    print(oUsersDao.query({'openid':'bbbccwwwdd'}))