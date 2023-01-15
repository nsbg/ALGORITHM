from datetime import datetime

def solution(today, terms, privacies):
    answer = []
    
    terms_dict = dict()
    
    today_year, today_month, today_day = int(today.split('.')[0]), int(today.split('.')[1]), int(today.split('.')[2])
    
    for term in terms:
        terms_dict[term.split()[0]] = int(term.split()[1])
    
    for idx, privacy in enumerate(privacies):
        date = privacy.split()[0]
        date = date.split('.')
        
        month = int(date[1])+terms_dict[privacy.split()[1]]
        year = int(date[0])
        
        if month > 12:
            year += (month//12)
            
            if month%12 == 0:
                month = 12
                year -= 1
            else:
                month %= 12
        
        if int(date[2]) == 1:
            day = 28
            month -= 1
        else:
            day = int(date[2])-1
    
        if month == 0:
            month = 12
            
        if datetime(today_year, today_month, today_day) > datetime(year, month, day):
            answer.append(idx+1)

    return sorted(answer)