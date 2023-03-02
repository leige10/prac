import os


def ddb_dd1(fix2,fix3):
    assert 1==2
def test_dd2(fix2):
    assert 1==1
    print('用例之中'+'   '+fix2)
# def test_aad3():
#     assert 1==3
# def test_aad1():
#     assert 1==1
import logging
logging.basicConfig(encoding='utf-8',level=logging.DEBUG,format=' %(asctime)s - %(levelname)s -%(message)s '
                                                                '(%(filename)s %(lineno)s',
                    datefmt='%m/%Y/%d %I/%M/%S %p',
                    )
logging.error('error')
logging.info('info')
logging.warning('waring')

def get_logger():
    # create logger  创建对象
    logger = logging.getLogger(os.path.basename(__file__))
    logger.setLevel(logging.DEBUG)
    # create console handler and set level to debug  创建处理器
    ch = logging.FileHandler(filename='./lxlmylog.log', encoding="utf-8")
    ch.setLevel(logging.DEBUG)
    # create formatter 创建格式器
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # add formatter to ch  格式器添加到处理器
    ch.setFormatter(formatter)
    # add ch to logger  处理器添加到对象
    logger.addHandler(ch)
    return  logger
a=get_logger()
a.info('123')



