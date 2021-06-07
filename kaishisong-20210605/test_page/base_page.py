# -*- coding: utf-8 -*-  
# Author    ： 怕你呀
# Time      ： 2021/5/21
# File      ： base_page
# IDE       ： PyCharm
import logging

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class BasePage:
    log = logging.getLogger(__name__)

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def swipe_find_element(self, text, num=5, direction='down', is_find=1, position=0.5):
        """

        :param text: 查找的文字
        :param num: 查找次数
        :param direction: 查找方向
        :param is_find: 是否查找
        :param position: 滑动百分比
        :return:
        """
        for i in range(0, num):
            try:
                if is_find == 1:
                    element = self.find_element(MobileBy.XPATH, f'//*[contains(@text,"{text}")]')
                    return element
            except NoSuchElementException:
                # 屏幕尺寸
                size = self.driver.get_window_size()
                width = size['width']

                height = size['height']
                # 向下查找
                start_x_down = width / 2
                start_y_down = height * 0.8
                stop_x_down = start_x_down
                stop_y_down = height * position
                # 向右查找
                start_x_left = width * 0.9
                start_y_left = height * 0.5
                stop_y_left = start_y_left
                stop_x_left = width * 0.1
                if direction == 'down':
                    self.driver.swipe(start_x_down, start_y_down, stop_x_down, stop_y_down, duration=1000)
                elif direction == 'left':
                    self.driver.swipe(start_x_left, start_y_left, stop_x_left, stop_y_left, duration=1000)

            if i == num - 1 and is_find == 1:
                # 如果达到 num-1次没有找到，则抛出这个异常
                raise Exception(f"找了{i}次，未找到")

    def find_element(self, by, ele=None):
        """
        :param by:
        :param ele:
        :return:
        """
        if ele:
            return self.driver.find_element(by, ele)
        else:
            return self.driver.find_element(*by)

    def click_find_element(self, ele):
        return ele.click()

    def allow_always(self):
        self.driver.implicitly_wait(1)
        """
        同意权限
        :return:
        """
        i = 1
        while 1:
            e = 0
            try:
                # 同意有"始终允许"选项的权限
                self.click_element(By.XPATH, '//*[contains(@text, "始终允许")]')
            except NoSuchElementException:
                e = 1

            try:
                # 同意小米的权限
                self.click_element(By.XPATH, '//*[contains(@text, "使用中允许")]')

            except NoSuchElementException:
                e = 2
            if e == 2:
                self.driver.implicitly_wait(5)
                break

    def click_element(self, by, ele=None):
        """
        :param by:
        :param ele:
        :return:
        """
        if ele:
            return self.driver.find_element(by, ele).click()
        else:
            return self.driver.find_element(*by).click()

    def send_element(self, by, ele=None, val=None):
        """
        :param val:
        :param by:
        :param ele:
        :return:
        """
        if ele:
            return self.driver.find_element(by, ele).send_keys(val)
        else:
            return self.driver.find_element(*by).send_keys(val)

    def find_android_uiautomator(self, ele):
        """
        通过android_uiautomator 查找
        :param ele:
        :return:
        """
        return self.driver.find_element_by_android_uiautomator(ele)

    def click_android_uiautomator(self, ele):
        """
        通过android_uiautomator 查找
        :param ele:
        :return:
        """
        return self.driver.find_element_by_android_uiautomator(ele).click()

    def get_toast(self):
        """
        获取toast内容
        :return: 返回toast获取的内容text
        """
        return self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
