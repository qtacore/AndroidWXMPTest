# -*- coding: UTF-8 -*-
#
# Tencent is pleased to support the open source community by making AndroidWXMPTest available.
# Copyright (C) 2019 THL A29 Limited, a Tencent company. All rights reserved.
# Licensed under the BSD 3-Clause License (the "License");you may not use this
# file except in compliance with the License. You may obtain a copy of the License at
# https://opensource.org/licenses/BSD-3-Clause
#
# Unless required by applicable law or agreed to in writing, software distributed
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS
# OF ANY KIND, either express or implied. See the License for the specific language
# governing permissions and limitations under the License.
#
import time
from demolib.demomp import MiniProgramComponentPage, MiniProgramTextPage
from demolib.testcase import DemoTestCase
from settings import MINIPROGRAM_NAME


class HelloTest(DemoTestCase):
    '''示例测试用例
    '''
    owner = "testowner"
    timeout = 5
    priority = DemoTestCase.EnumPriority.High
    status = DemoTestCase.EnumStatus.Design

    def run_test(self):
        self.start_step("打开小程序")
        wxapp = self.login("wxid","wxpasswd")#使用时请替换为实际微信ID和密码
        component_page = wxapp.open_mini_program(MINIPROGRAM_NAME, MiniProgramComponentPage)
        self.start_step("操作小程序内容及验证检查点")
        component_page.open_component_page('基础内容', 'text')
        time.sleep(2)
        textpage = MiniProgramTextPage(wxapp)
        textpage.add_line()
        textpage.add_line()
        inner_text='''2011年1月，微信1.0发布\n同年5月，微信2.0语音对讲发布'''
        self.assert_equal("判断文字内容",inner_text,textpage.control('文本区域').inner_text)
        textpage.remove_line()
        self.assert_equal("判断文字内容", "2011年1月，微信1.0发布", textpage.control('文本区域').inner_text)


if __name__ == '__main__':
    HelloTest().debug_run()
