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
'''
项目管理和辅助工具
'''

import sys
import os

proj_root = os.path.dirname(os.path.abspath(__file__))
if proj_root not in sys.path:
    sys.path.insert(0, proj_root)
exlib_dir = os.path.join(proj_root, 'exlib')
if os.path.isdir(exlib_dir):
    for filename in os.listdir(exlib_dir):
        if filename.endswith('.egg'):
            lib_path = os.path.join(exlib_dir, filename)
            if os.path.isfile(lib_path) and lib_path not in sys.path:
                sys.path.insert(0, lib_path)
            
from testbase.management import ManagementTools

if __name__ == '__main__':    
    ManagementTools().run()
