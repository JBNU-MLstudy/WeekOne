# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 23:20:50 2020

@author: user
"""

# 급여계산기

sh = input("몇시간?: ")
sr = input("참여율?: ")

fh = float(sh) # 실수형으로 변환
fr = float(sr)

if fh > 40 :
#    print("초과시간")
    req = fr * fh # 정량시간에 대한 계산
    otp = (fh - 40.0) * (fr*1.5) 
#    print(reg, otp)
    xp = reg + otp
else:
#    print("적당히 한듯")
    xp  = fh * fr
print("너의 급여는: ", xp)
