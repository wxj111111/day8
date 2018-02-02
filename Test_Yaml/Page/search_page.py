import sys,os
sys.path.append(os.getcwd())

import Page
from Base.Base import Base

class Search_Page(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)

    def search_click(self):
        # 点击搜索输入框
        self.click_element(Page.search_i)
    def search_input(self,text):
        # 输入内容
        self.input_element(Page.search_i,text)
    def search_return(self):
        # 点击返回
        self.click_element(Page.search_r)