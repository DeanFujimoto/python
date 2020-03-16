from scipy.io import loadmat
import numpy as num
import math;
data = loadmat('16_state.mat')
data1 = loadmat('exo0.5_endo1.0023_h1.mat')



eqADD = []
QADD = []
eqPROD = []
##print(data1)
##print(data)
state = data.get('STATE')
print(type(state))
eqADD = data1.get('eqADD')
QADD = data1.get('QADD')
eqPROD = data1.get('eqPROD')
print(state[0])

i = num.sum(eqADD);
##mut = print(eqADD[0])
##print(i)
##print(eqADD[0]);

def pairwise(num1, num2,s1,s2):
    sum =0

    for i in range (0, 65536):
        if state[i, num1]== s1 and state[i ,num2] ==s2:
            sum += eqADD[i]

    return sum\

def margins(num,s):
    sum =0
    for i in range (0, 65536):
        if state[i, num] ==s:
            sum += eqADD[i]
    return sum

##margin takes 0 value marginilizations
margin= []
##margin 0
num =0
for x in range(0, 65536):
    if(x%2 == 0):
        num += eqADD[x]
margin.append(num)


##margin 1

num =0
for i in range (0,65536,4):
    num+= eqADD[i]
    num+= eqADD[i+1]


margin.append(num)
##margin 2

num =0
for i in range (0,65536,8):
    for inner in range(0,4):
        num+= eqADD[i+inner]
margin.append(num)
##margin 3

num =0
for i in range (0,65536,16):
    for inner in range(0,8):
        num+= eqADD[i+inner]
margin.append(num)
##margin 4

num =0
for i in range (0,65536,32):
    for inner in range(0,16):
        num+= eqADD[i+inner]
margin.append(num)
##margin 5

num =0
for i in range (0,65536,32):
    for inner in range(0,16):
        num+= eqADD[i+inner]
margin.append(num)

##margin 6
num =0
for i in range (0,65536,64):
    for inner in range(0,32):
        num+= eqADD[i+inner]
margin.append(num)

##margin 7
num =0
for i in range (0,65536,128):
    for inner in range(0,64):
        num+= eqADD[i+inner]
margin.append(num)

##margin 8
num =0
for i in range (0,65536,256):
    for inner in range(0,128):
        num+= eqADD[i+inner]
margin.append(num)

##margin 9
num =0
for i in range (0,65536,64):
    for inner in range(0,32):
        num+= eqADD[i+inner]
margin.append(num)

##margin 10
num =0
for i in range (0,65536,64):
    for inner in range(0,32):
        num+= eqADD[i+inner]
margin.append(num)


##margin 11
num =0
for i in range (0,65536,2**7):
    for inner in range(0,2**6):
        num+= eqADD[i+inner]
margin.append(num)

##margin 11
num =0
for i in range (0,65536,2**8):
    for inner in range(0,2**7):
        num+= eqADD[i+inner]
margin.append(num)

##margin 12
num =0
for i in range (0,65536,2**9):
    for inner in range(0,2**8):
        num+= eqADD[i+inner]
margin.append(num)

##margin 13
num =0
for i in range (0,65536,2**10):
    for inner in range(0,2**9):
        num+= eqADD[i+inner]
margin.append(num)


##margin 14
num =0
for i in range (0,65536,2**11):
    for inner in range(0,2**10):
        num+= eqADD[i+inner]
margin.append(num)

##margin 15
num =0
for i in range (0,65536,2**12):
    for inner in range(0,2**11):
        num+= eqADD[i+inner]
margin.append(num)

print()
print( pairwise(0,1,1,0) + pairwise(0,1,0,0)+pairwise(0,1,1,1)+pairwise(0,1,0,1))


print(margin)

print(margins(1,0))


