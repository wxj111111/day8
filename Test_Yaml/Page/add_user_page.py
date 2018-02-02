import sys,os
sys.path.append(os.getcwd())

import Page,allure
from Base.Base import Base

class Add_User_Page(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)

    def click_add(self):
        # 点击新建联系人
        self.click_element(Page.add_n)

    def get_user_list(self):
        # 获取联系人列表
        user_data = self.find_elements(Page.)

    def input_add_click_return(self,name,phone):
        # 输入姓名
        self.input_element(Page.add_name,name)
        # 输入电话
        self.input_element(Page.add_phone,phone)
        # 点击保存并返回按钮
        self.click_element(Page.add_save_return)
        # 判断是否在用户详情页
        if self.if_disp(Page.user_edit_btn):
            self.driver.keyevent(4)

