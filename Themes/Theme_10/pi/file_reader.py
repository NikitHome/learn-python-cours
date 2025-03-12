file_path = 'themes/theme_10/pi/pi_digits.txt'
with open(file_path) as file_object:
    contents = file_object.read()
    print(contents.rstrip())


file_path = 'themes/theme_10/pi/pi_digits.txt'
with open(file_path) as file_object:
    for line in file_object:
        print(line.rstrip())

file_path = 'themes/theme_10/pi/pi_digits.txt'

with open(file_path) as file_object:
    lines = file_object.readlines()
    
for line in lines:
    print(line.strip())
