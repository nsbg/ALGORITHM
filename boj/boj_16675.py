# Bronze 3

import sys

Ml, Mr, Tl, Tr = sys.stdin.readline().split()

if Ml != Mr and Tl != Tr:
    print("?")

# 민성이만 같은 거 내는 경우
elif Ml == Mr and Tl != Tr:
    if Ml == "R" and (Tl == "P" or Tr == "P"):
        print("TK")
    elif Ml == "S" and (Tl == "R" or Tr == "R"):
        print("TK")
    elif Ml == "P" and (Tl == "S" or Tr == "S"):
        print("TK")
    else:
        print("?")

# 태경이만 같은 거 내는 경우
elif Ml != Mr and Tl == Tr:
    if Tl == "R" and (Ml == "P" or Mr == "P"):
        print("MS")
    elif Tl == "S" and (Ml == "R" or Mr == "R"):
        print("MS")
    elif Tl == "P" and (Ml == "S" or Mr == "S"):
        print("MS")
    else:
        print("?")

# 둘 다 같은 거 내는 경우
else:
    if (Ml == "R" and Tl == "P") or (Ml == "S" and Tl == "R") or (Ml == "P" and Tl == "S"):
        print("TK")
    elif (Tl == "R" and Ml == "P") or (Tl == "S" and Ml == "R") or (Tl == "P" and Ml == "S"):
        print("MS")
    else:
        print("?")