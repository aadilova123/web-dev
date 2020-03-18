n=int(input())
value=0
b=False
while value < n:
    value*=2
    if value == n:
        b=True
if b == True:
    print("YES")
else:
    print("NO")
