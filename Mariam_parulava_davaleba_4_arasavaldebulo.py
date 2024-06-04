import random

# შექმენი while ციკლი, რომელიც მომხმარებელს ხუთჯერ შემოატანინებს ინფორმაციას და ჩაამატებს ცარიელ სიაში. შედეგი დაბეჭდე. (append მეთოდი)
user_info_list = []

for _ in range(5):
    user_info = input("Enter user information: ")
    user_info_list.append(user_info)
    user_info_list.append('')

print(user_info_list)

# მიღებული სიის პირველ და ბოლო ელემენტებს ადგილი შეუცვალე და დაბეჭდე შედეგი
user_info_list[0], user_info_list[-1] = user_info_list[-1], user_info_list[0]


print(user_info_list)

# წაშალე სიაში მომხმარებლის მიერ მოთხოვნილი ელემენტი. (remove მეთოდი)
user_requested_item = input("Enter the user information to remove: ")
user_info_list.remove(user_requested_item)

print(user_info_list)


# იპოვე სიის სიგრძე მინიმუმ ორი მეთოდით
length_method1 = len(user_info_list)

print("Length using len() function:", length_method1)

# მეორე მეთოდი
count = 0

for numb in user_info_list:
    count += 1

length_method2 = count

print("Length using a loop:", length_method2)

# ამობეჭდე სიის ყოველი ელემენტი მის ინდექსთან ერთად მინიმუმ ორი მეთოდით
for i in range(len(user_info_list)):
    print(f"Index: {i}, Value: {user_info_list[i]}")

# მეორე მეთოდი
index = 0

while index < len(user_info_list):
    print(f"Index: {index}, Value: {user_info_list[index]}")
    index += 1

# შეკრიბე ორი სია და დაბეჭდე შედეგი.
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = [list1[i] + list2[i] for i in range(len(list1))]

print("Result after adding the two lists:", result)

# შეასრულე იგივე ოპერაცია extend მეთოდის დახმარებით
list1.extend(list2)

print("Result after adding the two lists:", list1)

# გაამრავლე სია რიცხვზე და დაბეჭდე შედეგი
multiplier = 2
result_multi = [element * multiplier for element in user_info_list]

print("Result after multiplying the list by", multiplier, ":", result_multi)

# Slicing _ ის გამოყენებით შეაბრუნე სია და დაბეჭდე შედეგი
reversed_list = user_info_list[::-1]

print("Reversed list:", reversed_list)

# გააკეთე იგივე reverse მეთოდის გამოყენებით
user_info_list.reverse()

print("Reversed list using reverse() method:", user_info_list)

# მომხმარებელს შემოაყვანინე წინადადება და გადააქციე სიტყვების სიად
sentence = input("Enter a sentence: ")
words = sentence.split()

print("List of words:", words)

# დაწერე პროგრამა, რომელიც ცარიელ სიაში ჩაამატებს 10 შემთხვევითად შერჩეულ რიცხვს,რიცხვების დიაპაზონი შემოჰყავს მომხმარებელს
start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))
random_numbers = []

for _ in range(10):
    random_number = random.randint(start_range, end_range)
    random_numbers.append(random_number)

print("Randomly selected numbers:", random_numbers)

#მომხმარებელს შეაყვანინე სიტყვა, და თუ ეს სიტყვა მოიძებნა მოცემულ სიაში, ამობეჭდე მისი ინდექსი.
fruits = ["apple", "orange", "banana", "strawberry"]
search_word = input("Enter a word to search: ")

if search_word in fruits:
    index = fruits.index(search_word)
    print(f"The word '{search_word}' is found at index {index}.")
else:
    print(f"The word '{search_word}' is not found in the list.")

# შემთხვევითი რიცხვებით შექმენი სია, იპოვე მინიმალური და მაქსიმალური ელემენტი და დაბეჭდე. (min max ფუნქციები)
random_numbers_2 = [random.randint(0, 100)
                  for _ in range(10)]
min_element = min(random_numbers_2)
max_element = max(random_numbers_2)

print("Generated list with random numbers:", random_numbers_2)
print("Minimum element:", min_element)
print("Maximum element:", max_element)

# წაშალე სიის ბოლო ელემენტი, ამავე დროს ამოპრინტე წაშლილი ელემენტი და მიღებული სია. (pop მეთოდის გამოყენებით)
deleted_element = user_info_list.pop()

print("Deleted element:", deleted_element)
print("Resulting list after deletion:", user_info_list)

# დაითვალე სიაში არსებული კონკრეტული ერთნაირი ელემენტების რაოდენობა. (count მეთოდი)
specific_element = ''
count_specific_element = user_info_list.count(specific_element)

print(f"Number of occurrences of {specific_element}: {count_specific_element}")

# მომხმარებლის მიერ შემოყვანილი წინადადება გადააქციე სიად. შემდეგ ეს სია ელემენტებისგან გაასუფთავე და დაბეჭდე შედეგი. (clear მეთოდი)
sentence = input("Enter a sentence: ")
sentence_list = sentence.split()
sentence_list.clear()

print("Resulting list after clearing:", sentence_list)

# არსებულ სიაში ჩაამატე „third indexed“ ელემენტი მესამე ინდექსის ადგილას. (insert მეთოდი)
new_element = input("Enter the new element: ")
third_index = 2
sentence_list.insert(third_index, new_element)

print("Updated list:", sentence_list)