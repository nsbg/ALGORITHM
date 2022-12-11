# Level 2(코드 지저분함)

import math

def solution(fees, records):
    car_number = {}
    car_time = {}
    
    for record in records:
        car_number[record.split()[1]] = 0
        
        if record.split()[1] not in car_time.keys():
            car_time[record.split()[1]] = [record.split()[0]]
        else:
            car_time[record.split()[1]].append(record.split()[0])

    for key, value in car_time.items():
        if len(value) % 2 != 0:
            car_time[key].append('23:59')
        
        total_hour = 0
        total_minute = 0
        
        for i in range(0, len(value), 2):
            minute = int(value[i+1].split(':')[1])-int(value[i].split(':')[1])
            
            if minute < 0:
                minute += 60
                hour = int(value[i+1].split(':')[0])-int(value[i].split(':')[0])-1
            else:
                hour = int(value[i+1].split(':')[0])-int(value[i].split(':')[0])
            
            total_hour += hour
            total_minute += minute
            
        total_time = (60*total_hour)+total_minute
        
        car_time[key] = total_time
        
        if car_time[key]-fees[0] > 0:
            car_number[key] = fees[1]+math.ceil((car_time[key]-fees[0])/fees[2])*fees[3]
        else:
            car_number[key] = fees[1]

    return list(dict(sorted(car_number.items())).values())