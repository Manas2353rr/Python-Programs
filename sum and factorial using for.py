n=eval(input('enter a number'))
sum=0
product=1
for i in range(1,n+1):
    sum=sum+i        #OR sum+=i
    product=product*i   #OR product*=i
print('Sum=',sum,'\nfactorial=',product)
