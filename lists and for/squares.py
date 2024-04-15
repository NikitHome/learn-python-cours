squares = []
for value in range(1, 11):
    square = value**2 # ** - степень
    squares.append(square)
print(squares)

squares = [value**2 for value in range(1, 11)] # генератор списка
print(squares)
