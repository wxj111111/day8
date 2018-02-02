import sys,os
sys.path.append(os.getcwd())
from Page.search_page import Search_Page
from Page.add_user_page import Add_User_Page

class Page_Obj:
    def __init__(self,driver):
        self.driver = driver

    def return_page(self):
        return Search_Page(self.driver)

    def return_add_page(self):
        return Add_User_Page(self.driver)