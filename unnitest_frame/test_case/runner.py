
import unittest
from BeautifulReport import BeautifulReport
#批量运行各个test模块的用例
# suite=unittest.TestSuite()
# suite.addTests(unittest.defaultTestLoader.discover(start_dir=r'D:\Python\loguru\selenium',pattern='test*.py'))
# test_runner=unittest.TextTestRunner()
# test_runner.run(suite)

#1.加载测试用例
cases=unittest.defaultTestLoader.discover(start_dir=r'D:\Python\loguru\test_case',pattern='test*.py')
#2.执行测试用例
result = BeautifulReport(cases)
#3.输出测试报告
result.report(description='测试报告2',filename='SIT测试报告',report_dir=r'D:\Python\loguru\Report')
