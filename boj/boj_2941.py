croatian = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

word = input()

for w in croatian:
    word = word.replace(w, '.')

print(len(word))