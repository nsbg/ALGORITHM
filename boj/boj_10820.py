# Bronze 2

while True:
    try:
        lowercase, uppercase, number, blank = 0, 0, 0, 0

        input_string = input()

        for char in input_string:
            if char.islower():
                lowercase += 1
            elif char.isupper():
                uppercase += 1
            elif char.isdigit():
                number += 1
            elif char == ' ':
                blank += 1
                
        print(lowercase, uppercase, number, blank, sep=' ')
    except:
        break