from scipy.io import loadmat
import numpy as num
import math

data = loadmat('16_state.mat')
data1 = loadmat('exo0.5_endo1.0023_h1.mat')
rows, cols = (16, 16)
mut = [[0 for i in range(cols)] for j in range(rows)]


state = data.get('STATE')
eqADD = data1.get('eqADD')
QADD = data1.get('QADD')
eqPROD = data1.get('eqPROD')


def pairwise(num1, num2, s1, s2):
    su = 0
    for i in range(0, 65536):
        if state[i, num1] == s1 and state[i, num2] == s2:
            su += eqADD[i]

    return su
pairs = num.zeros((16,16,4))

for row in range (0,16):
    for col in range (0,16):
        pairs[row,col,0] =pairwise(row, col, 0,0)
        pairs[row,col, 1] =pairwise(row, col, 0,1)
        pairs[row,col, 2] =pairwise(row, col, 1,0)
        pairs[row,col, 3] =pairwise(row, col, 1,1)


def margins(num, s):
    su = 0
    for i in range(0, 65536):
        if state[i, num] == s:
            su += eqADD[i]
    return su

marginARR=[]
for i in range (0,16):
    marginARR.append(margins(i,0))
print(marginARR)
for row in range(0,16):
    for col in range(0,16):
        mutsum = 0
        mutsum += pairs[row][col][0] * num.log2((pairs[row][col][0])/(marginARR[row]*marginARR[col]))
        mutsum += pairs[row][col][1] * num.log2((pairs[row][col][1])/(marginARR[row]*(1-marginARR[col])))
        mutsum += pairs[row][col][2] * num.log2((pairs[row][col][2])/((1-marginARR[row])*marginARR[col]))
        mutsum += pairs[row][col][3] * num.log2((pairs[row][col][3])/((1-marginARR[row])*(1-marginARR[col])))
        mut[row][col] = mutsum



print(pairwise(0, 1, 1, 0) + pairwise(0, 1, 0, 0) + pairwise(0, 1, 1, 1) + pairwise(0, 1, 0, 1))

print(margins(1, 1))
