# A Narcissistic Number (or Armstrong Number) is a positive number
# which is the sum of its own digits, each raised to the power of
# the number of digits in a given base. In this Kata, we will 
# restrict ourselves to decimal (base 10).

# For example, take 153 (3 digits), which is narcissistic:

#     1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
# and 1652 (4 digits), which isn't:

#     1^4 + 6^4 + 5^4 + 2^4 = 1 + 1296 + 625 + 16 = 1938
# The Challenge:

# Your code must return true or false (not 'true' and 'false') depending upon whether the given number is a Narcissistic number in base 10.

# This may be True and False in your language, e.g. PHP.

# Error checking for text strings or other invalid inputs is not required, only valid positive non-zero integers will be passed into the function.

# def narcissistic( value ):
#     lenofnumber = str (value)
#     lennum = len (lenofnumber)
#     for i in range (lennum):
#         return (sum (value[i] * lenofnumber))
    
    
# print (narcissistic (1254))


def narcissistic (value):
    strofnumber = str (value)
    lenofnumber = len (strofnumber)

    for i in range (lenofnumber):
        # return strofnumber[i]
        
        new_num = int(strofnumber[i]) ** lenofnumber
        
        sumofthing = 0 

        # sumofthing += new_num

        return new_num
        


print (narcissistic (1234))
        

# a = 124

# lenofnumber = str(a)

# lennum = len (lenofnumber)
# for i in range (lennum):
#     print (lenofnumber[i])



