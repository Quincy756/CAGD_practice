import matplotlib.pyplot as plt
import numpy as np
from itertools import combinations
from PyQt5.QtCore import pyqtSignal
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib as mpl
# 计算排列组合数
from scipy.special import comb, perm
# from drawCurves.test.test2 import QmyFigureCanvas
from matplotlib.animation import FuncAnimation
# import matplotlib.animation as ani


# 自定义画布
class MyFigureCanvas(FigureCanvas):
    mouseMove = pyqtSignal(np.float64, mpl.lines.Line2D)  # 自定义触发信号，用于与UI交互

    def __init__(self, *args, **kwargs):
        super(FigureCanvas, self).__init__(*args, **kwargs)
        self.mpl_connect("button_press_event", self.save_selectPos)  # 支持鼠标移动
        self.drawFunc = None

    def save_selectPos(self, event):

        if self.drawFunc:
            self.drawFunc()

    def getDrawFunc(self, drawFunc):
        self.drawFunc = drawFunc


# 自定义画图逻辑及样式
class DrawLines:
    def __init__(self):
        self.x_pointSet = []
        self.y_pointSet = []
        self.ax1 = None


        self.figure = plt.figure(frameon=True, num="10")
        # 几个QWidgets
        self.canvas = MyFigureCanvas(self.figure)

    def setDrawStyles(self):
        pass

    def setFigure(self):
        pass

    def setCanvas(self):
        pass

    def getCanvas(self):
        return self.canvas

    def getFigure(self):
        return self.figure

    def draw(self, x, y):
        self.x, self.y = x, y
        # 线性插值
        # self.x = [1, 2, 6, 20, 30]
        # self.y = [2, 20, 32, 35, 40]
        self.colorList = ['r', 'r','r', 'b']
        # 贝塞尔插值
        self.bezier_x, self.bezier_y = self.bezierFunc()

        # 新建区域ax1
        # figure的百分比,从figure 10%的位置开始绘制, 宽高是figure的80%
        left, bottom, width, height = 0.05, 0.05, 0.94, 0.94
        if self.ax1 and self.figure:
            self.ax1.cla()
            self.figure.clf()
            # self.canvas.draw()

        # 获得绘制的句柄
        self.ax1 = self.figure.add_axes([left, bottom, width, height])
        # self.ax1.set_axis_off()
        self.ax1.set_xticks(np.arange(0, 55, 5))
        self.ax1.set_xlim([0, 50])
        self.ax1.set_yticks(np.arange(0, 55, 5))
        self.ax1.set_ylim([0, 50])
        self.ax1.set_title('area1')
        self.ax1.plot(self.x, self.y, "r-o")
        self.ax1.plot(self.bezier_x, self.bezier_y, "c-")
        self.canvas.draw()



    def bezierFunc(self):
        t_array = np.arange(0, 1.01, 0.01)
        b_xList = []
        b_yList = []
        # 点的个数要比阶数大1
        point_num = len(self.x)
        # 阶数
        n = point_num - 1
        # for t in t_array:
        #     x_temp = 0.0
        #     y_temp = 0.0
        #     for i in range(n+1):
        #         # 计算系数
        #         coefficient = comb(n, i)
        #         x_temp += coefficient * self.x[i] * ((1.0-t)**(n-i)) * (t**i)
        #         y_temp += coefficient * self.y[i] * ((1.0-t)**(n-i)) * (t**i)
        #     b_xList.append(x_temp)
        #     b_yList.append(y_temp)
        # return b_xList, b_yList
        data = np.array([self.x, self.y], dtype=np.float32)
        data = data.T
        coefficient = np.zeros(n+1, np.int32)
        for i in range(n+1):
            # 计算系数矩阵
            coefficient[i] = comb(n, i)
        res = np.dot(coefficient, data)

        for t in t_array:
            x_temp = 0.0
            y_temp = 0.0
            for i in range(n+1):
                # 计算系数
                coefficient = comb(n, i)
                x_temp += coefficient * self.x[i] * ((1.0-t)**(n-i)) * (t**i)
                y_temp += coefficient * self.y[i] * ((1.0-t)**(n-i)) * (t**i)
            b_xList.append(x_temp)
            b_yList.append(y_temp)
        return b_xList, b_yList












# 定义插值算法类
class InterpolAlgo:
    def __init__(self, pointSet):
        pass

# 定义
class BezierCurve(InterpolAlgo):

    def __init__(self, pointSet=None):
        super(InterpolAlgo, self).__init__(pointSet)
        self.pointSet = pointSet
        self.result = []

    def get_result(self):
        return self.result

    def set_pointSet(self, pointSet):
        self.pointSet += pointSet
















