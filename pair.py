from test import state, margin, eqADD

def pairwise(num1, num2,s1,s2):
    sum =0
    for i in range (0, 65536):
        if state[i, num1]== s1 and state[i ,num2] ==s2:
            sum += eqADD[i]

    return sum
