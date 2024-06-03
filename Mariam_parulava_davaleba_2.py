import random

#1

question = """რომელი იმპერიის მიერ აგებული წყალ-მომარაგების სისტემა (აკვედუკი) ფუნქციონირებს დღესაც?
სავარაუდო პასუხები:

1. შუმერთა
2. სელჩუკთა
3. რომის
4. მონღოლთა
"""
print(question)

rslt = int(input("შეიყვანე იმ პასუხის ნომერი რომელიც ფიქრობ რომ სწორია: "))

if rslt == 3:
    print("სწორია!")
else:
    print("არა! სწორი პასუხია რომის!")


#2

category = ['laptop', 'PC', 'phone']
print(category)

costumer = input("choose category: ").lower()
budget = int(input("gimme your maximum budget: "))

options = {"laptop": ["MacBook", "Dell", "Lenovo"], "pc": ["HP", "Dell", "Lenovo"], "phone": ["iPhone", "Samsung", "Google"]}

while budget > 1000:
    if costumer in options:
        chosen_option = random.choice(options[costumer])
        print(f"I chose this {costumer} for you {chosen_option}. break with sun!")
        break

else:
    print("unfortunately, you are broke! i cannot offer anything at the moment")


#3

print("Hey you are in a forest! Do you want to go 'left' or 'right'?")
choice = input("your answer here: ").lower()
if choice == "left":
    print("You see a wild animal. Do you 'fight' or 'run'?")
    choice = input("your answer here: ").lower()
    if choice == "fight":
        print("You win the fight and find a treasure. You win!")
    else:
        print("You run away safely. Game over.")
else:
    print("You come across a river. Do you 'swim' or 'build' a boat?")
    choice = input("your answer here: ").lower()
    if choice == "swim":
        print("You find a hidden cave with treasures. You win!")
    else:
        print("You build a boat and find a friendly village. You win!")


#4

print("You are in profession finder space!")
while True:
    print("Do you prefer 'indoors' or 'outdoors'?")
    location = input("your answer here: ").lower()
    if location == "indoors":
        print("Do you enjoy 'technology' or 'arts'?")
        interest = input("your answer here: ").lower()
        if interest == "technology":
            print("You could be a Software developer!")
        elif interest == "arts":
            print("You could be a Graphic designer!")
        else:
            print("Everything will be okay!.")
    elif location == "outdoors":
        print("Do you like 'nature' or 'adventure'?")
        interest = input("your answer here: ").lower()
        if interest == "nature":
            print("You could be a botanic!")
        elif interest == "adventure":
            print("You could be a Travel guide!")
        else:
            print("Everything will be okay!")
    else:
        print("Everything will be okay!")
    break
