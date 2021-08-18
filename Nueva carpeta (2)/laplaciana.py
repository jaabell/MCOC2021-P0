# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 18:07:25 2021

@author: matia
"""

from numpy import zeros 

def laplaciana(N):
    A = zeros((N,N))
    
    for i in range(N):
      for j in range(N):
            if i==j:
                A[i,i]=2
            elif abs(i-j)==1:
                A[i,j]=-1
            
    return 

