import sys
if len(sys.argv)!=3:
    print('Insufficient Arguements.Write addition.py val1 val2')
    sys.exit(1)

try:
    a=eval(sys.argv[1])
    b=eval(sys.argv[2])

    c=a+b
    print('Sum=',c)

except Exception as e:
    print('Exception Occured',e)
    
