alien_0 = {}
print(f"{alien_0}\n")

alien_0 = { 
    'color': 'green', 
    'points': 5,
}

print(alien_0)
print(alien_0['color'])
print(f"{alien_0['points']}\n")

new_points = alien_0['points']
print(f"You just earned {new_points} points!\n")

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(f"{alien_0}\n")

alien_0['x_position'] = 5
print(f"{alien_0}\n")

del alien_0['points']
print(f"{alien_0}\n")