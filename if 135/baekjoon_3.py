# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 23:49:45 2020

@author: user
"""

a=int(input())

if a%4==0 and (a%100!=0 or a%400==0):
    print("1")
else: 
    print("0")