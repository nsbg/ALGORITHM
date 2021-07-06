# Bronze 3

n= list(map(str, input().split()))

left = int(''.join(n[:2]))
right = int(''.join(n[2:]))

print(left+right)