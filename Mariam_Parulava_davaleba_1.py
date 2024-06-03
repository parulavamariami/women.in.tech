#1

name = input("gimme your name: ")
surname = input("now surname as well: ")
age = input("you look young, how old are ya: ")
city = input("wow! so cool, which city you live in : ")

for_print = f""" I GOT HER/HIS INFO!

Name: {name} 
Surname: {surname}
Age: {age}
City: {city}"""

print(for_print)

#2

fruit1 = input("gimme fav fruit: ")
fruit2 = input("gimme N2 fav fruit: ")
fruit3 = input("now which one you just cannot: ")

print(fruit1,"//",fruit2,"%%",fruit3, sep="")

#3

write_poem_for_me = input("waiting to see your talent. write here poem for me: ")
print("Number of symbols:",len(write_poem_for_me))
print("I thought I was worth more than this!")