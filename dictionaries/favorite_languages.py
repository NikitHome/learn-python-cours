favorite_languages = {
    'jen': 'python',
    'sarah': 'c', 
    'edward': 'ruby',
    'phil': 'python',
}

language_item = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language_item}")

print("\n")



for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}")
    
print("\n")
    
    
    
for name in favorite_languages.keys():
    print(name.title())
    
print("\n")



for language in sorted(favorite_languages.values()):
    print(language.title())
    
print("\n")



for language in set(favorite_languages.values()):
    print(language.title())
    
print("\n")



friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")
        
        
        
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'], 
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")