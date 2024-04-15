motorcycles = [] # пустой список
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati' # так можно изменить элемент списка
print(motorcycles)

motorcycles.append('honda') # добавление элемента в конец список
print(motorcycles)

motorcycles.insert(0, 'yamaha2') # вставка элемента в список
print(motorcycles)

del motorcycles[0] # удаление элемента списка по индексу
print(motorcycles)

motorcycles.remove('suzuki') # удаление элемента списка по значению 
print(motorcycles)