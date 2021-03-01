#DataTypes

number_int = 10 #int

number_float = 10.5 #float

string = 'name' #string

Boolean = true or false # boolean

a="it's"
b='it\'s'  #escape 

type(number_int) #The answer is i <class 'int'>
type(number_float) #The answer is <class 'float'>
type(string) #The answer is <class 'str'>
type(boolean) #The answer is <class 'bool'>

#Using 'str' to convert
#using 'int' to convert

#example

a = int(1)        # a will be 1
b = int(2.5)      # b will be 2
c = int("3")      # c will be 3
#c1 = int("3.4")   # c1 will be... ERROR
d = float(1)      # d will be 1.0
e = float(2.5)    # e will be 2.5
f = float("3")    # f will be 3.0
g = float("4.23") # g will be 4.23
h = str("80s")    # h will be '80s'
i = str(22)       # i will be '22'
j = str(3.01)     # j will be '3.01'

print([a,b,c,d,e,f,g,h,i,j])

#the solution of this #c1 = int("3.4") is:

c1 = int(float("3.4"))   # Now the answer will go a be 3