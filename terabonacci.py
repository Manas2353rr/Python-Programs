def terabonacci(n):
    (a,b,c,d)=(0,1,1,2)
    for i in range(1,n+1):
        print(a,end='\n')
        a,b,c,d=b,c,d,a+b+c+d


def main():
    n=eval(input('enter a number'))
    terabonacci(n)

main()
