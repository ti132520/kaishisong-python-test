# -*- coding: utf-8 -*-  
# Author    ： 怕你呀
# Time      ： 2021/5/21
# File      ： main_page
# IDE       ： PyCharm
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException
import time
from test_page.base_page import BasePage
from test_page.user_info_page import UserInfoPage


class MainPage(BasePage):
    __by_of_user_info = (MobileBy.XPATH, '//*[@resource-id="com.supersendcustomer:id/main_toolbar"]'
                                         '/android.widget.ImageButton')
    __by_of_login_btn = (MobileBy.XPATH, '//*[@resource-id="com.supersendcustomer:id/activity_login_btn"]')
    __by_of_com_input_address = (MobileBy.ID, 'com.supersendcustomer:id/tv_input_address')
    __by_of_com_out_address = (MobileBy.ID, 'com.supersendcustomer:id/tv_out_address')
    __by_of_selected_weight = (MobileBy.XPATH, '//*[contains(@text, "公斤")]/preceding-sibling::android.widget.TextView[1]')

    def goto_user_info(self):
        self.click_element(self.__by_of_user_info)
        return UserInfoPage(self.driver)

    def is_login(self):
        self.click_element(self.__by_of_user_info)
        try:
            self.find_element(self.__by_of_login_btn)
            raise Exception("没有登录")
        except NoSuchElementException:
            return True

    def fill_in_from(self, from_address, to_address, item_select, weight, select_time):
        # 选择寄件地址
        self.click_element(self.__by_of_com_input_address)
        time.sleep(3)
        self.swipe_find_element(from_address).click()

        # 选择收件地址
        self.click_element(self.__by_of_com_out_address)
        time.sleep(3)
        self.swipe_find_element(to_address).click()
        # 物品选择
        self.click_element(MobileBy.XPATH, f'//*[contains(@text, "{item_select}")]')

        selected_height = self.find_element(self.__by_of_selected_weight).text()
        print(selected_height)


