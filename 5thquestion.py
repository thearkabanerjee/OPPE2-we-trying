# # write a function to check if a domain ends with .com or .in

# def domainchecker (domain : str):
#     if (domain [-1:] == 'm'):
#         if (domain [-4 :]== '.com'):
#          return (f'{domain} ends with .com')
#         else:
#             return (f'{domain} doesnt end with .com')

#     elif (domain [-1:]== 'n'):
#         if (domain [-3:] == '.in'):
#             return (f'{domain} ends with .in')
#         else:
#             return (f'{domain} doesnt end with .in')
#     else:
#         return (f'{domain} ends with none of .com or .in')

# print (domainchecker ('www.arka.in'))

def domainchecker (domain : str):
    newdomain = domain.lower().strip()
    
    if (newdomain.endswith('.in')):
        return (f'{domain} ends with .in')
    elif (newdomain.endswith ('.com')):
        return (f'{domain} ends with .com')

    else : 
        return ('does not end with a .in or .com')

print (domainchecker('WWW.ARKA.COM'))
