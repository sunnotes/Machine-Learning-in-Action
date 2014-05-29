'''
Created on 2014年5月30日

@author: EASON
'''
from numpy import *

print(random.rand(4,4))


randMat = mat(random.rand(4,4))
randMat.I
invRandMat =  randMat.I
print(randMat* invRandMat)