#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 10:24:23 2018

@author: j.wang
"""

import scipy as sc
import matplotlib.pyplot as plt
from scipy.linalg import svd


#%%

file = open("Data", "rb")
omega_read = sc.loadtxt(file)
#om = sc.transpose(omega_read)
#omega1 = omega_read[0]
#omega1 = omega1.reshape(512, 512)
#plt.imshow(omega1)

#%%
u, s, vh = svd(omega_read)

