def factorial(n):
    if n<=1:
        return 1
    else:
        return n*factorial(n-1)

def fibonacci(n):
    if n==0 or n==1:
        return n
    elif n>=2:
        return fibonacci(n-2)+fibonacci(n-1)

def main():
    a=eval(input('enter a number'))
    b=factorial(a)
    print('factorial is',b)
    m=eval(input('enter no. of terms to generate'))
    for i in range(1,m+1):
        print(fibonacci(i),end='\t')
    
main()

