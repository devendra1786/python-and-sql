# # # # # # # # # # # # # def display_details(**kwargs):
# # # # # # # # # # # # #     return kwargs


# # # # # # # # # # # # # details = display_details(
# # # # # # # # # # # # #     name="Deva",
# # # # # # # # # # # # #     age=21,
# # # # # # # # # # # # #     course="Python",
# # # # # # # # # # # # #     city="Chennai"
# # # # # # # # # # # # # )

# # # # # # # # # # # # # print("Name:", details["name"])
# # # # # # # # # # # # # print("Age:", details["age"])
# # # # # # # # # # # # # print("Course:", details["course"])
# # # # # # # # # # # # # print("City:", details["city"])

# # # # # # # # # # # # # def multiply(a, b):
# # # # # # # # # # # # #     return a * b

# # # # # # # # # # # # # result = multiply(10, 5)

# # # # # # # # # # # # # print("Multiplication:", result)

# # # # # # # # # # # # # def is_even(number):
# # # # # # # # # # # # #     return number % 2 == 0

# # # # # # # # # # # # # result = is_even(10)

# # # # # # # # # # # # # print("Is the number even?", result)

# # # # # # # # # # # # # def is_even(number):
# # # # # # # # # # # # #     return number % 2 == 0

# # # # # # # # # # # # # # Calling the function with different numbers
# # # # # # # # # # # # # print("10 is even:", is_even(10))
# # # # # # # # # # # # # print("7 is even:", is_even(7))
# # # # # # # # # # # # # print("20 is even:", is_even(20))
# # # # # # # # # # # # # print("15 is even:", is_even(15))

# # # # # # # # # # # # # def add(a, b):
# # # # # # # # # # # # #     return a + b


# # # # # # # # # # # # # def subtract(a, b):
# # # # # # # # # # # # #     return a - b


# # # # # # # # # # # # # def multiply(a, b):
# # # # # # # # # # # # #     return a * b


# # # # # # # # # # # # # def divide(a, b):
# # # # # # # # # # # # #     return a / b


# # # # # # # # # # # # # # Calling the functions
# # # # # # # # # # # # # print("Addition:", add(20, 10))
# # # # # # # # # # # # # print("Subtraction:", subtract(20, 10))
# # # # # # # # # # # # # print("Multiplication:", multiply(20, 10))
# # # # # # # # # # # # # print("Division:", divide(20, 10))

# # # # # # # # # # # # # def add(a, b):
# # # # # # # # # # # # #     return a + b


# # # # # # # # # # # # # def subtract(a, b):
# # # # # # # # # # # # #     return a - b


# # # # # # # # # # # # # def multiply(a, b):
# # # # # # # # # # # # #     return a * b


# # # # # # # # # # # # # def divide(a, b):
# # # # # # # # # # # # #     return a / b


# # # # # # # # # # # # # # Call all four functions
# # # # # # # # # # # # # result1 = add(20, 10)
# # # # # # # # # # # # # result2 = subtract(20, 10)
# # # # # # # # # # # # # result3 = multiply(20, 10)
# # # # # # # # # # # # # result4 = divide(20, 10)

# # # # # # # # # # # # # # Display results with proper labels
# # # # # # # # # # # # # print("Addition:", result1)
# # # # # # # # # # # # # print("Subtraction:", result2)
# # # # # # # # # # # # # print("Multiplication:", result3)
# # # # # # # # # # # # # print("Division:", result4)


# # # # # # # # # # # # # message = "Hello Python"

# # # # # # # # # # # # # print(message)

# # # # # # # # # # # # # message = "DEVENDRA"

# # # # # # # # # # # # # print(message)

# # # # # # # # # # # # message = "DEVENDRA REDDY"

# # # # # # # # # # # # print(message[0])
# # # # # # # # # # # # print(message[1])
# # # # # # # # # # # # print(message[2])
# # # # # # # # # # # # print(message[3])
# # # # # # # # # # # # # print(message[4])

# # # # # # # # # # # message = "DEVENDRA"
# # # # # # # # # # # name = "REDDY"

# # # # # # # # # # # result = message + " " + name

# # # # # # # # # # # print(result)

# # # # # # # # # # message = "DEVENDRA "

# # # # # # # # # # result = message * 3

# # # # # # # # # # print(result)

# # # # # # # # # string1 = "I am learning"
# # # # # # # # # string2 = "Python & Sql programming."

# # # # # # # # # sentence = string1 + " " + string2

# # # # # # # # # print(sentence)

# # # # # # # # message = "DEVA "

# # # # # # # # result = message * 3

# # # # # # # # print(result)

# # # # # # # message = '''
# # # # # # # hello,

# # # # # # # This is
# # # # # # # deva.
# # # # # # # '''

# # # # # # # print(message)

# # # # # # message = """hello

# # # # # # This is
# # # # # # deva."""

# # # # # # print(message)

# # # # # name = "kamasani reddy"

# # # # # print("Original:", name)
# # # # # print("Uppercase:", name.upper())
# # # # # print("Lowercase:", name.lower())
# # # # # print("Title Case:", name.title())
# # # # # print("Capitalize:", name.capitalize())

# # # # sentence = "Python is easy to learn and Python is powerful."

# # # # # Find the position of a substring
# # # # position = sentence.find("Python")
# # # # print("Position of 'Python':", position)

# # # # # Count how many times a substring occurs
# # # # count = sentence.count("Python")
# # # # print("Number of times 'Python' occurs:", count)

# # # sentence = "Hello Devendra"

# # # words = sentence.split()

# # # print(words)

# # text = "Python123"

# # print(text.isalpha())   # False
# # print(text.isdigit())   # False
# # print(text.isalnum())   # True
# # print(text.islower())   # False
# # print(text.isupper())   # False

# words = ["I", "am", "Devendra"]

# sentence = " ".join(words)

# print(sentence)

filename = input("Enter a filename: ")

if filename.endswith(".py"):
    print("The file is a Python file.")
else:
    print("The file is not a Python file.")