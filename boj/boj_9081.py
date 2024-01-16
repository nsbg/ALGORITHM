# Silver 1, next_permutation 알고리즘

import sys

def next_permutation(s):
    arr = list(s)
    
    i = len(arr)-2
    
    while i >= 0 and arr[i] >= arr[i+1]:
        i -= 1
    
    if i < 0:
        return False
    
    j = len(arr)-1
    
    while arr[j] <= arr[i]:
        j -= 1
    
    arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1:] = reversed(arr[i + 1:])
    
    return ''.join(arr)

T = int(sys.stdin.readline().strip())

for _ in range(T):
    word = sys.stdin.readline().strip()
    
    if next_permutation(word) == False:
        print(word)
    else:
        print(next_permutation(word))