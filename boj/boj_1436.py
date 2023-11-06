# Silver 5
# 716ms, 효율적인 코드는 아닌 듯

def check_consecutive_six(num):
    if '666' not in str(num):
        return False
    else:
        return True
        
N = int(input())

check, result = 0, 0

idx = 666

while True:
    if check_consecutive_six(idx):
        check += 1
     
    if check == N:
        result = idx
        break
    
    idx += 1
    
print(result)