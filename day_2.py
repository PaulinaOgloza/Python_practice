"""
    Sposób na sprawdzenie wbudowanych metod w Pythonie

    W celu sprawdzenia dostępnych metod na obiekcie możemy skorzystać z funkcji `help()`
"""
# print(help(str)) # Wypisz dostępne metody dla obiektu `str()`

"""
    Przykłady wbudowanych metod:

    'tekst'.capitalize()
    'tekst'.upper()
    'tekst'.lower()
    'tekst'.count('t')
    'tekst'.find('tek')
"""
# print(help(str.capitalize)) # Można sprawdzić konkretne metody
# print('tekst adfas'.capitalize())
# print('tekst'.upper())
# print('TEKST'.lower())
# print('tekst'.count('t'))
# print('tekst'.find('ks'))
# print('tekst tekst'.title())

"""
    Wbudowane funkcje `min()`, `max()`

    Można je stosować nie tylko na stringach, ale też na strukturach danych.
"""
# print(min("tekst"))
# print(max("tekst"))

"""
    Operacje na stringach.
"""
# name = "Jarek"
# last_name = "Majka"
# print(f"Imię: {name}, Nazwisko: {last_name}") # Preferowany sposób
# print("Imię: " + name + ", Nazwisko: " + last_name)
# print(name * 4)

"""
    Wyciągnięcie poszczególnych znaków za pomocą indeksów

    Pierwszy znak = 0
    Ostatni znak = -1
"""
# print(name[0]) # Pierwszy znak
# print(name[-1]) # Ostatni znak
# print(name[0:4]) # Pierwszy do czwartego znaku
# print(name[20]) # Błąd
# print(name[::-1]) # Odwrócenie tekstu

                                                    # ZADANIA

""" 1
    Napisz program, który pobierze od użytkownika jego imię i nazwisko,
    a następnie:

    Wypisze imię i nazwisko wielkimi literami.

    Wypisze imię z wielką literą na początku, a nazwisko małymi literami.

    Sprawdzi, ile razy litera "a" występuje w imieniu i nazwisku razem.
"""

# first_name = (input("State your first name: ")).lower()
# last_name = (input("State your last name: ")).lower()
#
#
# full_name = first_name.upper() + " " + last_name.upper()
# print(full_name)
#
# full_name = first_name.title() + " " + last_name.lower()
# print(full_name)

# a_in_name = 0
#
# for n in full_name.lower():
#     if n == "a":
#         a_in_name +=1
#
# print(a_in_name)

"""sol2"""

# a_in_name= full_name.lower().count("a")
#
# print(a_in_name)


""" 2
    Pobierz od użytkownika jego pełne imię i nazwisko.

    Sprawdź, czy w imieniu lub nazwisku znajduje się ciąg znaków "ek".

    Jeśli tak, wypisz komunikat: "Znaleziono frazę 'ek' w imieniu/nazwisku".

    Jeśli nie, wypisz: "Frazy 'ek' nie znaleziono".
"""


# full_name = input("State your full name: ")
# print(
#     f"Found 'ek' in phrase." if  "ek" in full_name.lower() else f"'ek' not found in phrase.",
# )


""" 3
    Pobierz imię i nazwisko użytkownika. Następnie:

    Sprawdź, które z nich jest dłuższe, wypisz które i podaj jego długość.

    Jeśli długość imienia i nazwiska jest taka sama, wypisz komunikat:
        "Imię i nazwisko mają taką samą długość".
"""

# full_name = (input("State your full name: ")).lower()
#
# name_split = full_name.split(" ")
#
# most_characters = 0
# longest_word = []
#
# for word in name_split:
#     word_length = len(word)
#     if word_length > most_characters:
#         most_characters = word_length
#         longest_word = [word]
#     elif word_length == most_characters:
#         longest_word.append(word)
#
# if len(longest_word) == 1 :
#     print(f"{longest_word[0]} is the longest word it has {most_characters} characters.")
# else:
#     word_str = ", " .join(word.title() for word in longest_word)
#     print(f"All longest words are the same length ({most_characters} characters): {word_str}")

