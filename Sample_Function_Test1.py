
def summ(x1, x2):
    z = x1 + x2
    return (z)

x1 = int(input("Enter the 1st number:"))
x2 = int(input("Enter the 2nd number:"))

result = summ(x1, x2)
print('Sum of ' +str(x1)+ ' & ' +str(x2) + ' = ' +str(result))

x = 30

def sample():
    x = 45
    print('Local Variable: ' + str(x))

sample()
print('Global Variable: ' +str(x))

def multi(*values):
    print(values)

def hi(name,age):
    print("My name is " +name +", My Age is " +age)

def hello():
    print('Hello')

hello()

value1 = input("Enter your name:")
value2 = input("Enter your age:")

hi(age = value2, name = value1)

multi('Today', 'Monday', 7725 )
