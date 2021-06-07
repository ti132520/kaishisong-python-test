# -*- coding: utf-8 -*-  
# Author    ： 怕你呀
# Time      ： 2021/5/21
# File      ： test_kaishisong_index
# IDE       ： PyCharm
import allure
import pytest
import yaml

from test_page.kai_shi_song import KaiShiSong


class TestKaiShiSong:
    def setup_class(self):

        self.app = KaiShiSong(ver='dev')
        self.main = self.app.goto_main().goto_user_info().login(18884396010, 'c1234567')

    def teardown_method(self):
        self.app.restart()

    def teardown_class(self):
        self.app.stop()

    @allure.title("报价测试")
    @pytest.mark.parametrize('from_data', yaml.safe_load(open('../../../test_data/from_data.yaml', 'r')))
    def test_quotation(self, from_data: dict):

        self.main.fill_in_from(from_data.get('from_address'), from_data.get('to_address'),
                               item_select=from_data.get('item_select'), select_time=from_data.get('time'),
                               weight=from_data.get("weight"))

