""" 1
Napisz program, który poprosi użytkownika o wpisanie liczby (całkowitej), a następnie przedstawi mu tą liczbę jako int i jako float

Input: liczba całkowita

Output:

- Liczba całkowita
- Float
"""

# number = input("Type in a number to see it and integer and float:")
#
# print(f"{int(number)} as an integer")
# print(f"{float(number)} as a float")

""" 2
Napisz kalkulator.

Input:

- Jakie działanie chcesz wykonać
- liczba_1
- liczba_2

Output: wynik działania
"""

# type_of_calculation=input("Choose the type of calculation you would like to do (*,/ etc): ")
# num1 = float(input("Insert first number:"))
# num2 = float(input("Insert second number:"))
#
# if type_of_calculation== "+":
#     result = num1 + num2
# elif type_of_calculation== "-":
#     result = num1 - num2
# elif type_of_calculation== "*":
#     result = num1 * num2
# elif type_of_calculation== "/":
#     result = num1 / num2
# else:
#     print(f"{type_of_calculation} is not a valid option")
#
#
# print(f"{num1} {type_of_calculation} {num2}= {result}")

""" 3
Napisz program, który sprawdzi, czy podana liczba jest parzysta

Input: Liczba całkowita

Output: String
"""

# num = int(input("Type a number:"))
#
# if num % 2 == 0:
#     print(f"{num} is even")
# else:
#     print(f"{num} is odd")

""" 4
Napisz program, który sprawdzi, czy liczba całkowita jest podzielna przez 3, lub 5, lub przez obie te liczby

Input: Liczba całkowita

Output: String
"""

# num= int(input("Choose a number: "))

# if num % 3 == 0 and num % 5 == 0:
#     print(f"{num} is divisible by 3 and 5.")
# elif num % 3 == 0:
#     print(f"{num} is divisible by 3 but not by 5.")
# elif num % 5 == 0:
#     print(f"{num} is divisible by 5 but not by 3.")
# else:
#     print(f"{num} is not divisible by 3 nor 5.")

# -solution2:

# num= int(input("Choose a number: "))
#
# div3= num % 3 == 0
# div5= num % 5 == 0
#
# print(
#     f"{num} is" +
#     ("divisible by 3 and 5" if div3 else
#      "divisible by 3 but not by 5" if div3 else
#      "not divisible by 3 nor 5" if div5 else
#      "not divisible by 3 nor 5") +
#     "."
# )


# -solution3:

# num= int(input("Choose a number: "))
#
# div3= num % 3 == 0
# div5= num % 5 == 0
#
# messages = {
#     (True, True): "divisible by 3 and 5",
#     (True, False): "divisible by 3 but not by 5",
#     (False, True): "divisible by 5 but not by 3",
#     (False, False): "not divisible by 3 nor 5"
# }
#
# print(f"{num} is {messages[(div3, div5)]}.")

""" 5
Napisz program, który zwróci informację na temat długości przekazanego tekstu

Input: String

Output: String
"""

# text = input("Type in your text: ")
# text_lenght = len(text)
#
# if text_length >1:
#     print(f"Your text had {text_length} characters.")
# elif text_lenght == 1:
#     print(f"Your text had 1 characters.")
# else:
#     print(f"Your text had no characters.")

# solution2:

# text = input("Type in your text: ")
# text_len = len(text)
#
# if text_length == 0:
#     print("Your text had no characters.")
# else:
#     print(f"Your text had {text_length} character{'s' if text_length != 1 else ''}.")

""" 6
Napisz program, który po przekazaniu 2 liczb zwróci informację, która z tych liczb jest większa

Input:

- Liczba
- Liczba

Output: String

Zadanie z plusem - napisz program, który przyjmie 3 liczby.
"""
#
# num1: int(input("Input your first number: "))
# num2: int(input("Input your second number: "))

# if num1 > num2:
#     print(f"{num1} > {num2}")
# else:
#     print(f"{num2} < {num1}")

# sol2:

# num1 = int(input("First number: "))
# num2 = int(input("Second number: "))
# num3 = int(input("Third number: "))
#
# largest = max(num1, num2, num3)
# print(f"The largest number is {largest}.")

"""sol3"""

# nums = [int(input("Number: ")) for _ in range(3)]
# nums.sort(reverse=True)  # sort descending
# print(f"{nums[0]} > {nums[1]} > {nums[2]}")


""" 7
Napisz program, który sprawdzi, czy przekazana liczba jest dodatnia

Input: Liczba

Output: String
"""


# num= float(input("State a number: "))
#
# print (
#     f"{num}" +
#     (" is a negative number." if num < 0 else " is a positive number" if num > 0 else  " is zero." )
# )

""" 8
Napisz program, który sprawdzi, czy przekazany rok jest przestępny

Każdy rok jest przestępny jeżeli:
* Jest podzielny przez 4,
* Ale nie jest podzielny przez 100,
* Chyba, że jest podzielny przez 400
"""

# user_year= int(input("Input your year: "))

# print(
#     f"{user_year}" +
#     (" is a leap year" if user_year % 4 == 0 and user_year % 100 != 0 or user_year % 400 == 0 else
#      " is not a leap year.")
# )

"""sol2"""

# user_year = int(input("Input your year: "))
#
# print(
#     f"{user_year} is a leap year."
#     if (user_year % 4 == 0 and user_year % 100 != 0) or (user_year % 400 == 0)
#     else f"{user_year} is not a leap year."
# )


"""sol3"""

# print(
#     (lambda y: f"{y} is a leap year."
#                if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)
#                else f"{y} is not a leap year.")
#     (int(input("Input your year: ")))
# )

""" 9
Sprawdź, czy przekazana liczba składa się z 3 cyfr. (Bez sprawdzania, czy przekazany ciąg znaków to tylko liczby).

Input: Liczba

Output: String
"""

# user_num = input("Input your number: ")
#
# print(
#     ("This number has 3 numbers." if len(user_num) == 3 else "This number has more than 3 numbers." if len(user_num) > 3 else "This number has less than 3 numbers.")
# )

""" 10 
Sprawdź, czy przekazany znak jest samogłoską. Samogłoski: `aeiouy`

Input: String

Output: String
"""

# letter = input("Input your letter: ")
#
# consonant= "aeiouy`"
#
# print (f"{letter} is a consonant." if letter in consonant else "is not a consonant.")


""" 11
Napisz program, który zmieni temperaturę podaną w stopniach Celsjusza na Fahrenheita

F = C * 9/5 + 32

Input: Liczba

Output: Liczba / String
"""
# try:
#     celsius_number= float(input("State temperature in Celsius: "))
#
#     fahrenheit_number= celsius_number * (9/5) + 32
#
#     print(f"{fahrenheit_number} F = {celsius_number} C.")
#
# except ValueError:
#     print("State temperature in Celsius.")

""" 12
Napisz program, który przyjmie 3 liczby i obliczy z nich średnią arytmetyczną

Input: Liczba, Liczba, Liczba

Output: Liczba / String
"""

# try:
#
#     numbers = input("Type 3 numbers separated by comma: ")
#     numbers = numbers.split(",")
#
#     numbers= [float(n) for n in numbers]
#     average = sum(numbers) / len(numbers)
#
#     print(f"Average for {numbers} is: {average}")
# except ValueError:
#     print("Invalid input: please state 3 numbers separated by comma.")







