# Bronze 2

# start-current
current = list(map(int, input().split(":")))
start = list(map(int, input().split(":")))

hour = start[0]-current[0]
min = start[1]-current[1]
sec = start[2]-current[2]

if sec < 0:
    sec += 60
    min -= 1

if min < 0:
    min += 60
    hour -= 1

if hour < 0:
    hour += 24

if sec < 10:
    sec = '0'+str(sec)

if min < 10:
    min = '0'+str(min)

if hour < 10:
    hour = '0'+str(hour)



print(hour, min, sec, sep=":")