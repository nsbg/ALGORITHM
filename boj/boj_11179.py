# Bronze 1

n = int(input())

convertedN = str(bin(n))[2:]
reversedN = convertedN[::-1]

print(int(reversedN, 2))