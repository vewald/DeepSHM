# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 09:10:44 2019

@author: vewald
"""

import h5py
filename = "predictor.h5"

h5 = h5py.File(filename,'r')

data = h5.get('0').value

h5.close()