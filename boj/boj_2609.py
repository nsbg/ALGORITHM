# Bronze 1

# 최대공약수
def GCD(a, b):
    while b > 0:
        a, b = b, a%b

    return a

# 최소공배수
def LCM(a, b, gcd_num):
    return (a*b)//gcd_num

m, n = map(int, input().split())

gcd = GCD(m, n)
lcm = LCM(m, n, gcd)

print(gcd, lcm, sep='\n')