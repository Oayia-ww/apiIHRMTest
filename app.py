"""
编写初始化日志函数   类似于postman的全局变量
"""
import logging
import os
from logging import handlers

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HOST = 'http://182.92.81.159'
HEADERS = {'Content-Type': 'application/json'}
EMP_ID = ''


def init_log():
    # 1、日志器
    logger = logging.getLogger()
    # 2、设置等级
    logger.setLevel(logging.INFO)
    # 3、设置处理器
    #   3.1 控制台处理器
    sh = logging.StreamHandler()
    #   3.2 文件处理器         ❀ __file__ 所在文件的绝对路径
    filename = BASE_DIR + '/log/ihrm.log'
    fh = logging.handlers.TimedRotatingFileHandler(filename, when='S', interval=1, backupCount=7)  # 最新生成的7个日志文件

    # 4、设置格式化器
    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    formatter = logging.Formatter(fmt)

    # 组装
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)
    logger.addHandler(sh)
    # logger.addHandler(fh)
