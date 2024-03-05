#how to distinguish primitives types in input 
v1 = int(input('Input a number: ')) #if you dont put 'int()' it will read the number as a string type...
v2 = int(input('Input other number: '))
s = v1 + v2
print("The sum of {} and {} is {}!".format(v1,v2,s)) #...and here the "sum" would be ex.: v1=2 v2=1 s=21