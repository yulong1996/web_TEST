import unittest
from common import HTMLTestRunner_cn
import time

# 用例路径
casePath = "F:\\jkjob\\workspace\\web_auto\\test_case"
# 匹配规则
rule = "test*.py"

discover = unittest.defaultTestLoader.discover(start_dir=casePath, pattern=rule)
# print(discover)

# 报告存放的路径
reportPath = "F:\\jkjob\\workspace\\web_auto\\report\\" + "result.html"
# 打开文件写入
fp = open(reportPath, "wb")

# retry=1失败重跑一次
runner = HTMLTestRunner_cn.HTMLTestRunner(stream=fp,
                                          title="云平台登录测试报告",
                                          description="共六条测试用例",
                                          retry=1)
runner.run(discover)

fp.close()
