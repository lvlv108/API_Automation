# # -*- coding: utf-8 -*-
# # @Time    : 2018/7/30 下午4:14
# # @File    : Test_Basic.py
# import json
#
# import allure
#
# from API_Automation.Params.params import Basic
# from API_Automation.Conf.Config import Config
# from API_Automation.Common import Request
# from API_Automation.Common import Consts
# from API_Automation.Common import Assert
#
#
#
# class TestBasic:
#
#     @allure.feature('Home')
#     @allure.severity('blocker')
#     @allure.story('Basic')
#     def test_basic_01(self, action):
#         """
#             用例描述：登录失败
#         """
#         conf = Config()
#         data = Basic()
#         test = Assert.Assertions()
#         request = Request.Request(action)
#
#         host = conf.host_debug
#         req_url = 'http://' + host
#         urls = data.url
#         params = data.data
#
#         api_url = req_url + urls[0]
#         response = request.post_request(api_url, params[0])
#
#         assert test.assert_code(response['code'], 400)
#         assert test.assert_body(response['body'], 'msg' ,'校验失败: 用户名或密码错误')
#         assert test.assert_time(response['time_consuming'], 300)
#         Consts.RESULT_LIST.append('True')
#
#     @allure.feature('Home')
#     @allure.severity('normal')
#     @allure.story('Basic')
#     def test_basic_02(self, action):
#         """
#             用例描述：登陆成功
#         """
#         conf = Config()
#         data = Basic()
#         test = Assert.Assertions()
#         request = Request.Request(action)
#
#         host = conf.host_debug
#         req_url = f'http://{host}'
#         urls = data.url
#         params = data.data
#
#         api_url = req_url + urls[1]
#         response = request.post_request(api_url, params[1])
#
#         assert test.assert_code(response['code'], 200)
#         assert test.assert_text(json.loads(response['text']), 'code',0)
#         assert test.assert_time(response['time_consuming'], 300)
#         Consts.RESULT_LIST.append('True')
