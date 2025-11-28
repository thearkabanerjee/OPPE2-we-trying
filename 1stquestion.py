# check if a number is an even 2 digit number 
# ignore the negative sign if there 

a : int = int(input ('Enter the number you want: '))
b : str = str (a)

if (len(b)== 2):
    # print (f"{a} is even")
    if (int (b) % 2 == 0):
        print (f'{a} is an even number')
    else:
        print (f'{a} is not an even 2 digit number')

elif (len(b)== 3):
    # if ()
    if (b[0]== '-'):
        # print ('works maybe')
        if (int(b[1:]))% 2 == 0 :
            print (f'{a} is an even number')
        else:
            print (f'{a} is not an even 2 digit number')
    else: 
        print (f'{a} is not an even 2 digit number')

else:
    print (f'{a} is not an even 2 digit number')