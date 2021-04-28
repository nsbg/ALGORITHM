# Silver 3
# 피보나치 수열과 동일

cnt = [0]*1000001

cnt[1] = 1
cnt[2] = 2

n = int(input())

for i in range(3, n+1):
    cnt[i] = (cnt[i-2]+cnt[i-1])%15746

print(cnt[n])