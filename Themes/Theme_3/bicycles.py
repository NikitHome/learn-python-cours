bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles) 


# обращение к элементам списка 
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0]) 


bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0].title())


# индексы начинаются с 0, а не с 1
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[1])
print(bicycles[3])


bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[-1])


# использование отдельных элементов списка
bicycles = ['trek', 'cannondale', 'redline', 'specialized']

message = f'My first bicycle was a {bicycles[0].title()}.'

print(message)