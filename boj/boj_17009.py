# Bronze 4

apple = 0
banana = 0

for a in range(3, 0, -1):
    apple += a*int(input())

for b in range(3, 0, -1):
    banana += b*int(input())
    
if apple > banana:
    print("A")
elif apple < banana:
    print("B")
else:
    print("T")