print('if elif else - Exercise')
# Create a calculator which handles +,-,*,/ and outputs answer based on the mode/ operator used
# Hint: use 3 separate inputs 
# Bonus: Extend functionality with extra mode so it also does celsius to fahrenheit conversion
# formula is: temp in C*9/5 + 32 = temp in f

def choose(num_1, t, num_2):
      if t == "*":
        answer_def = num_1 * num_2
      elif t == "+":
        answer_def = num_1 + num_2
      elif t == "-":
        answer_def = num_1 - num_2
      elif t == "/":
        answer_def = num_1 / num_2
      else:
        print('Try again')

      return answer_def

def conversion(number):
    return (number * 9 / 5 )+ 32

number_1 = int(input("Tell me a number: "))
number_2 = int(input("Tell me another number: "))
answer = input("Choose [*,/,+,-]")
number_c = input("Do you want to converte C to F? [Y/N] ")

if number_c == "Y":
    number_to_converte = float(input("Tell me the number for conversion"))
    print(conversion(float(number_to_converte)))
else:
    print("Ok another time")

print(choose(number_1, answer, number_2))


# Teacher solution

mode = input('Enter math operation(+,-,*,/) or f for Celsius to Fahrenheit conversion: ')
num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))

if mode == '+':
    print(f'Answer is: {num1 + num2}')
elif mode == '-':
    print(f'Answer is: {num1 - num2}')
elif mode == '*':
    print(f'Answer is: {num1 * num2}')
elif mode == '/':
    print(f'Answer is: {num1 / num2}')
elif mode.lower() == 'f':
    print(f'{num1} Celsius is equivalent to {(num1*9/5)+32 } fahrenheit')
else:
    print('Input error!')