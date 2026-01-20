"""
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

"""
Napisz kalkulator.

Input:

- Jakie działanie chcesz wykonać
- liczba_1
- liczba_2

Output: wynik działania
"""

type_of_calculation=input("Choose the type of calculation you would like to do (*,/ etc): ")
num1 = float(input("Insert first number:"))
num2 = float(input("Insert second number:"))

if type_of_calculation== "+":
    result = num1 + num
elif type_of_calculation== "-":
    result = num1 - num2
elif type_of_calculation== "*":
    result = num1 * num2
elif type_of_calculation== "/":
    result = num1 / num2
else:
    print(f"{type_of_calculation} is not a valid option")


print(f"{num1} {type_of_calculation} {num2}= {result}")








