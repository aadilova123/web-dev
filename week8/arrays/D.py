N = int(input())

arr = list(map(int, input().split()))

answ = 0

for i in range (1, len (arr)):

   if arr[i] > arr[i-1]:

       answ += 1

print (answ)