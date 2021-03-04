
# # object oriented programming

class Book():

    favorrites=[]
    def __init__(self,title,pages):
        self.title = title
        self.pages=pages

    def is_long(self):
        if self.pages >100:
            return True
        return False
    def __str__(self):
        return f"{self.title} is {self.pages} pages long"
    def __eq__(self,other):
        if self.title ==other.title and self.pages == other.pages:
            return True
        return False

book =Book("This is quite intresting",170)

file=open("input3.txt",'a')

file.write("Test")
file.write("Are you my mother? 72\n")
file.write("This is a data structures book,89")
# file.close()
# open("Input2.txt",'a')
open("input3.txt","a")
data=file.read().split('\n')
# file.close()

book1_data=data[0].split('t')
print(book1_data)
book1=Book(book1_data[0],book1_data[1])
book2=Book(book1_data[0],book1_data[1])
print(book1)
print(book2)
# def do_something_new(book):
#     book.title="This is a new book which the title as ben changed by a new function"

# do_something_new(book)

# print(book)
# book2=Book("This is a different book",23)

# print(id(book),)
# print(id(book2))




# def do_something(book):
#     print(id(book))
#     book.title="something new"


# do_something(book)

# print(book)

# book2=Book("This is quite intresting",170)


# print(id(book),id(book2))

# print(book == book2 )


# print(book.title)
# print(book.is_long())

# Book.favorrites.append(book)
# for b in Book.favorrites:
#     print(b.title)
# print(Book.favorrites)

# my_fav={"blue","white","green","maroon"}
# her_fav={"pink","purple","white","black"}



# only_me = my_fav - her_fav
# only_her =her_fav -my_fav

# print(only_her | only_me)

# print(only_me)

# wedding_colors=my_fav & her_fav

# print(wedding_colors)


# colors=['red','red','red','orange','orange','blue']

# count=[colors.count(color) for color in set(colors)]


# print(count)

# print(id(colors))
# sorted(colors)

# colors[:]=list(set(colors))

# print(id(colors))


# print(colors)


# conjuctions={"for","and","but","or","yet","so"}

# seen=set()
# # conjuctions ={"for ": 0,"and": 0,"nor":0,"or":0,"yet":0,"so":0}

# completely_original_poem="""“After the Sea-Ship—after the whistling winds;
# # After the white-gray sails, taut to their spars and ropes,
# # Below, a myriad, myriad waves, hastening, lifting up their necks,
# # Tending in ceaseless flow toward the track of the ship:
# # Waves of the ocean, bubbling and gurgling, blithely prying”"""


# data=completely_original_poem.split()


# for word in data:
#     if str.lower(word) in conjuctions:
#             seen.add(str.lower(word))



# print(seen)

        # conjuctions[str.lower(word)]+=1

# # print(data)


# for word in data:
#     if str.lower(word) in conjuctions:
#         conjuctions[str.lower(word)] += 1

# print(conjuctions)
 

# emails={'caleb' : "caleb@email.com",
#         'gal':"gal@email.com",
#         'collins':"collins@gmail.com"

# }


# for k,elem in emails.items():
#     print(k,elem)
# emails["Josh"]="J@email.com"

# emails.update({"irene":"irene@email.com","hildah":"Hildahcherotich@email.com"})

# print(emails)
# print(emails.get("Caleb","No user found"))
# if "collins" in emails:
#     print(emails["collins"])


# import utils

# print(utils.stats_range([1,3,10,40,4,3]))

# import random as r
# random =3.14
# print(random.randint(1,6))

# print(type(random))

# r.




# data =[[10,2,3],[10,4],[4,5000,6],[10]]


# def avg(data):
#     return sum(data) / len(data)

# print(sorted(data,key=avg))

# data2=[-1,-2,-1,-3,-4,1,2,3,4]

# print(sorted(data))

# sorted(data2,key=abs)

# print(data2)

# data["ball","amazon"]



# data=["This","is" ,"data"]

# d= " "

# print(d.join(data))

# d = " "

# print(data.split(d))


# grades=[[10,25,13,45],[205],[70,76,49,100]]


# def print_2d(grades):

#     for inner_list in grades:
#         for grade in inner_list:
#             print(grade, end="")
#     print()

# for i in range(len(grades)):
#     for j in range(len(grades[i])):
#         print(grades[i][j],end="")
#     print()

# print(grades[0])


# print("Enter yout favorite meal")
# print("Press q to quit and r to remove")

# favs=[]

# while True:
#     data=input()
#     if str.lower(data) == "q":
#         break
#     elif str.lower(data) =="r":
#         print("You are removing",favs.pop(0))
#     else:
#         favs.append(data)
#     print(favs)

# for food in favs:
#     print("You said", food)



# print("Enter your favorite meal")
# print("For example nyamachoma")
# print("Hit enter for ecah food and q to quit")

# favs=[]

# while True:
#     data=input()
#     if str.lower(data)=="q":
#         break
#     favs.append(data)

# for food in favs:
#     print("You said",food)

# data=input()

# favs=data.split()


# for food in favs:
#     print("You said" ,food)




# work_days=['Monday','Tuesday','Wednesday','Thursday','Friday']


# msg="Pay attention to everything i say"
# msglist=msg.split()
# print(msglist)

# random=['a','A','aa','AAA','HELLO','b','c','a']

# numbers=['1','2','3','4','-1','-2','-321','-221','-112','112']


# numbers.sort(key=str)

# print(numbers)


# random2=sorted(random,key=len)

# random.sort(key=len)
# print(random,random2)
# string=['a','A','abc','ABC','aBc','aBC','Abc']

# string.sort(key=str.lower)
# print(string)
 
# data=[1,32,54,34,65,11,100,-1,3]

# print(sorted(data,reverse=True))

# data.reverse()
# print(data)

# print(sorted(work_days))

# copy=work_days[:]
# copy.sort()
# print(copy)




# data=['a','b','c','d','e','f','g','h']

# data_reversed=[]

# for item in reversed(data):
#    data_reversed.append(item)

# print(data_reversed)
# for index in range(len(data) // 2):
#     data[index],data[-index-1]=data[-index-1],data[index]


# print(data)



# healthy=['kale chips','pizza']
# from collections import Counter
# backpack=['ugali','skuma','kale chips','pizza','ugali']
# Workdays=['Monday','Tuesday','Thursday','Friday']

# backpack2= backpack[:]

# print(id(backpack), id(backpack2))

# while backpack.count('ugali') > 0:
#     backpack.remove('ugali')

# print(backpack)
# Workdays.insert(2,'Wednesday')
# Workdays.remove('Friday')
# del Workdays[1]
# Workdays.pop(2)

# print(Workdays)


# counts=[backpack.count(item) for item in set(backpack)]
# print(counts)
# backpack2={'ugali','skuma','kale chips','pizza'}

# for item in backpack2:
#     print('i got ya')

# print(backpack,backpack2)

# print((backpack.count('pizza')))

# if backpack.count('pizza') < 2 :
#     backpack.append('pizza')


# print(backpack)
# print(id(backpack))
# # backpack[:]=[item for item in backpack if item in healthy]

# for item in backpack:
#     if item in healthy:
#         backpack.append(item)

# print(healthy)
# print(backpack)
# print(id(backpack))

# squares=[]

# for i in range(10):
#     squares.append(i**2)
# print(squares)

# print(len(['hello''goodmorning kenya']))