# -*- coding: utf-8 -*-
#
# Tencent is pleased to support the open source community by making AndroidWXMPTest available.
# Copyright (C) 2019 THL A29 Limited, a Tencent company. All rights reserved.
# Licensed under the BSD 3-Clause License (the "License");you may not use this
# file except in compliance with the License. You may obtain a copy of the License at
#
# https://opensource.org/licenses/BSD-3-Clause
#
# Unless required by applicable law or agreed to in writing, software distributed
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS
# OF ANY KIND, either express or implied. See the License for the specific language
# governing permissions and limitations under the License.
#
'''示例测试用例
'''

from wxmplib.account import WeiXinAccount
from wxmplib.wxapp import WeiXinApp
from qt4a.androidtestbase import AndroidTestBase, Device


class DemoTestCase(AndroidTestBase):
    '''测试用例基类
    '''

    def post_test(self):
        '''清理测试用例
        '''
        from qt4a.androiddriver.util import logger
        logger.info('post_test run')
        super(DemoTestCase, self).post_test()
        Device.release_all_device()  # 释放所有设备
        logger.info('postTest complete')

    def login(self,wxid, wxpasswd):
        '''
        :param wxacc: 微信账号
        :return: 小程序APP对象
        '''
        device = self.acquire_device()
        wxacc = WeiXinAccount(wxid, wxpasswd)
        wxapp = WeiXinApp(device)
        wxapp.login(wxacc)
        return wxapp

