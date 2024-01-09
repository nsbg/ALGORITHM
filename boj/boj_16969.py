# Silver 5

import sys

car_format = sys.stdin.readline().strip()

if car_format[0] == "c":
    result = 26
else:
    result = 10

for i in range(1, len(car_format)):
    if car_format[i] == "c":
        if car_format[i-1] == "c":
            result *= 25
            result %= 1000000009
        else:
            result *= 26
            result %= 1000000009
    
    if car_format[i] == "d":
        if car_format[i-1] == "d":
            result *= 9
            result %= 1000000009
        else:
            result *= 10
            result %= 1000000009

print(result)