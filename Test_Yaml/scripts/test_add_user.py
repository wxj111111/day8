import sys,os,pytest
sys.path.append(os.getcwd())

from Page.Page import Page_Obj
from Base.Init_driver import init_driver
from Base.Read_Data import ret_yaml_data

def yaml_add_data():
    data_list = []
    data = ret_yaml_data("add_user_data").get("Add_User_Data")
    for i in data.keys():
        data_list.append((i,data.get(i).get("name"),data.get(i).get("phone")))
    return data_list

class Test_Add_Page:
    def setup_class(self):
        self.driver = init_driver()
        self.add_obj = Page_Obj(self.driver).return_add_page()

    def teardown_class(self):
        self.driver.quit()

    @pytest.fixture()
    def click(self):
        # 点击新建联系人
        self.add_obj.click_add()

    @pytest.mark.usefixtures("click")
    @pytest.mark.parametrize("test_num,name,phone",yaml_add_data())
    def test_add(self,test_num,name,phone):
        print("用例编号：", test_num)
        self.add_obj.input_add_click_return(name,phone)
        self.driver.keyevent(4)
