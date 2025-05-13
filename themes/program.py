max = 0
min = 300
count = 0

N = int(input())

for i in range(N):
    car_speed = int(input())
    
    if car_speed > max:
        max = car_speed
        
    if car_speed < min:
        min = car_speed

    if car_speed <= 60:
        count += 1
        
print(max - min)
print(count)        
    