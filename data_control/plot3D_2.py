#coding: UTF-8
"""
3Dの散布図をplotし、その中心点と各点を点線でつなぐサンプルコード


"""
#3Dを表示するにはmpl_toolkits.mplot3dが必要
from mpl_toolkits.mplot3d import Axes3D
#数値計算用のモジュール
import numpy as np

import matplotlib.pyplot as plot

#データ数
data_num = 100

data = np.random.randn(data_num,3)

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
ax.plot(mean_x,mean_y,mean_z,marker="o",linestyle='none',color='aqua',markersize="10")
print (f"mean(x,y,z) = ({mean_x},{mean_y},{mean_z}))")

for i in range(data_num):
    #この書き方が正しいのかは疑問
    line_x = [mean_x[0],x[i]]
    line_y = [mean_y[0],y[i]]
    line_z = [mean_z[0],z[i]]
    #print (f"mean_x = {mean_x},line_x = {line_x}")
    #ls=Line Style, lw=Linw width
    ax.plot(line_x,line_y,line_z,color="black",ls=":",lw="1")

plot.show()