"""sol2"""

# full_name = (input("State your full name: ")).lower()
#
# name_split = full_name.split(" ")
#
# most_characters = max(len(word) for word in name_split)
# longest_word = [x for x in name_split if len(x) == most_characters]
#
#
# if len(longest_word) == 1 :
#     print(f"{longest_word[0]} is the longest word it has {most_characters} characters.")
# else:
#     word_str = ", " .join(word.title() for word in longest_word)
#     print(f"All longest words are the same length ({most_characters} characters): {word_str}")

""" 4
    Napisz program, który będzie prosił użytkownika o wpisanie dowolnego słowa.

    Program powinien wypisywać to słowo wielkimi literami.

    Następnie zapyta użytkownika, czy chce kontynuować (wpisując "tak" lub "nie").

    Jeśli użytkownik wpisze "tak", program poprosi o kolejne słowo.

    Jeśli wpisze "nie", program zakończy działanie i wypisze "Do zobaczenia!".

    Wykorzystaj:
    * pętlę `while`
    * `input()`
    * wbudowaną metodę w `str()`, która zmieni litery na wielkie
"""

# user_word = (input("Enter a word: ")).upper()
#
# continue_answer = (input("Do you want to continue? (y/n): ")).title()
#
# while continue_answer == "Y" or continue_answer == "Yes":
#  next_answer = input("Enter next word: ").upper()
#  continue_answer = (input("Do you want to continue? (y/n): ")).title()
#
# print("Thank you  for your answers(s).")


"""sol2"""

# continue_answer = "Yes"
# loop_counter = 0
#
# while continue_answer in ["Yes", "Y"]:
#  user_word = (input("Enter a word: ")).upper()
#  print(user_word)
#  loop_counter += 1
#  continue_answer = (input("Do you want to continue? (y/n): ")).title()
#
# print(loop_counter)
#
# if loop_counter == 1:
#  print("Thank you  for your answers.")
# else:
#  print("Thank you for your answers.")


""" 5
    Pobierz od użytkownika jego imię.

    Następnie poproś go o zgadywanie liter, które znajdują się w jego imieniu.

    Jeśli poda literę, która występuje w imieniu, wypisz: „Brawo! Litera X jest w twoim imieniu.”

    Jeśli poda literę, której nie ma, wypisz: „Niestety, litery X nie ma w twoim imieniu.”

    Program działa w pętli, dopóki użytkownik nie wpisze "exit".
"""

# user_name= (input("State your name: ")).lower()
#
# user_letter= ""
#
# while user_letter != "exit":
#  user_letter = input("Guess a letter in your name (or type 'exit' to quit): ").lower()
#
#  if user_letter == "exit":
#   print("Goodbye!")
#  elif user_letter in user_name:
#   print(f"Brawo! Litera {user_letter} jest w twoim imieniu.")
#  else:
#   print(f"Niestety, litery {user_letter} nie ma w twoim imieniu.")



""" 6
    Problem Collatza
    https://pl.wikipedia.org/wiki/Problem_Collatza

    Weźmy dowolną dodatnią liczbę naturalną c0.
    Jeśli jest ona parzysta, to niech c1 = c0 / 2
    w przeciwnym wypadku niech c1 = 3 * c0 + 1.

    Następnie z liczbą c1 postępujemy podobnie jak z c0 i kontynuujemy ten proces.

    Przedmiotem problemu jest przypuszczenie, że niezależnie od jakiej liczby
    c0 wystartujemy, w końcu dojdziemy do liczby 1
"""

# our_number= int(input("Enter a positive integer: "))
#
# while our_number != 1:
#     if our_number % 2 == 0:
#      our_number = our_number // 2
#     else:
#         our_number = our_number * 3 + 1
#
# print(our_number)


