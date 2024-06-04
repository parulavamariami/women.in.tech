"""1. ციკლის მეშვეობით 3 მომხმარებელს შეაყვანინე ინფორმაცია საკუთარი სახელის, გვარის და ასაკის შესახებ. თითოეული მომხმარებლის
ინფორმაცია შეინახე ინდივიდუალურ სიაში. შემდეგ კი სამივე სია დაამატე საერთო ცალრიელ სიას სახელად consumer_info. Input_ის
მეშვეობით მომხმარებლის ინდექსის შეყვანის შემთხვევაში პროგრამამ უნდა დაბრუნოს არჩეულ მომხმარებელზე ინფორმაცია შემდეგნაირად:

Name: Elene
Lastname: Khardava
Age: 21

2. შექმენი ჩაშენებული სია, რომელშიც იქნება შენახული ცნობილი მსახიობების შესახებ ინფორმაცია.მომხმარებელს შემოჰყავს მსახიობის
სახელი ან გვარი. თუ სიაში მოიძებნა მსახიობი, დაბეჭდe მის შესახებ არსებული ინფორმაცია რეზუმის სახით.

3. შექმენი ფუნქცია რომელიც მიიღებს სიას და დააბრუნებს ასევე სიას, თუმცა უნიკალური ელემენტებით (გამოიყენე set მონაცემთა ტიპი)

def unique_list():
...
return ...

4. შექმენი ფუნქცია რომელიც მიიღებს ორ set ტიპის მონაცემს, გააერთიანებს მათ, შემდეგ კი გადააქცევს tuple ტიპის მონაცემად და
დააბრუნებს შედეგს.

def set_to_tuple():
...
return ...

5. დაწერე პროგრამა, რომელიც შეამოწმებს გადაცემული ლექსიკონი არის თუ არა ცარიელი.

6. დაწერე პროგრამა რომელიც სტრიქონისგან ქმნის ლექსიკონს. დათვალე სტრიქონში კონკრეტული სიმბოლოს ოდენობა. მაგალითად
პროგრამას გადავეცით სტრიქონი: &#39;w3schools&#39; უნდა დააბრუნოს ლექსიკონი:

{&#39;w&#39;: 1, &#39;3&#39;: 1, ‘s&#39;: 2, ‘c&#39;: 1, ‘h&#39;: 1, &#39;o&#39;: 2, ‘l&#39;: 1}
"""

#1
def customer_info_system():
    names = []
    surnames = []
    ages = []
    customer_info = []

    for i in range(3):
        name = input(f"Enter name for customer {i + 1}: ")
        surname = input(f"Enter surname for customer {i + 1}: ")
        age = input(f"Enter age for customer {i + 1}: ")

        if age.isdigit():
            names.append(name)
            surnames.append(surname)
            ages.append(int(age))
        else:
            print("Invalid input for age. Skipping customer.")

    for i in range(len(names)):
        customer_info.append([names[i], surnames[i], ages[i]])

    for _ in range(3):
        index = input("Enter customer index (0, 1, 2): ")

        if index.isdigit() and 0 <= int(index) < len(customer_info):
            idx = int(index)
            customer = customer_info[idx]
            print(f"Name: {customer[0]}")
            print(f"Lastname: {customer[1]}")
            print(f"Age: {customer[2]}")
        else:
            print("Invalid index.")

customer_info_system()

#2

actors_info = [
    {"name": "Mariam", "surname": "Parulava", "age": 23, "movies": ["not", "really", "The actress"]},
    {"name": "some", "surname": "actor", "age": 65, "movies": ["good", "film"]},
    {"name": "Brad", "surname": "Pitt", "age": 58, "movies": ["Fight Club", "Ms&Mrs Smiths", "Once Upon a Time in Hollywood"]}
]

def search_actor(actor_name):
    for actor in actors_info:
        if actor_name.lower() in (actor['name'].lower(), actor['surname'].lower()):
            print(f"Name: {actor['name']} {actor['surname']}")
            print(f"Age: {actor['age']}")
            print("Movies:")
            for movie in actor['movies']:
                print("-", movie)
            return
    print("Actor not found.")

actor_name = input("Enter the name or surname of an actor: ")

search_actor(actor_name)

#3

def unique_list(input_list):
    return list(set(input_list))

original_list = [3, 0, 0, 1, 1, 1, 1]
print(unique_list(original_list))

#4

def set_to_tuple(set1, set2):
    combined_set = set(set1)
    for element in set2:
        combined_set.add(element)
    return tuple(combined_set)

set1 = {3, 0, 3}
set2 = {3, 2, 0}

print(set_to_tuple(set1, set2))

#5
def is_dict_empty(input_dict):
    print("The dictionary is empty."
          if not input_dict
          else "The dictionary is not empty.")

dictionary1 = {}
dictionary2 = {"key": "value"}

is_dict_empty(dictionary1)
is_dict_empty(dictionary2)

#6

def count_characters(string):
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

input_string = 'MariamParulava'
result = count_characters(input_string)
print(result)

