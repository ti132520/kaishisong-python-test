# -*- coding: utf-8 -*-  
# Author    ： 怕你呀
# Time      ： 2021/5/21
# File      ： kaishisong_page
# IDE       ： PyCharm
import logging
import time
from datetime import datetime

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException

from test_page.base_page import BasePage
from appium.webdriver.webdriver import WebDriver

from test_page.main_page import MainPage


class KaiShiSong(BasePage):
    __by_of_select_ser = (MobileBy.XPATH, '//*[@text="选择服务器"]')
    __by_of_select_url = (MobileBy.XPATH, '//*[contains(@text, "app.dev.kaishisong.com")]')
    __by_of_select_ok = (MobileBy.XPATH, '//*[@text="确定"]')
    # 服务协议同意
    __by_of_server_text = (MobileBy.XPATH, '//*[contains(@text, "服务协议")]')
    __by_of_server_text_ok = (MobileBy.XPATH, '//*[contains(@text, "我知道了")]')

    # 开屏广告的定位
    __by_of_ad_close = (MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/'
                                        'android.widget.FrameLayout/android.widget.FrameLayout/'
                                        'android.widget.LinearLayout/android.widget.ImageView')
    __ver: str

    def __init__(self, ver: str = 'dev', driver: WebDriver = None):
        """
        tish1
        :param ver: 传入版本，dev（测试版本），ser（正式）
        :param driver:
        """
        self.__ver = ver
        if driver:
            self.driver = driver
        else:

            caps = {
                "platformName": "android", "deviceName": "kaishisong", "appPackage": "com.supersendcustomer",
                "appActivity": ".chaojisong.ui.activity.SplashActivity",
                "noReset": True,
                "settings[waitForIdleTimeout]": 0, "skipDeviceInitialization": True, "dontStopAppOnReset": False
            }
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def start(self):
        self.driver.launch_app()
        return self

    def restart(self):
        self.driver.close_app()
        self.driver.launch_app()
        return self

    def stop(self):
        self.driver.quit()

    def goto_main(self) -> MainPage:
        if self.__ver == 'dev':
            # 点击选择服务器
            self.click_element(self.__by_of_select_ser)
            # 选择服务器地址
            self.click_element(self.__by_of_select_url)
            # 点击确认
            self.click_element(self.__by_of_select_ok)
        elif self.__ver == 'ser':
            pass
        else:
            assert Exception("没有传入版本")
        # 软件获取权限
        try:
            if self.find_element(self.__by_of_server_text):
                self.log.info("获取了软件权限")
                self.click_element(self.__by_of_server_text_ok)
                # 始终允许所有权限
                self.allow_always()
                # 向右滑动 跳过特性
                self.swipe_find_element('', 5, 'left', 0)
                # 点击屏幕一个地方跳过特性
                self.driver.swipe(100, 100, 100, 100, 10)
                # 始终允许所有权限
                self.allow_always()
        except NoSuchElementException:
            self.log.info('不是第一次启动')

        # 关闭广告
        try:
            self.find_element(self.__by_of_ad_close)
            self.click_element(self.__by_of_ad_close)
        except NoSuchElementException:
            # 找不到广告 不进行任何操作
            self.log.info('没有广告')
        return MainPage(self.driver)

    def save_screenshot(self):
        time.sleep(2)
        filename = 'screenshot/' + datetime.now().__str__() + '.png'
        self.driver.save_screenshot(filename)
        return filename
