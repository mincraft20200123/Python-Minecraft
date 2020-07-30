# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 16:31:10 2020

@author: appedu
"""
A=[1,89,56,9,42,37,6]
for i in range(len(A)):
    for j in range(len(A)-i-1):
        if A[j]>A[j+1]:
            T=A[j]
            A[j]=A[j+1]
            A[j+1]=T
            print(A)