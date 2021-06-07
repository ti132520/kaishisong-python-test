# -*- coding: utf-8 -*-  
# Author    ： 怕你呀
# Time      ： 2021/5/21
# File      ： test_kaishisong_index
# IDE       ： PyCharm
import allure
import pytest

from test_page.kai_shi_song import KaiShiSong


class TestKaiShiSong:
    def setup_class(self):
        self.app = KaiShiSong(ver='ser')

    def teardown_method(self):
        self.app.restart()

    def teardown_class(self):
        self.app.stop()

    @pytest.mark.login
    @pytest.mark.parametrize('user', [{'mobile': 18884396010, 'password': 'c1234567'},
                                      {'mobile': 18884396011, 'password': 'c123456'}])
    @allure.title("登录测试")
    def test_login(self, user):
        with allure.step('1.打开"开始送app"'):
            app = self.app.goto_main()
            file = open(self.app.save_screenshot(), 'rb').read()
            allure.attach(file, '截图', allure.attachment_type.PNG)
        with allure.step('2.跳转到登录页面；'):
            app = app.goto_user_info()
            file = open(self.app.save_screenshot(), 'rb').read()
            allure.attach(file, '截图', allure.attachment_type.PNG)
        with allure.step(f'3、输入手机号{user["mobile"]} 输入密码{user["password"]}'):
            app = app.login(user['mobile'], user['password'])
            file = open(self.app.save_screenshot(), 'rb').read()
            allure.attach(file, '截图', allure.attachment_type.PNG)

        with allure.step(f'5、判断登录是否成功'):
            is_login = app.is_login()
            file = open(self.app.save_screenshot(), 'rb').read()
            allure.attach(file, '截图', allure.attachment_type.PNG)
            assert is_login

