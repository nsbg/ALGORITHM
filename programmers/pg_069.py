# Level 1

def solution(X, Y):
    answer = ''
    
    x = set(X)
    y = set(Y)
    z = list(x&y)

    intersection_dict = {key: min(X.count(key), Y.count(key)) for key in z}
    intersection_dict = dict(sorted(intersection_dict.items(), reverse=True))
    
    if len(intersection_dict) == 0:
        return '-1'    
    else:
        for key in intersection_dict.keys():
            answer += key*intersection_dict[key]
        
        if list(set(answer)) == ['0']:
            answer = '0'
            
    return answer