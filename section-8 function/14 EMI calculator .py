# formula to calculate EMI is : P x R X (1+R)^N / [(1+R)^N-1]

def emi_calculator(principal,rate,time):
    r = rate/12/100
    emi = (principal * r * (1+r)**time) / ((1+r)**time - 1)
    return emi

print(emi_calculator(500000,8.75,240))