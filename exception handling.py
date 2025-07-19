try:    
    d=eval(input('Enter Displacement'))
    t=eval(input('Enter Time'))
    v=d/t
    print('Velocity=',v,'m/s')

except ZeroDivisionError as ze:
    print('Mistake you did:-Denominator cannot be Zero')

except NameError as ne:
    print('Please provide numerical valu-not the string')

except Exception as ex:
    print('Unknown Error',str(ex))

else:
    print('Thanks:Designed by Manas')