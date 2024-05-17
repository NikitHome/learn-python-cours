alien_0 = {
    'color': 'green',
    'speed': 'slow',
    'points': 5,
}

alien_1 = {
    'color': 'blue',
    'speed': 'slow',
    'points': 10,
}

alien_2 = {
    'color': 'red',
    'speed': 'fast',
    'points': 15,
}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    for key, value in alien.items():
        print(f"{key}: {value}")