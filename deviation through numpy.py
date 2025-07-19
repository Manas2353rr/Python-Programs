#Correct way to find out mean and standard deviation
import numpy #Step I
#Step II: create a list withe certain items
a=[12,45,30,21,4,67,19] # 7 elements
#Step III: Use built-in mean and std function of numpy
mean=numpy.mean(a)
stddev=numpy.std(a) #Abstraction - Using factility without internal code logic
print('Mean=' , mean, '\n','Standard Deviation=' , stddev)
