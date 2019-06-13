from xToolkit import xdatetime as xdt
from xToolkit import xthreading
from time import ctime, sleep
import arrow

if __name__ == "__main__":
    # print("现在时间：{}".format(xdt.now()))
    # print("格式化现在时间：{}".format(xdt.now().format("YYYY-MM-DD HH:mm:ss")))
    # print("验证格式 1988-07-20 是否错误,返回值{}".format(xdt.shape("1988-07-20")))
    # print("验证格式 1988-07-88 是否错误,返回值{}".format(xdt.shape("1988-07-88")))
    # print("验证格式 98787987 是否错误,返回值{}".format(xdt.shape("98787987")))
    # print("当月第一天和最后一天:{}".format(xdt.start_and_end()))
    # print("下个月第一天和最后一天:{}".format(xdt.start_and_end(space=1)))
    # print("上个月个月第一天和最后一天:{}".format(xdt.start_and_end(space=-1)))
    # print("今年第一天和最后一天:{}".format(xdt.start_and_end(genre="Y")))
    # print("下个月第一天和最后一天:{}".format(xdt.start_and_end(genre="Y", space=1)))
    # print("上个月个月第一天和最后一天:{}".format(xdt.start_and_end(genre="Y", space=-1)))
    # print("星期字典{}".format(xdt.get_week_dict(start="2019-05-01", end="2019-05-08")))
    #
    # print('开始在：', ctime())
    #
    #
    # # 斐波那契
    # def fib(arguments):
    #     sleep(2)
    #     return "0"
    #
    #
    # # 阶乘
    # def fac(arguments):
    #     sleep(3)
    #     return "1"
    #
    #
    # # 累加
    # def sum(arguments):
    #     sleep(3)
    #     return "2"
    #
    #
    # funcs = [fib, fac, sum]
    # # 参数样式
    # arguments = {"fib": [1], "fac": [2], "sum": [3]}
    # a = xthreading.xthreading(funcs, arguments)
    #
    # print(a)
    # print('结束于：', ctime())

    a = xdt.get_age_date("1988-11-25", "days")
    b = xdt.get_age_date("1988-12-20", "years")

    print(a)
    print(b)
