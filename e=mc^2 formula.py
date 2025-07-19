print('E=mc^2')
def Energy(m,c):
    return m*c**2
m=eval(input('Enter Mass in Kg'))
c=eval(input('Enter speed of light in m/s'))
e=Energy(m,c)
print('Energy=',e,'Joules')
