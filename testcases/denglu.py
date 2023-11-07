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

    # def test_login(self):
    #     url = 'https://www.wh00.ooo/api/email/users'
        # head = {'Cookie': '_message_backend_session=hghkruW2J92EXLBuUgEjkOV%2FgLHr0FpyQYTQMJagPUCkfUPPlhSdmCuQ20KP8FNJKC%2BN8jTqeoQ6GNFHboUWWxufQqu%2BXb6sqzDBkRs6yFKbLOrGkdbzpiQMy520Z5pPx%2BZkT4uWB4eeEMePofiL2sCnsoMAJ5qM6qLxBaLeYhNRhGSeFYPOTuY%2FpbXo8nxZgv9u991QwRCPHXgFum7Ei76IemZVdvYwgUaiXx7cvsFVKqVT--xWtJYFBUGN4V78A5--HRloQcUgjbfW8ASywIsscA%3D%3D',
        #         'Host': '<calculated when request is sent>',
        #         'accept"': 'application/json',
        #         'user-agent': 'PostmanRuntime/7.34.0',
        #         'accept-language': 'zh-JP'
        #         }
    #     head = {
    #             'Cookie': '_message_backend_session=5SuJHIViAr46rMej%2FISKS9YBEq1gMVqPzdfADDA%2FVn%2F2U49OLGvynboJNl3NXLHokpvuiGP439meXub8DEV9J4%2BeXzdaT8pBx1AHLOvGBBZXl23gM%2FX9yQDJRRy%2FjZsZZOkzyggisJbT2Fs3K8Lw5zyjv1mtVZ5LA3jgn2HAjTKfo%2BqKPyxY5GV0%2F9cCI%2FDlKmuj7%2FsqRlZ4mOFLrqOlupmydLdx5fOKBjcMpZ5Ba2fiEpEs--0YgRbfGjMrsPlURf--4jqqRqtUq7%2F920U1GmHW4Q%3D%3D',
    #             'Host': '<calculated when request is sent>',
    #             'Cache-Control"': 'no-cache',
    #             'Postman-Token"': '<calculated when request is sent>'
    #         }
    #
    #     data = {'user[email]': '1420990591@qq.com',
    #             'user[password]': '12345678',
    #             'user[display_name]': 'zyj',
    #             # 'user[profile_image]': 'profile_images/images/368EB0B1-761D-41E7-BCC5-4A3C8B4BF5FD.jpeg',
    #             'user[username]':'zyaojie',
    #             'user[birthday]':'1999-10-29'
    #             }
    #
    #     register = requests.post(url, params=data, headers=head)
    #     print(register.status_code)
    #     print(register.content)

    def test_xiugai(self):
        url= 'https://www.wh00.ooo/api/user?user'
        test = {'Host': "www.whoo.ooo",
                'Cookie': '_message_backend_session=IC6bdBMXV3WCFQV3FaFkGPoMpIiBY3mnw1Ulug0IMVll%2B1sNsj3ysPTNb%2F0hH39x1OC%2BBRe%2BKAPD1MsaumRFtqmWsxLr%2F%2BBMo2P7I0nCIUsME7coNQx%2B0BDhqxFfFwtSvVGA4bZ%2FOhwaX%2F3hKv0GCXWr6xZ%2FGwmuQmyoiI%2Bb2VqkBbJ1V67KPvm0hVVcKtP9KEJ8MM8%2Fn62uHlHq8Fu0M6sGX16h2TRSNLkMp8wwulHFi1FH--caKVZGSE3dUWKD%2BM--sQZVCKKgbXUCoKy%2B9rfUoQ%3D%3D',
                "accept": "application/json",
                'user-agent': 'app.whoo/0.14.3 iOS/16.3',
                'accept-language':'zh-CN',
                'authorization':'Bearer eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxMjUyMjA5OX0.aIQ1ALNFyGrXg_Iu4xX54hrORksbdjYCXteuim0F7xU'}
        data= {'user[username]': 'zhangyaojie'}
        xiugai=requests.patch(url, data=data,headers=test )
        print(xiugai.status_code)
        print(xiugai.content)


if __name__ == "__main__":
    pytest.Test_demo(["vs"])


