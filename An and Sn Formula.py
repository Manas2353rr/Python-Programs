from math import *
a=eval(input('enter first term'))
n=eval(input('enter number of term'))
d=eval(input('enter difference'))
An=a+(n-1)*d
Sn=n/2*(2*a+(n-1)*d)
print('Last term=',An,'Sum of numbers=',Sn,end'\n') 
