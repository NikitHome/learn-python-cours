import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'themes/theme_10/number/numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)