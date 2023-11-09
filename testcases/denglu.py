# -*- coding: utf-8 -*-
# @Time : 2023/10/7 19:25
# @Author : 17507
# @File : denglu
# @Project : pytest_demo
import json, pytest, random
from urllib import response

import requests
from deepdiff import DeepDiff
import config.fw_config



class Test_demo():

    def test_login(self):
        url = 'https://www.wh00.ooo/api/email/login'

        head = {'Cookie': '_message_backend_session=ugaGaBOa7%2FcVW3I3uev1yML3QuVBh7SxYV%2F8zUjS1DH4R05i%2Ffqja488T1LlY9CvQlI0q3dc8utljpckvNw6ZD1x2BusmWcVpi42ca1yH91OuyD3obnHlmBmJF9CjwK%2FwJ5sXi4a%2Fe5UuYpZYiTSr8FMgJ73g3LpQAtYdomOGN0dTNPr9%2BrCypBvjx9w0LRIpKXonELQgPcj%2FXgo%2FNa2nd24JCHTWY%2Bf%2FLKBu%2Bg%2BO0%2FX8bsi--pojaVWZ7leRX2gbI--V%2Bbo%2F%2FwUTRe2Az53fWqo1Q%3D%3D; path=/; HttpOnly; SameSite=Lax',
                'Host': 'www.wh00.ooo',
                'accept': "application/json",
                'user-agent': 'app.whop/0.14.4 i0S/15.8',
                'accept-language': 'zh-JP'
                }
        data = {'email': '1420990591@qq.com',
                'password': '12345678'
                }
        register=requests.post(url, data=data, headers=head)
        register = json.loads(register.text)
        print(register)

    def test_demo5(self):
        url = "https://www.wh00.ooo/api/user"

        test = {
            "Host": "www.wh00.ooo",
            "accept": "application/json",
            "user-agent": "app.whoo/0.14.3 iOS/16.3",
            "accept-language": "zh-CN",
            'authorization' : 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxMjUyMjA5OX0.aIQ1ALNFyGrXg_Iu4xX54hrORksbdjYCXteuim0F7xU',
            'Accept-Encoding' : 'gzip, deflate, br',
            'Connection' : 'keep-alive',
            'Cookie' : '_message_backend_session=AYLtZmMX4mKXsTOS1hA7L8QFQPOpse2iHTQPrAg5HTdO%2FB9IS8LHAoK8lTir%2FCS3jz7QnEJcwxYtoeEAK81ZZINxSRmBnx%2FnuWyhiRPf4J028TuokVh1R3GId43pIjxO3cwoIBbLHUP260pEcbBtWZpHbd43YtRnTfUnk8n1j22wBUA9jEMVk%2FrXlg0%2BRLVrhq4fkRsUVomA87zAjjS%2Bar2bohpZ5ZDzrfT5D%2B5JLgi9idJA--bRl5USpWJ93Wve4D--%2FU1yHKQSn0uYdQkCJfGUqA%3D%3D',

        }
        data = {
            'user[username]': '142099059432',
            'user[display_name]' : 'llllllllllllll'
        }
        List = requests.patch(url, data=data, headers=test)
        List = json.loads(List.text)
        print(List)


if __name__ == "__main__":
    pytest.Test_demo(["vs"])


