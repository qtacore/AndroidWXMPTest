## 微信小程序Demo工程
 这是微信小程序的Demo使用项目，以Android端的微信官方提供的示例小程序作为目标对象，构建的自动化测试Demo工程。

### 安装依赖库
```shell
cd /path/to/project
pip install -r requirements.txt
```

### 执行demo测试用例
该demo需要运行在一台已经安装好微信的Android手机上。执行命令如下：
```shell
cd /path/to/project
python manage.py runtest demotest.hello
```
以上命令会执行demotest目录下，hello文件中所有自动化测试用例

### Demo说明
本工程使用了[wxmplib][1]提供的微信小程序自动化接口，该项目提供了：微信登录、登录弹框处理以及打开小程序的接口。项目目录结构如下所示：
![enter description here][2]

demolib用于存放测试基类及小程序的页面封装。对于小程序而言需要将每次跳转封装一个WXMPPage，例如示例程序的Text页面可以放装如下：
```python
class MiniProgramTextPage(WXMPPage):
    '''小程序text组件界面
    '''
    ui_map = {
        '文本区域': XPath('//wx-text/span[2]'),
        '添加一行': XPath('//wx-button[text()="add line"]'),
        '移除一行': XPath('//wx-button[text()="remove line"]')
    }

    def add_line(self):
        self.control('添加一行').click()

    def remove_line(self):
        self.control('移除一行').click()

```
MiniProgramTextPage继承自wxmplib的WXMPPage（WXMPPage是QT4W的WebPage子类），使用ui_map定义页面元素，并定义了该页面的两个操作：添加一行和移除一行。小程序界面本质上是Web页面，这里的页面封装方式可以参开[QT4W的页面][3]封装方式。
demotest目录存放测试用例，一个典型的小程序自动化测试用例如下所示：
```python
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
        wxapp = self.login("wxid","wxpasswd") #使用时请替换为实际微信ID和密码
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


```
首先使用测试基类提供的login(wxid,wxpwd)登录微信,该方法会返回一个WXAPP对象(wxmplib封装的对象，其中封装了一些微信相关的基础能力),我们这里使用open_mini_program()进入小程序,其中第一个参数是小程序名，第二个参数是对应的页面封装类型。执行时需要将这个里的换成真实的微信id及密码。在默认情况下在一个测试工程只会测试一个小程序，因此我们在setting文件中提供了小程序配置项MINIPROGRAM_NAME,：
```python
import os 
PROJECT_NAME = "AndroidWXMPTest"
PROJECT_MODE = "standalone"
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
INSTALLED_APPS = []
DRUN_TASK_ENTRY = 'qt4a.task'
MINIPROGRAM_NAME = '小程序示例'
```
该配置项用于设置小程序名，在测试时可以直接使用该配置项。更多关于测试用例的信息，可以参考[QTA的基础测试用例][4]。




  [1]: https://github.com/qtacore/AndroidWXMPLib
  [2]: image/content.PNG "content.png"
  [3]: https://qt4w.readthedocs.io/zh_CN/latest/usage.html
  [4]: https://qta-testbase.readthedocs.io/zh/latest/testcase.html