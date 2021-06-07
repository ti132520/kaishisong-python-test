# -*- coding: utf-8 -*-  
# Author    ： 怕你呀
# Time      ： 2021/5/29
# File      ： user_info_page
# IDE       ： PyCharm
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException

from test_page.base_page import BasePage


class UserInfoPage(BasePage):
    __by_of_user_info = (MobileBy.XPATH, '//*[@resource-id="com.supersendcustomer:id/main_toolbar"]'
                                         '/android.widget.ImageButton')
    __by_of_login_btn = (MobileBy.XPATH, '//*[@resource-id="com.supersendcustomer:id/activity_login_btn"]')
    __by_of_mobile = (MobileBy.XPATH, '//*[@resource-id="com.supersendcustomer:id/activity_login_username"]')
    __by_of_password = (MobileBy.XPATH, '//*[@resource-id="com.supersendcustomer:id/activity_login_pass"]')

    def goto_main_page(self):
        # 局部引入
        from test_page.main_page import MainPage

        return MainPage(self.driver)

    def login(self, mobile, password):
        """
        登录方法
        :param mobile: 登录手机号
        :param password: 密码
        :return:
        """
        self.send_element(self.__by_of_mobile, val=mobile)
        self.send_element(self.__by_of_password, val=password)
        self.click_element(self.__by_of_login_btn)
        toast = self.get_toast()
        if '登录成功' in toast:
            from test_page.main_page import MainPage
            return MainPage(self.driver)
        else:
            raise Exception(toast)

