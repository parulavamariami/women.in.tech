"""1. შექმენი ფუნქცია, რომელიც მომხმარებლისგან მიღებულ ინფორმაციას გაასამმაგებს
და დაბეჭდავს შემდეგნაირად:
input: “word”
Output: „Tripled: wordwordword“
2. შექმენი ფუნქცია, რომელიც მიიღებს მომხმარებლის წონას და დააბრუნებს მის წონას
მთვარეზე. (მთვარის გრავიტაცია 6_ჯერ ნაკლებია დედამიწისაზე)
3. შექმენი კალკულატორის ფუნქცია, რომელიც მიიღებს გამოსახულებას
მომხმარებლისგან input() ფუნქციის დახმარებით (სამ მონაცემს _ პირველ რიცხვს,
მოქმედებას (+ - * / ^), მეორე რიცხვს)
მაგ. „2 * 6“ დათვლის და დააბრუნებს შედეგს. გაითვალისწინე რომ რიცხვის შეყვანის
მაგიერ სიმბოლოების შეყვანის შემთხვევაში უნდა დააბრუნოს ფუნქციამ შესაბამისი
მესიჯი. ასევე ნულზე გაყოფა არ შეიძ₾ება, ამ შემთხვევაშიც უნდა დააბრუნოს
შესაბამისი მესიჯი. (დააბრუნოს და არა დაპრინტოს)"""


#1

def print_three_times(somevalue):
    rslt = somevalue * 3
    print(rslt)

value = input("gimme something i will multiply it tree times: ")
print_three_times(value)

#2

def weight_in_the_moon():
    weight = int(input("put your weight and lets see how much it will be in the moon: "))
    print("if you are women, good news on the moon you will weight 6 times less")
    moon_result = weight / 6
    return f"in the moon your weight which was {weight} will be {moon_result}, congrats! you made it there."


output_1 = weight_in_the_moon()
print(output_1)

#3

def calculator_for_you():
    num1 = float(input("Please enter the first number: "))
    operator = input("Please enter the operator (+, -, *, /, ^): ")
    num2 = float(input("Please enter the second number: "))

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Error 404: are you dumb? no division by 0. try again!"
        result = num1 / num2
    elif operator == '^':
        result = num1 ** num2
    else:
        print("Error 404: what you need me to do. Please use one of +, -, *, /, ^.")
        return

    return f"The result of {num1} {operator} {num2} is: {result}"

print(calculator_for_you())