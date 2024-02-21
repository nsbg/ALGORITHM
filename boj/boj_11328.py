# Bronze 2

def strfry(str1, str2):
    if sorted(str1) == sorted(str2):
        return True
    else:
        return False

N = int(input())

for _ in range(N):
    A, B = input().split()
    
    result = strfry(A, B)
    
    if result == True:
        print("Possible")
    else:
        print("Impossible")