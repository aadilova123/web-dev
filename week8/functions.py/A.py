def min(a,b,c,d):
    if(a>b):
        m=b
    if(a<b):
        m=a
    if(c >d):
        if(m<d):
                return m
        if(m>d):
                return d

a = int(input())
b = int(input())
c = int(input())
d = int(input())

print(min(a,b,c,d))

