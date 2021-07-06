# Bronze 4

science = []
society = []

for _ in range(4):
    science.append(int(input()))

for _ in range(2):
    society.append(int(input()))

science = sorted(science, reverse=True)
print(sum(science)-science[-1]+max(society))