# i got to try some interesting commands on python



try:
    number : int = int (input ('enter the number'))
    print (1/number)

except ZeroDivisionError :
    print ("You can't divide by Zero . Idiot")

except ValueError:
    print ('Enter only numbers please: ')
finally:
    print ('')
