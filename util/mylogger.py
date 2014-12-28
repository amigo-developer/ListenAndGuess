import logging
import logging.handlers
import sys
import os
 
class CMyLogger(object) :
    strLogPath = os.environ['PYTHONPATH'] + '/log/data.log'
    
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    handler = logging.handlers.RotatingFileHandler(strLogPath, maxBytes=20*1024*1024, backupCount=10)
    handler.setFormatter(logging.Formatter("%(asctime)s (%(process)d,%(thread)d) FILE:%(filename)s LN:%(lineno)d FUN:%(funcName)s %(message)s"))
    logger.addHandler(handler)
    
    @classmethod    
    def debug(cls, str) :
        cls.logger.debug(str)
    
    @classmethod    
    def info(cls, str) :
        cls.logger.info(str)
        
    @classmethod
    def warn(cls, str) :
        cls.logger.warn(str)

    @classmethod        
    def error(cls, str) :
        cls.logger.error(str)

    @classmethod        
    def critical(cls, str) :
        cls.logger.critical(str)        
        
        
def test() :
    CMyLogger.debug('wuyao')
    print(sys.path)
        
if __name__ == '__main__' :
    test()