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
    # def test_demo5(self):
    #     url = "https://www.wh00.ooo/api/email/login"
    #
    #     test = {
    #         "Host": "www.wh00.ooo",
    #         "Cookie": "_message_backend_session=X7plfcvk1nuSMznj4r2SejthiEXBMTocc9XUTB0zovc%2FzVVX63AqmqEpGIMC4m4ShNcaTGS%2BqMguPl2Bj%2FJ4%2FR%2FUEMnAyajSy1WR2Mz%2FMzkkLRnYFL7CH6OOHY6qwctoTCy5paxsbMTqed5fLfwJRQ126LIQVjG6ONbQ6HrH4KbhAuIMf%2BOmgwEcdA59P2TWcbP0T8MSoKX1UdPXXqN6gj1vFY8Rr9Sm7qWaegsJZM%2Bf0WyB--xV6Wugdt0cl9csp7--3V9FwaNiYBeb5PZfvlIptA%3D%3D",
    #         "accept": "application/json",
    #         "user-agent": "app.whoo/0.14.4 iOS/15.8",
    #         "accept-language": "zh-JP"
    #     }
    #     data = {
    #         "email": "1420990591@qq.com",
    #         "password": "12345678"
    #     }
    #     List = requests.post(url, data=data, headers=test)
    #     List = json.loads(List.text)
    #     print(List)

    # def test_xiugai(self):
    #     url= 'https://www.wh00.ooo/api/user?user'
    #     test = {'Host': "www.whoo.ooo",
    #             'Cookie': '_message_backend_session=IC6bdBMXV3WCFQV3FaFkGPoMpIiBY3mnw1Ulug0IMVll%2B1sNsj3ysPTNb%2F0hH39x1OC%2BBRe%2BKAPD1MsaumRFtqmWsxLr%2F%2BBMo2P7I0nCIUsME7coNQx%2B0BDhqxFfFwtSvVGA4bZ%2FOhwaX%2F3hKv0GCXWr6xZ%2FGwmuQmyoiI%2Bb2VqkBbJ1V67KPvm0hVVcKtP9KEJ8MM8%2Fn62uHlHq8Fu0M6sGX16h2TRSNLkMp8wwulHFi1FH--caKVZGSE3dUWKD%2BM--sQZVCKKgbXUCoKy%2B9rfUoQ%3D%3D',
    #             "accept": "application/json",
    #             'user-agent': 'app.whoo/0.14.3 iOS/16.3',
    #             'accept-language':'zh-CN',
    #             'authorization':'Bearer eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxMjUyMjA5OX0.aIQ1ALNFyGrXg_Iu4xX54hrORksbdjYCXteuim0F7xU'}
    #     data= {'user[username]': 'zhangyaojie'}
    #     xiugai=requests.patch(url, data=data,headers=test )
    #     print(xiugai.status_code)
    #     print(xiugai.content)


if __name__ == "__main__":
    pytest.Test_demo(["vs"])


