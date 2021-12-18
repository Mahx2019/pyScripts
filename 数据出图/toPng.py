'''
参数说明
xo:X轴数据
yo:Y轴数据
respath:图片输出路径（png）
'''


xo = [5, 7, 12, 15, 17, 20, 25]
yo = [2.62, 3.04, 9.44, 42, 23, 16.8, 14.2]
respath = r'./res/demo.png'


import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import numpy as np
from scipy.optimize import leastsq
import os




def mkdir(path):
	folder = os.path.exists(path)
	if not folder:os.makedirs(path)

def calPng(xo, yo, respath):
    xmin, xmax, ymin, ymax = min(
        xo)*0.95, max(xo)*1.05, min(yo)*0.95, max(yo)*1.05
    # 原始数值
    x = np.array(xo, dtype='float')
    y = np.array(yo, dtype='float')

    # 六次
    params = [0, 0, 0, 0, 0, 0, 0]

    def polynomialFun(a, x):
        k1, k2, k3, k4, k5, k6, b = a
        return k6 * x ** 6 + k1 * x ** 5 + k2 * x**4 + k3 * x**3 + k4 * x ** 2 + k5 * x + b

    # 偏差
    def lost(a, fun, x, y):
        return fun(a, x) - y

    # 作图
    # 中文字体
    myFont = FontProperties(fname="C:\Windows\Fonts\msyhbd.ttc")
    plt.figure()
    plt.title(u'demo数据', fontproperties=myFont)
    plt.xlabel(u'X', fontproperties=myFont)
    plt.ylabel(u'Y', fontproperties=myFont)

    # 坐标轴的范围xmin, xmax, ymin, ymax
    plt.axis([xmin, xmax, ymin, ymax])
    plt.grid(True)
    plt.plot(x, y, 'k.')

    funs = [polynomialFun]
    params = [params]
    colors = ['blue']

    # 拟合函数绘图部分
    for i, (func, param, color) in enumerate(zip(funs, params, colors)):
        tmp = leastsq(lost, param, args=(func, x, y))
        plt.plot(x, func(tmp[0], x), color)

    plt.legend(['orign', 'line'], loc='upper left')
    try:
        plt.savefig(respath, dpi=800)
    except:
        pareDir = ''
        for splits in range(len(respath.split('/',-1))-1):
            pareDir+=respath.split('/',-1)[splits]+'/'
        pareDir.strip('/')
        os.makedirs(pareDir)
        plt.savefig(respath, dpi=800)
    plt.show()
    print('创建完成!')


calPng(xo, yo, respath)
