#coding: UTF-8
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

osaka = pd.read_csv('./data/Osaka_u.csv',
                    skiprows=[0,1,2,3,4],
                    header=None,
                    usecols=[0,1,2,3,5],
                    names=('date','temperature','humited','precipitaion','SunshineHours'))
fukui = pd.read_csv('./data/Fukui_u.csv',
                    skiprows=[0,1,2,3,4],
                    header=None,
                    usecols=[0,1,2,3,5],
                    names=('date','temperature','humited','precipitaion','SunshineHours'))

print("==Osaka==")
print(osaka.head())
print("==Fukui==")
print(fukui.head())

print(osaka.temperature)
osaka.plot()
