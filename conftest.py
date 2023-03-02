import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示在控制台上
    :return:
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        print(item.nodeid)
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")

# @pytest.fixture(autouse=True)
# def fix1():
#     print('前置1所有的都开始')
@pytest.fixture(params=['前置参数化1','前置参数化2'])
def fix2(request):
    print(request.param)
    yield request.param
@pytest.fixture()
def fix3():
    print('前置3开始')

# def pytest_runtest_setup(item: "Item") -> None:
#     print('hook函数')

@pytest.fixture(scope='class')
def fix5_class():
    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com')
    time.sleep(3)
    yield driver

@pytest.fixture()
def fix4(fix5_class):
    fix5_class.get('https://www.baidu.com')