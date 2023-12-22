# Bronze 1

import sys

while True:
    input = sys.stdin.readline().strip()
    
    if input == '-1':
        break
    
    division = []
    
    for i in range(1, int(input)):
        if int(input)%i == 0:
            division.append(str(i))
    
    if sum(map(int, division)) == int(input):
        print(f"{input} = {' + '.join(division)}")
    else:
        print(f"{input} is NOT perfect.")