
file=open('input2.txt','r')

try:
    file.open('input.txt')
except OSError:
    print('Cannot open')
else:
    with file:
        print(file.readline()) 






# try:
#     open('input.txt','r')
#     print('Found the file')
# except FileNotFoundError as e:
#     print('Cannot find file')
# except Exception as e:
#     print('Something went wrong')