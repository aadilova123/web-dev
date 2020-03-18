def xor(x,y):
        return bool(x and not y or not x and y)

for a in range(2):
    for b in range(2):
        print(a,b,int(xor(a,b)))
