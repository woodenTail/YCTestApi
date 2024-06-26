# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author:   wsj QQ：3512937625
# @Time:   2021-07-04
# @Copyright：

import logging.handlers
from apiframework.setting import DIR_NAME

class GetLogger:
    '''
        当已经创建了logger对象的时候，那么之后就不在创建了，也就是只创建一次对象
        '''
    # 把logger对象的初始值设置为None
    logger = None

    # 创建logger，并且返回这个logger
    #@classmethod,用来指定一个类的方法为类方法,cls通常用作类方法的第一参数  跟self有点类似（ __init__里面的slef通常用作实例方法的第一参数)。即通常用self来传递当前类对象的实例，cls传递当前类对象
    @classmethod
    def get_logger(cls):
        if cls.logger is None:
            cls.logger=logging.getLogger('apiautotest')
            #设置总的级别，debug/info/warning/error
            #只有比debug级别高的日志才会被显示出来
            cls.logger.setLevel(logging.DEBUG)
            # 2获取格式器
            # 2.1 要给格式器设置要输出的样式
            fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d] - %(message)s"
            # 2.2创建格式器，并且给他设置样式
            fm = logging.Formatter(fmt)
            # 3.创建处理器 按照时间进行切割文件
            tf = logging.handlers.TimedRotatingFileHandler(filename=DIR_NAME + '/logs/requests.log',  # 原日志文件
                                                           when='H',  # 间隔多长时间把日志存放到新的文件中
                                                           interval=1,
                                                           backupCount=3,  # 除了原日志文件，还有3个备份
                                                           encoding='utf-8'
                                                           )
            logging.basicConfig(level=logging.DEBUG, format=fmt)  # 这是在控制台上打印日志信息

            # 在处理器中添加格式器
            tf.setFormatter(fm)
            # 在日志器中添加处理器
            cls.logger.addHandler(tf)

            # return cls.logger
        return cls.logger
if __name__ == '__main__':
    logger=GetLogger().get_logger()
    print(id(logger))
    logger1=GetLogger().get_logger()
    print(logger1)
    logger.debug('调试')  # 相当print小括号中的信息
    logger.info('信息')
    logger.warning('警告')
    name = 'yaoyao'
    logger.error('这个变量是{}'.format(name))
    logger.critical('致命的')