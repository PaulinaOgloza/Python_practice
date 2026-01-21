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

