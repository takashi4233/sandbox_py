#coding: UTF-8
"""
3Dの散布図をplotするサンプルコード
plot(x,y,z)で基本は表示されるが、x,y,zは必ずarray形式とする必要があるので、
１つのデータをプロットしたいだけでも、[]で囲んでarrayにする必要がある。


"""
#3Dを表示するにはmpl_toolkits.mplot3dが必要
from mpl_toolkits.mplot3d import Axes3D
#数値計算用のモジュール
import numpy as np

import matplotlib.pyplot as plot

data = np.random.randn(100,3)

x = data[:,0]
y = data[:,1]
z = data[:,2]

fig = plot.figure()
ax = Axes3D(fig)

#座標軸の定義
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

ax.plot(x,y,z,marker="o",linestyle='none',color='blue')

#x,y,zはarray形式が必須
mean_x = [np.mean(x)]
mean_y = [np.mean(y)]
mean_z = [np.mean(z)]
ax.plot(mean_x,mean_y,mean_z,marker="o",linestyle='none',color='aqua')


data2 = np.random.randn(100,3)
x2 = data2[:,0]
y2 = data2[:,1]
z2 = data2[:,2]
ax.plot(x2,y2,z2,marker="o",linestyle='none',color='red')

#x,y,zはarray形式が必須
mean_x2 = [np.mean(x2)]
mean_y2 = [np.mean(y2)]
mean_z2 = [np.mean(z2)]
ax.plot(mean_x2,mean_y2,mean_z2,marker="o",linestyle='none',color='plum')

plot.show()

