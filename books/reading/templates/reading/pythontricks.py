# import webbrowser


pairs=[[1,2],[2,3],[4,5],[6,7]]


flat = []

for pair in pairs:
    for item in pair:
        flat.append(item)

print(flat)

flat= [item for pair in pairs for item in pair]
print(flat)






# pets=['cats','dogs','cheetah']

# claeaned=[pet for pet in pets if pet not in ['cats','chicken']]
# print(claeaned)

# names=['caleb','curry']
# full_name=''.join(names)
# print(full_name)


# print("What is your full name")
# fist_name,second_name=input().split()

# print(fist_name,second_name)

# age=34
# reputation=15

# if age >= 21 and reputation >=20:
#     print("admin")
# else:
#     print("standard user")

# pets=['cats','dogs','cheetah']


# print(list(set(pets)))

# def move_position(x,y,z):
#     print(f"moveing to {x} {y},{z}")



# move_position(10,20,30)

# print(list(range(90,100)))
# print(type(range))


# for i in range(10):
#     print(i)

# print(list(range(889)))

# has_cats=False

# for pet in pets:
#     print(pet)
#     if pet=="cat":
#         has_cats=True
#         break

# if has_cats:
#     print('nope')



# reputation=2
# status=None

# pets=['cats','dogs','cheetah']
# if 'cat' in pets:
#     print('Am done')
# else:
#     print('Does not exist! lol')

# if reputation > 15:
#     status='admin'
#     print('you are an admin')
# else:
#     print('You are a reglar user')
#     status

# status='admin' if reputation > 15 else "user"
# print(status)
# print('What is your reputation')
# data=input()
# reputationfunction(data)


# language=['c','c++','python','go','matlab']
# name="collins"

# for item in language:
#     print(item,end=" ")
# print('hello')

# print(f'{language} are my goals to learn this year {name}')
# # data=[]
# print(not data)
# print(data is None)
# def changelist(data):
#     data=['new']
# def changelistdata(data):
#     data[:]=['new']
# languages=['c++','java','go','python']

# print(languages)
# changelist(languages)
# print(languages)
# changelistdata(languages)
# print(languages)

# learnin=languages[:]
# print(learnin)
# data2=data1
# data2['Erin']=10

# print(id(data1),id(data2))
# print(data1,data2)

# data={'hello':5}
# print(id(data))
# # webbrowser.open('www.roseliancakes.co.ke')

# a,b=5,10

# print('\033[91mThis is a different color')

# print(5**5)
# print(round(10.6))
# my_bank=999_999
# print(my_bank)
# print('This is really owesome'
# 'i am getting there')
# data=[1,2,3] 
# print(data[::-2])

# print('youtube'.find('tube'))

# if 'you' in 'youtube':
#     print('youtube'.index('you'))
