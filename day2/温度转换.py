# -*- coding: UTF-8 -*-
# @date: 2019/8/30 2:08 
# @name: 温度转换.py
# @author：Spring
"""
将华氏温度转换为摄氏温度
F = 1.8C + 32
"""

f = float(input('请输入华氏摄氏度温度:'))
C = (f - 32) / 1.8
print('%.1f华氏摄氏度=%.1f摄氏度' % (f, C))  # .1 表示小数位是1位，.n表示小数位n位

