# check if a number is prime

# when is a number a prime number

# when it is only divisible by 1 and the number itself
# only then we can say that the number is prime 

def primeChecker (num : int):
    # numberroot = int (num ** 0.5)
    for i in range (2, num):
        if (num % i == 0) :
            return (f'{num} is not a prime number')
        
    return f'{num} is a prime number'
    # # return numberroot

print (primeChecker(int (17)))