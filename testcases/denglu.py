# -*- coding: utf-8 -*-
# @Time : 2023/10/7 19:25
# @Author : 17507
# @File : denglu
# @Project : pytest_demo
import json, pytest, random
import requests
from deepdiff import DeepDiff
import config.fw_config
class Test_demo():

    # def test_demo2(self):
    #     url = "https://www.baidu.com"
    #     response = requests.get(url)
    #     print(response)
    #
    # def test_delu(self):
    #     url = config.fw_config.user
    #     data=config.fw_config.user1
    #     response = requests.post(url,data)
    #     print(response.status_code)
    #     print(response.content)



    def test_admindelu(self):
        url = 'http://127.0.0.1/index.php?m=Admin&c=Admin&a=login&t=0.8997745857908359&username=admin&password=123456&vertify=0000'
        response = requests.post(url)
        # print(response.status_code)
        # print(response.content)
        assert response.status_code


if __name__ == "__main__":
    pytest.Test_demo(["vs"])


