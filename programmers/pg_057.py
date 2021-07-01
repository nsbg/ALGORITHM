# Level 2

def solution(brown, yellow):
    y_w = 0
    y_h = 0
    
    for i in range(1, yellow//2+2):
        if yellow % i == 0:
            y_w = yellow // i
            y_h = yellow // y_w
        
        if y_w >= y_h and 2*(y_w+y_h+2) == brown:
            return [y_w+2, y_h+2]