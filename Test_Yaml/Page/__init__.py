from selenium.webdriver.common.by import By

# 搜索输入框
search_i = (By.CLASS_NAME,"android.widget.EditText")
# 返回按钮
search_r = (By.ID,"com.android.settings:id/back")

# 联系人
# 新建联系人
add_n = (By.ID,"com.android.contacts:id/menu_add_contact")
# 姓名
add_name = (By.XPATH,"//*[contains(@text,'姓名')]")
# 电话
add_phone = (By.XPATH,"//*[contains(@text,'电话号码')]")
# 保存并返回按钮
add_save_return = (By.ID,"android:id/icon2")
# 用户详情页的编辑按钮
user_edit_btn = (By.ID,"com.android.contacts:id/contact_menuitem_edit")