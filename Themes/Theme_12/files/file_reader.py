with open('Themes/Theme_12/files/pi_digits.txt') as file_object:
    contents = file_object.read()
    contents = contents.strip()
print(contents)

with open('Themes/Theme_12/files/pi_digits.txt') as file_object:
    for line in file_object:
        print(line)

with open('Themes/Theme_12/files/pi_digits.txt') as file_object:
    lines = file_object.readlines()
    
for line in lines:
    print(line.strip())
