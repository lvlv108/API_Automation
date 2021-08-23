# -*- coding: utf-8 -*-
# @Time    : 2018/7/30 下午4:14
# @File    : Test_Collections.py

import allure
from API_Automation.Params.params import Collections
from API_Automation.Conf.Config import Config
from API_Automation.Common import Request
from API_Automation.Common import Consts
from API_Automation.Common import Assert


class TestCollections:

    @allure.feature('Home')
    @allure.severity('normal')
    @allure.story('Collections')
    def test_collections_01(self, action):
        """
            用例描述：验证实习转试用test薪资结果
        """
        conf = Config()
        data = Collections()
        test = Assert.Assertions()
        request = Request.Request(action)

        host = conf.host_debug
        req_url = 'http://' + host
        urls = data.url
        params = data.data

        api_url = req_url + urls[0]

        response = request.post_request(api_url, params[0])
        print(f"response['body']=========={response['body']}")

        assert test.assert_code(response['code'], 200)
        assert test.assert_in_text(response['body']['data']['data'][0]['base_salary'], '10,000.00')
        assert test.assert_in_text(response['body']['data']['data'][0]['base_performance'], '477.27')
        assert test.assert_in_text(response['body']['data']['data'][0]['compensate'], '-')
        assert test.assert_in_text(response['body']['data']['data'][0]['rank_salary'], '5,000.00')
        assert test.assert_in_text(response['body']['data']['data'][0]['actuall_salary'], '9,850.00')
        Consts.RESULT_LIST.append('True')





