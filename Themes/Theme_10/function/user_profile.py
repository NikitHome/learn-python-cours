def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_info = build_profile('albert', 'einstain', 
                          location='princeton', 
                          field='physic')

print(user_info)