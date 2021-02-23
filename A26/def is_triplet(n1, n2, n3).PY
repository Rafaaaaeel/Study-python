
try:
    num = int(input('Enter a number between 1 and 30: '))
    num1 = 30 / num
    if num > 30:
        raise ValueError(num)
except ZeroDivisionError as err:
    print(err, 'Yo cant divide by zero') 
except ValueError as err:
    print(err, 'bad value')
except:
    print('Invalid input')
else:
    print(f"30 divided by {num} is {num1}")
finally:
    print("**Thank you for playing!**")
