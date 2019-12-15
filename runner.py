import unittest
import time
import os
import logging
from HTMLTestRunner import HTMLTestRunner

#获取项目的根目录
test_dir=os.path.join(os.getcwd())
#自动搜索项目根目录下所有的testcase 构造测试集 返回Testsuit对象
discover=unittest.defaultTestLoader.discover(test_dir,pattern='TestCase_*.py')
now=time.strftime('%Y-%m-%d')#获取当前日期
#测试报告完整路径
result=test_dir+'\\Result_Report\\'+'SuperFA接口测试报告'+'_'+now+'.html'
#日志的完整路径
log=test_dir+'\\Result_Report\\'+'SuperFA接口测试log'+'_'+now+'.txt'
#filename 日志文件路径 level 日志的级别 format 格式
logging.basicConfig(filename=log,level=logging.INFO,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fp=open(result,'wb')#wb方式写入
#构造runner
runner=HTMLTestRunner(
    stream=fp,
    title='SuperFA接口测试报告',
    description='SuperFA接口测试用例执行情况',
    verbosity=2
)
# 使用run()方法运行测试套件（即运行测试套件中的所有用例）
runner.run(discover)