#check if a given year is a leap year

def leap_year_checker (year : int):
    if (year % 4 == 0) :
        return (f'{year} is a leap year')
    else:
        return (f'{year} is not a leap year')

# print (leap_year_checker(input ('Enter the year you want to check : ')))
# print (leap_year_checker(2024))
print (leap_year_checker(int (input('Enter a year you want to check : '))))



