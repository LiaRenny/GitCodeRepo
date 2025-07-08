a = int(input('Enter a number'))

#Even or Odd Number
if (a%2==0):
    print('The Entered Value: ' +str(a) +' is a Even Number')
else:
    print('The Entered Value: ' + str(a) + ' is a Odd Number')

#Positive or Negative Number
if a<0:
    print("The Entered Value: " + str(a) +" is a Negative Number")
elif a==0:
    print("It's Zero")
else:
    print("The Entered Value: " + str(a) +" is a Positive Number")

