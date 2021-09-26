# Bronze 1

import sys

N = int(int(sys.stdin.readline().rstrip()))

for i in range(N):
    words = sys.stdin.readline().split()
    
    print("Case #" + str(i+1) + ":", end=" ")
    
    for _ in range(len(words)):
        print(words.pop(), end=" ")