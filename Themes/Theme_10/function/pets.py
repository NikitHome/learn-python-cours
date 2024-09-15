def describe_pet(animal_type, animal_name):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {animal_name.title()}.")
    
describe_pet('hamster', 'harry')
describe_pet(animal_type='dog', animal_name='willie')