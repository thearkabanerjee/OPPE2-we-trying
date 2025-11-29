D = {'Anita': 23, 'Ashwin': 43,
     'Ahana': '24',
     'Adarsh': 30, 'Archana': 15}
try:
    # iterates through the keys from left to right
    for key in D:
        value = D[key]
        if type(value) == str:
            raise 'Error'
        print(f'{key}:{value}')
except:
    print("Values cannot be strings")