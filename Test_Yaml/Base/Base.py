from selenium.webdriver.support.wait import WebDriverWait


class Base:
    def __init__(self,driver):
        self.driver = driver

    def find_element(self,loc,timeout=5,poll=0.5):
        """
        :param loc:  元组 格式为：（By.XX,value值）
        :param timeout:
        :param poll:
        :return:
        """
        return WebDriverWait(self.driver,timeout,poll).until(lambda x: x.find_element(*loc))

    def find_elements(self,loc,timeout=5,poll=0.5):
        return WebDriverWait(self.driver,timeout,poll)\
            .until(lambda x: x.find_elements(*loc))

    def click_element(self,loc):
        # 点击元素
        self.find_element(loc).click()

    def input_element(self,loc,text):
        #输入内容
        el = self.find_element(loc)
        el.clear()
        el.send_keys(text)

    def if_disp(self,loc):
        # 判断元素是否存在
        try:
            self.find_element(loc)
            return True
        except Exception as e:
            return False
