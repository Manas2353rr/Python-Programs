def tribonacci(n):
    (a,b,c)=(0,1,1)
    for i in range(1,n+1):
        print(a,end='\t')
        a,b,c=b,c,a+b+c
def main():
    n=eval(input('enter a number'))
    tribonacci(n)
main()
