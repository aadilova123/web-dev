from math import sqrt 
a=int(input()) 
b=int(input())
for x in range(a, b+1):
        if int(sqrt(x)) == sqrt(x):
          print(x)