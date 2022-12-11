# Level 1

def solution(id_list, report, k):
    answer = {key: 0 for key in id_list} 
    
    cnt = {key: 0 for key in id_list} # 신고당한 횟수
    mail = {key: [] for key in id_list} # 신고한 사람
    
    for i in list(set(report)):
        mail[i.split()[0]].append(i.split()[1])
        cnt[i.split()[1]] += 1

    for key, value in mail.items():
        for id in value:
            if cnt[id] >= k:
                answer[key] += 1
    
    return list(answer.values())