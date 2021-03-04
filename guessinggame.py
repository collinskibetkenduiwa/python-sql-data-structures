print('Enter a number')
userinput=input()
numbers=(2,3,4,5,6,7,8,9)


for item in numbers:
    if item in int(userinput):
        print('You guessed it right')
    else:
        print('Try again')
