import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from time import time,clock
import threading as thd
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.ion()
def plot_cloud_model(Ex, En, He, n, title='', grid=False):
    # Ex = 0      # 期望
    # En = 1      # 熵
    # He = 0.1    # 超熵
    # n = 500     # 云滴个数

    Y = np.zeros((1, n))
    np.random.seed(int(time()))
    X = np.random.normal(loc=En, scale=He, size=n)
    Y = Y[0]
    # 用来正常显示负号
    fig = plt.figure(len(plt.get_fignums()))
    ax = fig.add_subplot(111)
 
    for i in range(n):
        np.random.seed(int(time())+i+1)
        Enn = X[i]
        X[i] = np.random.normal(loc=Ex, scale=np.abs(Enn), size=1)
        Y[i] = np.exp(-(X[i]-Ex)*(X[i]-Ex)/(2*Enn*Enn))

    ax.scatter(X, Y, s=10, alpha=0.5, c='r', marker='o',label='云图1')
    if title == '':
        title = '期望:%.2f,熵:%.2f,超熵:%.2f,云滴数:%d' % (Ex, En, He, n)
    ax.set_title(title)
    ax.legend(loc='best')
    ax.set_xlabel('指标值')
    ax.set_ylabel('确定度')
    ax.grid(True)




def plot_2d_cloud_model(Ex, En, He, n, title='', grid=False):
    # 画第一张图
    Y = np.zeros((1, n))
    np.random.seed(int(time()))
    X0 = np.random.normal(loc=En[0], scale=He[0], size=n)
    Y = Y[0]
    np.random.seed(int(time())+1)
    X1 = np.random.normal(loc=En[1], scale=He[1], size=n)
    # 用来正常显示负号
    fig = plt.figure(len(plt.get_fignums()))
    ax = fig.add_subplot(111, projection='3d')
    for i in range(n):
        Enn0 = X0[i]
        np.random.seed(int(time())+i)
        X0[i] = np.random.normal(loc=Ex[0], scale=np.abs(Enn0), size=1)
        Enn1 = X1[i]
        np.random.seed(int(time())+i+1)
        X1[i] = np.random.normal(loc=Ex[1], scale=np.abs(Enn1), size=1)
        Y[i] = np.exp(-(X0[i] - Ex[0]) * (X0[i] - Ex[0]) / (2 * Enn0 * Enn0)-(X1[i] - Ex[1]) * (X1[i] - Ex[1]) / (2 * Enn1 * Enn1))

    ax.scatter(X0, X1, Y, s=10, alpha=0.5, c='b', marker='o',label='云图1')
    # 画第二张图
    Y = np.zeros((1, n))
    np.random.seed(int(time())+2)
    X0 = np.random.normal(loc=En[0], scale=He[0], size=n)
    Y = Y[0]
    np.random.seed(int(time())+3)
    X1 = np.random.normal(loc=En[1], scale=He[1], size=n)
    Ex[0] = Ex[0]
    Ex[1] = Ex[1]+1
    for i in range(n):
        Enn0 = X0[i]
        np.random.seed(int(time())+i)
        X0[i] = np.random.normal(loc=Ex[0], scale=np.abs(Enn0), size=1)
        Enn1 = X1[i]
        np.random.seed(int(time())+i+1)
        X1[i] = np.random.normal(loc=Ex[1], scale=np.abs(Enn1), size=1)
        Y[i] = np.exp(-(X0[i] - Ex[0]) * (X0[i] - Ex[0]) / (2 * Enn0 * Enn0)-(X1[i] - Ex[1]) * (X1[i] - Ex[1]) / (2 * Enn1 * Enn1))

    ax.scatter(X0, X1, Y, s=10, alpha=0.5, c='g', marker='o',label='云图2')
    # 画第三张图
    Y = np.zeros((1, n))
    np.random.seed(int(time())+4)
    X0 = np.random.normal(loc=En[0], scale=He[0], size=n)
    Y = Y[0]
    np.random.seed(int(time())+5)
    X1 = np.random.normal(loc=En[1], scale=He[1], size=n)
    Ex[0] = Ex[0]+1
    Ex[1] = Ex[1]-1
    for i in range(n):
        Enn0 = X0[i]
        np.random.seed(int(time())+i)
        X0[i] = np.random.normal(loc=Ex[0], scale=np.abs(Enn0), size=1)
        Enn1 = X1[i]
        np.random.seed(int(time())+i+1)
        X1[i] = np.random.normal(loc=Ex[1], scale=np.abs(Enn1), size=1)
        Y[i] = np.exp(-(X0[i] - Ex[0]) * (X0[i] - Ex[0]) / (2 * Enn0 * Enn0)-(X1[i] - Ex[1]) * (X1[i] - Ex[1]) / (2 * Enn1 * Enn1))

    ax.scatter(X0, X1, Y, s=10, alpha=0.5, c='y', marker='o',label='云图3')

    # 画第四张图
    Y = np.zeros((1, n))
    np.random.seed(int(time())+6)
    X0 = np.random.normal(loc=En[0], scale=He[0], size=n)
    Y = Y[0]
    np.random.seed(int(time())+7)
    X1 = np.random.normal(loc=En[1], scale=He[1], size=n)
    Ex[0] = Ex[0]
    Ex[1] = Ex[1]+1
    for i in range(n):
        Enn0 = X0[i]
        np.random.seed(int(time())+i)
        X0[i] = np.random.normal(loc=Ex[0], scale=np.abs(Enn0), size=1)
        Enn1 = X1[i]
        np.random.seed(int(time())+i+1)
        X1[i] = np.random.normal(loc=Ex[1], scale=np.abs(Enn1), size=1)
        Y[i] = np.exp(-(X0[i] - Ex[0]) * (X0[i] - Ex[0]) / (2 * Enn0 * Enn0)-(X1[i] - Ex[1]) * (X1[i] - Ex[1]) / (2 * Enn1 * Enn1))

    ax.scatter(X0, X1, Y, s=10, alpha=0.5, c='r', marker='o',label='云图4')
    if title == '':
        title = '期望:[%.2f,%.2f],熵:[%.2f,%.2f],超熵:[%.2f,%.2f],云滴数:%d' % (Ex[0], Ex[1], En[0], En[1], He[0], He[1], n)
    ax.legend(loc='upper left')
    ax.set_title(title,y=1.1)
    ax.set_xlabel('指标值1')
    ax.set_ylabel('指标值2')
    ax.set_zlabel('确定度')
    ax.grid(True)


plot_cloud_model(0.8004, 0.49,0.01, 100)
plot_cloud_model(1, 0.49,0.01, 100)

plot_2d_cloud_model([0, 1], [0.3, 0.3], [0.01, 0.05], 200)
plot_2d_cloud_model([0, 1], [0.3, 0.3], [0.01, 0.05], 200)

plt.pause(3600)