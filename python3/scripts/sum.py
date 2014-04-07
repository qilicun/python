'''
This function calculate the following equation.
L(x,n)=\\sum_{i=1}^{n}\\frac{1}{i}(\\frac{x}{1+x})^{i}
'''
import math
import sys
def Ln(x, n):
    sum = 0;
    for i in range(1, n+1):
        sum += (x/(1+x))**i/i
    return sum

def L(x):
    return math.log(1 + x)
    
if __name__=='__main__':
    print(__doc__)
    x = float(sys.argv[1])
    n = int(sys.argv[2])
    print(Ln(x,n), L(x), Ln(x,n)-L(x))
    
