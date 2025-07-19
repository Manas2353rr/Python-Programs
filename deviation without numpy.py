a=[12,45,30,21,4,69,18]
sum=0

for i in a:
    sum+=i

mean=sum/len(a)
print('Arthmetic Mean=',mean)

sum=0
for i in a:
    sum+=(i-mean)**2

import math
stddev=math.sqrt(sum/len(a))
print('Standard Deviation=',stddev)
