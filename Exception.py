# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 23:23:35 2020

@author: user
"""
# 급여계산기

sh = input("몇시간?: ")
sr = input("참여율?: ")
try: 
    fh = float(sh) # 실수형으로 변환
    fr = float(sr)
except: 
    print("숫자 넣어라")
    quit() #그만두기 

# print(fh,fr)
if fh > 40 :
    req = fr * fh # 정량시간에 대한 계산
    otp = (fh - 40.0) * (fr*1.5) 
    xp = reg + otp
else:
    xp  = fh * fr
print("너의 급여는: ", xp)
