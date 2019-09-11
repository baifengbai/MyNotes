
import argparse

parser = argparse.ArgumentParser(description='解析命令行参数')
parser.add_argument('-v','--verbose',action='store_const',const='Test') # 添加选项参数'-v'，且设置参数为布尔值，此时默认为False
args = parser.parse_args()
print(vars(args))