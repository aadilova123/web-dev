def swapPositions(list, pos1, pos2): 
      
    list[pos1], list[pos2] = list[pos2], list[pos1] 
    return list

s=int(input())
arr=list(map(int,(input()).split()))
swapPositions(arr, 0, s)
    