""" 7 (4_1)
    Napisz program, który poprosi użytkownika o wpisanie dowolnego słowa.

    Program powinien przeiterować po tym słowie i do każdej litery dodać literkę "b",
    a następnie wypisać wynik na ekranie.
"""

# word = (input("Type a word:")).lower()
# new_word = ""
#
# for x in word:
#     new_word += x + "b"
#
# print(new_word.title())

"""sol2"""

# word = (input("Type a word:")).lower()
# new_word = "".join (x + "b" for x in word)
# print(new_word)

""" 8 (4_2)
    Napisz program, który:

    Wypisze liczby od 10 do 100 co 10 za pomocą pętli for i range().

    W każdym kroku pętli powinien pojawić się komunikat: "Aktualna liczba to: X".
"""

# for number in range(10, 101, 10):
#     print(number)

""" 9 (4_3)
    Napisz program, który:

    Pobierze od użytkownika dowolny tekst.
    Za pomocą pętli for zliczy, ile samogłosek (a, e, i, o, u, y) znajduje się w tym tekście.
    Wypisze wynik w konsoli.

    Podpowiedź:
    1. Skorzystaj ze zmiennej, która przechowa ilość `widzianych` samogłosek
"""

# user_text= (input("Enter text:")).lower()
#
# vowels = {}
#
# for x in user_text:
#     if x in "aeiou":
#         if x in vowels:
#             vowels[x] += 1
#         else:
#             vowels[x] = 1
#
# print(vowels)



""" 10 (4_4)
    Napisz program, który:

    Użyje for i range() do odliczania od 10 do 0.

    Po każdej liczbie wypisze "...", a na końcu "Start!".
"""

# for x in range(10,-1,-1):
#     if x > 0:
#         print(f"...{x}")
#     else:
#         print("Start!")

"""sol2"""
#
# countdown= [f"...{x}" for x in range(10,-1,-1)]
# print(countdown)
# countdown.append("Start!")
# print(countdown)
#
# for x in countdown:
#     print(x)


import random

liczba = random.randint(1, 10)

""" 11 (5_1)
    Funkcja `randint()` losuje liczbę z przekazanego zakresu, w powyższym od 1 do 10.
    Nie jest zbyt często wykorzystywana, więc nie musicie się jej uczyć, warto po prostu o niej pamiętać.
"""

"""
    Odgadnij liczbę

    Program losuje liczbę z zakresu 1-10.

    Użytkownik ma zgadywać liczbę.

    Jeśli poda poprawną wartość, pętla kończy się (break).

    Jeśli nie, program prosi o kolejną próbę.

    ZADANIE DODATKOWE:
    Policz ile prób miał użytkownik i zwróć informację na koniec działania programu.

    ZADANIE DODATKOWE 2:
    Podaj użytkownikowi informację, czy liczba jest większa, czy mniejsza niż podana przez niego.
"""

# user_number = liczba +1
# try_counter = 0
#
# while liczba != user_number:
#     try:
#         user_number = int(input("Guess a number between 1 and 10: "))
#         try_counter += 1
#         if liczba == user_number:
#             print("You got it right.")
#         else:
#             if liczba > user_number:
#                 print(f"Please try again. {user_number} is bigger that that number.")
#             elif liczba < user_number:
#                 print(f"Please try again. {user_number} is smaller that that number. ")
#     except ValueError:
#         print("That was not a number.")
#
# print(f" You tried {try_counter} times.")


""" 12 (5_2)
    Pomijanie liter

    Pobierz od użytkownika słowo.

    Wypisz je litera po literze, ale pomiń wszystkie samogłoski (a, e, i, o, u, y).

    Użyj continue, aby pominąć drukowanie samogłosek.
"""

user_word= input("Type a word: ").lower()
i= 0

while i < len(user_word):
    letter= user_word[i]

    if letter not in "aeiou":
        i += 1
        continue







