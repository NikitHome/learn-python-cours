first_name = "ada"
last_name = "lovelace"

full_name = first_name + ' ' + last_name # можно складывать строки вот так
print(full_name)

full_name = f'{first_name} {last_name}' # так же можно складывать строки вот 
                                        # так, f-строки
print(full_name)

print(f"Hello, {full_name.title()}!") # f нужна для того что бы в тексте можно 
                                      # было вставить переменную 

message = f"Hello, {full_name.title()}!" # f-строки можно сохранять в переменной
print(message)
