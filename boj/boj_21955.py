# Bronze 2

n = list(map(str, input()))

left = n[:len(n)//2]
right = n[len(n)//2:]

print(''.join(left), ''.join(right), end=' ')
