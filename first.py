a = 5
b = 12

print("suma a i b wynosi: ",a + b)
print(b)

# tak się robi komentarze w python!!!!

a = 5 # tak się deklaruje liczby całkowite
b = 4.3 # tak się deklaruje liczby z,iennoprzecinkowe (Float)
znaki = 'deklaracja znaków' # tak się deklaruje znaki (string)

# jak rozwiązać problem z zapisywaniem pojedyńczego lub podwójnego cudzysłowu?
# przykładowe zapisy
znakiZCudzyslowem = "deklaracja 'pojedyńczego cudzysłowa"
znakiZPodwojnymCudzyslowem = "deklaracja \" podwojnego cudzyslowa"

#a jak sprawdzić typ zmiennej?
sprawdzenieTypu = type(znakiZCudzyslowem)

# typy zmiennych bool, czyli prawa lub fałsz, przykład deklaracji
deklaracjaPrawdy = True

#operatory arytmetyczne
# generalie wszystko jest praktycznie jak w innych językach, python może dodatkowo potęgować 
# z marszu 
przykladpotegowania = 2 ** 5
dzielenieZZaokragleniemWdol = 11 // 4 # tutaj wynik wyjdzie 2.75 ale zaokragli w dol do 2
# teraz jak zrobić modulo
testmodulo = 11 % 5 # tutaj reszta z dzielenia zostanie 1
testmodulo2 = 13 % 5 # tutaj reszta z dzielenia to 3, bo wejdą dwie pełne 5 i zostanie 3

#teraz robienie pierwszego programu
cenaNettoJava = 10
cenaNettoJS = 20
stawkaVat = 1.23

cenaBruttoJava = cenaNettoJava * stawkaVat
cenaBruttoJS = cenaNettoJS * stawkaVat

#różne sposoby zapisywania danych:
pierwszyPrzyklad = 1; drugiPrzyklad = 2; trzeciPrzyklad = 3 #mało stosowany przyklad
pierwszyP2, drugiP2, trzeciP2 = 1, 2, 3 # częściej stosowany i czytelniejszy
pierwszyP3 = drugiP3 = trzeciP3 = 1 # tak można przypisac jedną wartośc pod trzy zmienne odrazu

#przypisywanie nazywamy inicjalizacją
#operatory przypisania
testPrzypisania = 4
testPrzypisania += 4
# teraz testPrzypisania powinno wynosić 8

dlugiString = """ to jest dłigi string, to jest dłigi string,to
 jest dłigi string,to jest dłigi string,to jest dłigi string,"""
# tak sie zapisuje dlugi string, któru może być wyświetlony w kilku liniach np. 

#działania na zmiennych typu string
imie = "Marta"
print(imie[4])
print(imie[-1]) # tak możemy pobrać ostatnią literę słowa bez znania długości całego ciągu znaków

#usuwanie ostatniego elementu
print(imie[:-1])
print(imie[1:-1]) # usuwa pierwszy i ostatni element
print(imie[1:-1])

#importowanie bibliotek
import math
print(math.sqrt(9)) # funkcja z biblioteki math robi pierwiastek z 9

from math import sqrt
print(sqrt(16)) # wyciągnięcie z math konkretnej funkcji,żeby nie przepisywać wiele razy, choć mało stosowane, lepiej wyciągać z math


imieMoje = "patryk"
print(imieMoje.capitalize()) # zmienia moje imię na dużą literę
print(imieMoje) # teraz należy pamiętać, że imię zostanie takie jak było, bo nie przepisałem nowej wartości, a poprzedni print działał na kopii

imieMoje = imieMoje.capitalize() # teraz przypisuje nowa wartość
print(imieMoje) # teraz wyświetli mi zmienioną wartość

#pobieranie i formatowanie danych od użytkownika (służy do tego funkcja Input)
# nowyInput1 = input()
# nowyInput2 = input() # teraz należy pamiętać, że jak wpiszemy liczbe to beszie string
# dlatego należy zastosować rzutowanie

# nowyInput1 = int(input("Podaj pierwszy składnik "))
# nowyInput2 = int(input("Podaj drugi składnik "))
# print("Wynik dodawania to: " + str(nowyInput1 + nowyInput2))
# print("Wynik dodawania to: ", nowyInput1 + nowyInput2)
# print("Wynik dodawania to: ", nowyInput1, "+", nowyInput2, "=", nowyInput1 + nowyInput2)

#operatory porównania
#są to standardowe operatory, praktycznie jak w każdych językach, standardowo podczas porównywania zostaje nam zwracane true lub false np. print(2>=2) otrzymamy true

#instrukcje warunkowe
#przykłady zapisywania instrukcji warunkowych
if (5<3):
    print("Wyrażenie jest poprawne") # najważniejsze jest, zeby było wcięcie, bo dotyczy to konkretnego warunku WAŻNE: warunki muszą być tej samej wielkości dla tego samego warunku
print("Wyrażenie jest poprawne") # ten print już nie należy do warunku dlatego, że nie ma odstępu

liczba11 = 2
liczba12 = 3
if (liczba11 > liczba12):
    print("liczba a jest większa od b")
elif (liczba11 < liczba12):
    print("liczba b jest większa od a")
else:
    print("liczba a i b są równe")

# trzeba pamiętać że wszystkie wartości oprócz 0 są zwracane jako true, czyli program zostanie dalej puszczony

## operatory logiczne !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# wartosc = int(input("sprawdz czy wartość jest z zakresu 1 do 10: "))
wartosc = 2

if (wartosc >= 1):
    if (wartosc <= 10):
        print("wartość jest od 1 do 10")

# operator logiczny and
if (wartosc >= 1 and wartosc <= 10):
    print("wartość jest pomiędzy 1 a 10 z operatorem and")

# operator logiczny or
# wtedy wystarczy że jeden argument jest true i program zostanie dalej wykonany

#operator not
if (not(wartosc >= 1 and wartosc <= 10)):
    print("wartość NIE jest pomiędzy 1 a 10 z operatorem and")


# PĘTLE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# liczbaDlaPetli = 0

# while liczbaDlaPetli <= 5:
#     print(liczbaDlaPetli)
#     liczbaDlaPetli += 1

wynik = 0
# i = 0
# while i < 4:
#     x1 = int(input("Podaj liczbę: "))
#     x1 = 1
#     wynik += x1
#     i += 1

# print("Wynik dodawania czterech liczb to: ", wynik)

# for i in range(0, 4):
#     x2 = int(input("Podaj liczbę: "))
#     wynik += x2

# print("Wynik dodawania czterech liczb to: ", wynik)


# ćwiczenie 1
# iloscDzialan = int(input("podaj ile działań chcesz wykonać: "))

# i = 0
# wynikDodawania = 0
# while (i < iloscDzialan):
#     liczba1 = int(input("podaj liczbę parzysta: "))
#     if (liczba1 % 2 == 0):
#         wynikDodawania += liczba1
#         i += 1
#     else:
#         print("podałeś liczbę nieparzystą")
#         continue
# print("wynik dodawania: ", wynikDodawania)

#ćwiczenie 2
# import random
# szukanaLiczba = random.randint(1, 1000)
# liczbaUzytkownika = 0

# while (not(szukanaLiczba == liczbaUzytkownika)):
#     liczbaUzytkownika = int(input("Wpisz liczbę: "))
#     if(liczbaUzytkownika > szukanaLiczba):
#         print("szukana liczba jest mniejsza!")
#     elif(liczbaUzytkownika < szukanaLiczba):
#         print("szukana liczba jest większa!!!")
#     else:
#         print("wygrałeś!!!!")

#LISTY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
imiona = ["Patryk", "Zosia", "Dominika"] #lista 3 el.
liczby = [1, 2, 3]
listaMieszana = [1, "a", 2]

#wypisywanie z tablicy
print(imiona[0]) # wyswietlenie pierwszego imienia z tablicy
print(imiona[-1]) # wyswietlenie ostatniego imienia z tablicy

print("Patryk" in imiona) # sprawdzanie czy konkretny element jest w TAblicy

# imie = input("Wpisz imię: ")

if (imie in imiona):
    print("Masz dostep")
else:
    print("Brak dostepu")

#metody do operowania na listach 
testLista = [1, 2, 3, 4, 56, 12, 13, 14]
print(len(testLista)) # sprawdzanie długości listy
testLista.extend([333, 444]) # dodanie kolejnych dwóch elementów do listy
print(testLista)
testLista.insert(1, 1000) # wstawianie na miejsce pierwsze elementu o wartości 1000, element na konkretnej pozycji
print(testLista)
print(testLista.index(13)) # znalezienie na której konkretnie pozycji jest konkretny element
newList = testLista
newList.sort() # funkcja pozwalająca posortować elementy od najmniejszej do największej
print(newList) # posortowanie listy

#dodatkowe przydatne funkcje
# .append - dodanie elementu na koniec listy
# .max - znalezienie największej wartości
# .min - znalezienie minimalnej wartości
print(min(testLista)) # przykład zastosowania
# .count - znajdowanie ile konkretnych wystąpień jest w danej tablicy
print(testLista.count(13)) 
# .pop - usuwa ostatni element
# .remove - usuwa pierwsze wystąpienie w tablicy
# .clear - czyści listę
# .reverse - odwraca kolejność listy

#Krotki - tuple !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#najważniejszą różnicą miedzy listami jest to, że krotki nie można póżniej zmieniać
krotka = 1, 2, 3, 12, 12, -12 #aby stworzyć krotkę nie dajemy nawiasów kwadratowych, ewentualnie nawiasy okkrągłe

print(krotka[4])
#po co korzystać z krotki? - kiedy tylko możliwe, zawsze kiedy wiesz, że nie bedzie zmieniana, bo wtedy napewno się nie pomylisz i krotki są szybsze i zajmują mniej miejsca w pamięci

#Słowniki - dictionary !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
pokoje = {45: 'Patryk Romanowski', 46: 'wolny', 47: 'Zbigniew Nowak'} #przykładowy słownik
pokoje[46] = 'Jan Kowalski' #dodanie nowego elementu do słownika, jeśli klucz jest to zmnienia się wartość
pokoje[48] = "wolny" #jeżeli nie ma klucza jest dodawany nowy do słownika, z przypisaną wartością
# inne metody pracy na słownikach
pokoje.get(48) # wyświetla aktualną wartośc dla podanego klucza
pokoje.update({48: 'Kazimierz Nowak'}) #aktualizacja wartości dla wybranego klucza
del(pokoje[48]) #usuwanie wartości spod klucza, razem z kluczem
print(pokoje.pop(47)) # usuwanie wartości wraz ze zwróceniem usuwanej wartości
# pokoje.clear() # usunięcie całego słownika
print(len(pokoje)) # sprawdzenie ile wartości znajduje się w słowniku

# Zbiory!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#różnice pomiędzy listami, krotkami, zbiorami i słownikami

#           el.unikalne         kolejność           zmiana konkretnego el.      nowe elementy
#listy          NIE                 TAK                 TAK                         TAK
#krotki         NIE                 TAK                 NIE                         NIE
#słowniki       TAK                 NIE                 TAK                         TAK
#zbiory         TAK                 NIE                 NIE                         TAK

zbiorA = {1, 2, 3, 4, 1, 2} # 1 i 2 się nadpiszą bo nie mogą byc dwa takie same elementy
zbiorA.add(7) # sposób na dodanie nowego elementu
# zaletą zbioru jest unikalność, wykorzystujemy jeżeli nie chcemy mieć zduplikowanych danych
print(set(zbiorA)) # w taki sposób 
zbiorA.discard(1) #usuwa ze zbioru wartosc 1

#TYPY ZAGNIEŻDZONE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
imie1 = "Patryk"
nazwisko1 = "Romanowski"
wiek1 = 34
imie2 = "Arek"
nazwisko2 = "Nowak"
wiek2 = 38

osoba1 = ('PAtryk', 'Romanowski', 34)
osoba2 = ('Arek', 'Nowak', 38)

listaGosci = [          # jest to zagnieżdzona lista, ale wewnątrz listy możemy np. użyć krotki
    ['Patryk', 'Romanowski', 34],
    ['Arek', 'Nowak', 38]
]

print(listaGosci[1][1])

for imie, nazwisko, wiek in listaGosci:  # gdy wypisujemy poszczególne elementy z listy, automatycznie sie przypisują do podanych zmiennych w pętli
    print("imię: ", imie)
    print("nazwisko: ", nazwisko)
    print("wiek: ", wiek)

## wypisywanie zagnieżdzeń !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

people = {
        "IcFDG2bO9AYDF651DoyH": {'name': 'John', 'age': 27, 'sex': 'Male'},
        "KcD9ntE6IRM59vkVta1k": {'name': 'Marie', 'age': 22, 'sex': 'Female'},
        "yDlgcn99xPc19mYXcRmy": {'name': 'Agness', 'age': 25, 'sex': 'Female'},
        "cpQh6GiAbBdGv35NDoTk": {'name': 'Nabeel', 'age': 17, 'sex': 'Male'},
        "12BifzWxCQySKgLhgahC": {'name': 'Jasmin ', 'age': 42, 'sex': 'Female'},
        "QLnmg0pzlLj9x7c7DlLv": {'name': 'Ruby', 'age': 55, 'sex': 'Female'},
        "To47urX0DUznWmOxGZ6H": {'name': 'Lori', 'age': 27, 'sex': 'Male'},
        "KQ4bir3y4tlkbG69I7zq": {'name': 'Marie', 'age': 42, 'sex': 'Female'},
        "94cp4hsyZP2BnCh4D34z": {'name': 'Agness', 'age': 25, 'sex': 'Female'},
        "Vr4wRdkljeEs46Czxo54": {'name': 'Chiara', 'age': 17, 'sex': 'Male'},          
         }

people2 = [
         {'id': 'IcFDG2bO9AYDF651DoyH', 'name': 'John', 'age': 27, 'sex': 'Male'},
         {'id': 'KcD9ntE6IRM59vkVta1k', 'name': 'Marie', 'age': 22, 'sex': 'Female'},
         {'id': 'yDlgcn99xPc19mYXcRmy', 'name': 'Agness', 'age': 25, 'sex': 'Female'}               
        ]

people3 = ["Arkadiusz",
           "Wiola",
           "Kuba"
          ]

ratings1 = {
            "Arkadiusz": (2,1,2,3,2,3),
            "Agness": (4,2,1,3,4)           
           }    
ratings2 = [
        {'name': "Arkadiusz", 'ratings': (2,1,2,3,2,3), 'behaviour': 4},
        {'name': "Agness", 'ratings': (4,2,1,3,4), 'behaviour': 2}
    ]

ratings3 = {
        "Arkadiusz": {'ratings': (2,1,2,3,2,3), 'behaviour': 4},
        "Agness:": {'ratings': (4,2,1,3,4), 'behaviour': 2}
    }

for key in ratings1:
    print(key,  "oceny: ", ratings1[key])

for value in people2:
    print(value)
    for key in value:
        print(key, value[key])

for key in people:
    print(key)
    for item in people[key]:
        print(item, ": ", people[key][item])

for id, dictionary in people.items(): #szybsza metoda, ale da radę stosować tylko do słowników
    print("ID: ", id)
    for key in dictionary:
        print(key, ": ", dictionary[key])

# Ćwiczenia !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# slownik = {}
# endProgram = False
# userChange = ""
# newDef = ""
# defDescription = ""

# while (not(endProgram)):
#     print("wybierz działanie: ")
#     print("jeśli chcesz zakonczyc działanie programu wpisz: END")
#     print("jeśli chcesz dodać nową definicję wpisz: ADD")
#     print("Jeśli chcesz znalężć definicję wpisz: FIND")
#     print("Jeśli chcesz usunąć definicję wpisz: DEL")
#     userChange = input("Wpisz odpowiedni znak: ")
#     if(userChange == "END"):
#         endProgram = True
#     elif(userChange == "ADD"):
#         newDef = input("Wpisz nazwę definicji: ")
#         defDescription = input("Dodaj opis definicji: ")
#         slownik[newDef] = defDescription
#         print("Zapisano nową definicję !!!!")
#     elif(userChange == 'FIND'):
#         print("Zapisane definicje")
#         for item in slownik:
#             print(item)
#         myChange = input("Wybierz definicję: ")
#         if myChange in slownik:
#             print(myChange, ": ", slownik[myChange])
#         else:
#             print("Nie ma wybranej definicji")
#     elif(userChange == 'DEL'):
#         itemDel = input("Wpisz element do usunięcia: ")
#         if itemDel in slownik:
#           del(slownik[itemDel])
#           print("usunięto rekord")
#         else:
#             print("nie ma w bazie podanego elementu")

# Wyrażenia listowne!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# liczby2 = [1 ,2, 3, 4, 5, 6, 7]
# liczbyDoPotegi = [element**2
#                   for element in liczby2]
# liczbyParzyste = [element
#                   for element in liczby2
#                   if (element % 2 == 0)
#                   ]
# print(liczby2)
# print(liczbyDoPotegi)
# print(liczbyParzyste)

#Wyrażenia generujące !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# evenNumbersGenerator = (element**2
#                         for element in range(100)
#                         )
# sum = 0
# for item in evenNumbersGenerator:
#     sum += item
#     print(item)
# print(sum)

#Wyrażenie słownikowe
names = ["Patryk", "Zosia", "Dominika"]
numbers = [1, 2, 3]
celcius = {'t1': 20, 't2': -10, 't3': 12}

namesLength = {
    name : len(name)
    for name in names
}

multipleNumbers = {
    number : number*number
    for number in numbers
    if number > 1
}
print(multipleNumbers)

fahrenheit = {
    key: (temp * 1.8) + 32
    for key, temp in celcius.items()
}

print(fahrenheit)

#wyrażenie zbioru !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1
names = {"patryk", "Zosia", "dominika"}
names = {name.capitalize()
         for name in names
         if not(name.upper().startswith("P"))}


print(names)

## zadanie!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

result = [element
          for element in range(2,470)
          if(element % 7 == 0) and not(element % 5 == 0)]

print(result)

# FUNKCJE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def wiadomosc_powitalna(name):
    print("Witaj: ", name, "!")

wiadomosc_powitalna("Patryku")
wiadomosc_powitalna("Dominiko")
wiadomosc_powitalna("Zosiu")

#funkcja z wieloma parametrami

def pole_prostokata(a, b):
    print("Pole wynosi: ", a*b)

#funkcja zwracająca wartośc

def oblicz_pole(a, b):
    return a * b

print(5 * oblicz_pole(5,5))

#ćwiczenie - program liczący powierzchnie figur

def prostokat(a, b):
    return a * b

def kwadrat(a):
    return a*a

def trojkat(a, h):
    return 0.5*a*h

def kolo(r):
    return math.pi * r*r

def trapez(a, b, h):
    return (a*h) - (0.5 * h * (a-b))

# def obliczanie(liczba):
#     if(liczba == 1):
#        aProstokat = int(input("Wpisz długośc boku: "))
#        hProstokat = int(input("Wpisz wysokość: "))
#        print("Wynik: ", prostokat(aProstokat, hProstokat)) 
#     elif(liczba == 2):
#         aKwadrat = int(input("Wpisz długośc boku: "))
#         print("Wynik: ", kwadrat(aKwadrat))
#     elif(liczba == 3):
#         aTrojkat = int(input("Wpisz długośc boku: "))
#         hTrojkat = int(input("Wpisz wysokosc: "))
#         print("Wynik: ", trojkat(aTrojkat, hTrojkat))
#     elif(liczba == 4):
#         rKolo = int(input("Wpisz promień koła: "))
#         print("Wynik: ", kolo(rKolo))
#     elif(liczba == 5):
#         aTrapez = int(input("Wpisz dłuższy bok: "))
#         bTrapez = int(input("Wpisz krótszy bok: "))
#         hTrapez = int(input("Wpisz wysokośc: "))
#         print("Wynik: ", trapez(aTrapez, bTrapez, hTrapez))
#     else:
#         print("wpisałeś niepoprawną wartość")

    

# print("Wybierz jaką figurę chcesz obliczyć")
# print("pole prostokąta - 1")
# print("pole kwadratu - 2")
# print("pole trójkąta - 3")
# print("pole koła - 4")
# print("pole trapezu - 5")
# wybor = int(input("Wpisz liczbę: "))
# obliczanie(wybor)

import figury

print(figury.pole_kola(1))

from enum import IntEnum

Menu_Figury = IntEnum('Figury', 'kwadrat prostokat trojkat koło trapez')
print(Menu_Figury.kwadrat)

#Zadanie
import time

def sumuj_do1(ilosc_liczb):
    wynik = 0
    for liczba in range(ilosc_liczb):
      wynik += liczba
    return wynik

def sumuj_do2(ilosc_liczb):
   return sum((ilosc_liczb 
               for ilosc_liczb in range(1, ilosc_liczb + 1)))

def sumuj_do3(ilosc_liczb):
    return (1 + ilosc_liczb) / 2 * ilosc_liczb

print("Wynik sum1 wynosi: ", sumuj_do1(5000))
print("Wynik sum2 wynosi: ", sumuj_do2(5000))
print("Wynik sum3 wynosi: ", sumuj_do3(5000))

def function_performance(func, arg):
   start = time.perf_counter()
   result = func(arg)
   print("wynik: ", result)
   end = time.perf_counter()
   return end - start

def show_message(show_message):
    print("wiadomość: ", show_message)

function_performance(sumuj_do1, 5000)
function_performance(sumuj_do2, 5000)
function_performance(sumuj_do3, 5000)

#Domyślne argumenty
def increment(x, amount = 1):
    return x + amount

print(increment(12)) # w tym przypadku wystarczy podać jeden argument

#argumenty kluczowe i pozycyjne
def greet(name, message):
    print(message, name, sep="     \n ") 

greet("Patryk", "HEJ!") # w tym przypadku argumenty zostaną przypisane zgodnie z kolejnością
greet(message="Witaj", name = "Patryk") # w tym przypadku argument zostanie przypisany do konkretnej nazwy, teraz kolejnośc nie ma znaczenia

list1 = [x for x in range(1000)]
zbior1 = {x for x in range(1000)}

print("!!!!!!!!!!!!!!!!")

def task_function(number, name, how_many = 1000):
  if name == "list":  
    start = time.perf_counter()
    retValue = "nie"
    for i in range(how_many):
        result = [element 
                  for element in list1
                  if element == number]   
        if(result != []):
            retValue = "tak"
        else:
            retValue = "nie" 
    end = time.perf_counter()
    timeList = end - start
    return(retValue, timeList)

  elif name == "zbior":
      start = time.perf_counter()
      retValue = "nie"
      for _ in range(how_many):
          result = [element 
                    for element in zbior1
                    if element == number]
          if(result != []):
             retValue = "tak"
          else:
             retValue = "nie"
      end = time.perf_counter()
      timeList = end - start
      return(retValue, timeList)

print(task_function(120, "list"))
print(task_function(120, "zbior"))

def function_performrnce2(func, *arg, how_many = 1000):
    sum = 0

    for i in range(0, how_many):
        start = time.perf_counter()
        func(*arg)
        end = time.perf_counter()
        sum = sum + (end-start)

    return sum

def is_element_in(what_value, container):
    if what_value in container:
        return True
    else:
        return False

print(function_performrnce2(is_element_in, 450, list1, how_many= 3000))
print(function_performrnce2(is_element_in, 450, zbior1, how_many= 3000))


def count(*arg):
    suma = 0
    for i in arg:
        suma += i
    return suma

print(count(2,4,1,2,4,5, 10))


#Zasięg globalny vs zasięg lokalny !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#obiekty:
""" 
    Obiekty to zmienna która ma więcej możliwości 
    można wywołać na niej funkcje
    może mieć więcej niż jedną wartość

    obiekty immutable: bool, int, float, tuple, str

    immutable - niezmienne
    mutable - zmienny
"""

listSample = [1, 4, 512, 24]
listSample2 = listSample
listSample2.append(465)
print(listSample)
print(listSample2)

a1 = 4
print(a1)
b1 = a1
print(b1)
b1 = 7
print(b1)

# funkcje anonimowe - lambda

test = lambda x: x * 2
print(test(6))

my_list = [2, 5, 6, 12, 14, 18, 22]

my_list_filter = list(filter(lambda x: x % 2 == 0, my_list))
print(my_list_filter) # zwrócona lista zawierająca liczby parzyste

number1 = [1, 3, 5 ,7, 8]
number2 = [1, 3, 5, 7, 9]
number3 = [2, 4, 6, 8, 12]

def any_even(lista):
    for nr in lista:
        if nr %2 == 0:
            return True
    
    return False

print(any_even(number1))
print(any_even(number2))

number11 = [nr % 2 == 0  #tutaj dostanę tablice number11 = [False, False, False, False, True]
for nr in number1
]
number12 = [nr % 2 == 0  #tutaj dostanę tablice number11 = [False, False, False, False, True]
for nr in number2
]

print(number11)

# teraz można użyć funkcji any, by sprawdzić czy w danej liście jest jakikolwiek element true
result = any(number11)
print(result)
result2 = any(number12)
print(result2)

#funkcja all
number13 = [nr % 2 == 0  #tutaj dostanę tablice number11 = [False, False, False, False, True]
for nr in number3
]

result3 = all(number13) # w tym przypadku wszystkie wartości będą true, więc funkcja zwróci wartośc tru, ponieważ wszystkie będą true
print(result3)

person = {
    "name": "Patryk Romanowski",
    "age": 34,
    "skills": ["Python", "Java Script", "React", "C++"]
}

print(person["skills"])

def checkSkills(skills, skillsForJob = ["Python", "C++"]):
    skillsTrue = [
        skill in skills
        for skill in skillsForJob
    ]
    return skillsTrue

def getInfoAboutPerson(personValue):
    if(personValue == True):
        return "NADAJE SIĘ!"
    else:
        return "NIE NADAJE SIĘ"

personAccept = all(checkSkills(person["skills"]))
personAcceptInfo = getInfoAboutPerson(personAccept)
 
print("Kandydat: ", person["name"], ":", personAcceptInfo)

#losowanie !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

import random
from collections import Counter

print(random.random()) # losuje liczbe o 0 do 1, do wielu miejsc po przecinku

#zadanie: licznik randomowych trafień

hit = 0
not_hit = 0
counter = 0

while counter < 1000:
    counter += 1
    los = random.uniform(0, 100)
    if los <= 50:
        hit += 1
    else:
        not_hit += 1

print("trafienia:", hit)
print("pudła:", not_hit)

random.randint(1, 100) # to losuje od 1 do 100 i nic nie trzeba dodawać ani odejmować

#funkcje choice i choices
movieList = ["Film1", "Film2", "Film3", "Film4", "Film5"]
nagrody = ["długopis", "książka", "samochód"]
print(random.choice(movieList))

print(Counter(random.choices(nagrody, [100, 10, 1], k=1000))) # losujemy, wraz ze zliczeniem elementów(dzięki importowaniu funkcji Counter) 1000 razy (parametr k) z 3 elementów (liczby w liście oznaczają ile razy więcej dany element ma być brany pod uwagę (pierwszy - 100 razy bardziej, drugi - 10 razy bardziej))

#funkcja shuffle

cardList = ["9", "9", "9", "9", "10", "10", "10", "10", "J", "J", "J", "J", "Q", "Q", "Q", "Q", "K", "K", "K", "K", "A", "A", "A", "A", "JOKER", "JOKER"]
random.shuffle(cardList)
print(cardList)

#ćwiczenie - symulator lotto, losujący 6 z 49 liczb

def choose_random_numbers(amount, total_amount):
    print(random.sample(range(total_amount), amount))
    print(random.sample(range(total_amount), amount))

myLos = choose_random_numbers(6, 49)

#ćwiczenie !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
"""
Napisz krótką grę w której masz 5 ruchów w jedną stronę poprzez KOMNATĘ.

Za każdym razem masz szansę spotkać po drodzę skrzynkę lub NIC.

Skrzynki mają różne kolory.

Kolor skrzynki oznacza jak rzadka jest ta skrzynka.

zielona - 75%
pomarańczowa - 20%
fioletowa - 4%
złota (legendarna) - 1%

Ustaw, że jest 40% szansy, że nie spotkasz niczego. 60%, że będzie skrzynka.

Ustaw złoto jako to co może "wypaść" ze skrzynki:
zielony - 1000,
pomaranczowy - 4000,
fioletowy - 9000,
zlota - 16000

Pamiętaj o:
1) czystym kodzie
2) nazywaniu zmiennych tak by bylo samoopisujace sie
3) spróbuj napisać program po angielsku

"""

gameLength = 50
boxes = [
    {'color': 'green', 'value': 1000}, 
    {'color': 'orange', 'value': 4000}, 
    {'color': 'purple', 'value': 9000}, 
    {'color': 'gold', 'value': 16000}
]
valueBox = {}
myElements = []
i = 0

while i < gameLength:
    i+=1
    isBox = random.choices([True, False], [60, 40])
    if isBox[0] == True:
        newBox = random.choices(boxes, [75, 20, 4, 1])
        myElements.extend(newBox)
    else:
        continue

result = [
    element['value']
    for element in myElements
        ]

print(result)
print('Twój wynik to: ', sum(result))

## rozwiązanie !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# from enum import Enum

# Event = Enum('Event', ['Chest', 'Empty'])

# eventDictionary = {
#                     Event.Chest: 0.6,
#                     Event.Empty: 0.4
#                 }

# Colours = Enum('Colours', {
#     'Green': 'zielony',
#     'Orange': 'pomarrańczowy',
#     'Purple': 'fioletowy',
#     'Gold': 'złoty'
# })

# chestColoursDictionary = {
#                             Colours.Green :  0.75,
#                             Colours.Orange : 0.2,
#                             Colours.Purple : 0.04,
#                             Colours.Gold : 0.01
#                          }

# chestColourList = tuple(chestColoursDictionary.keys())
# chestColourProbability = tuple(chestColoursDictionary.values())

# eventList = list(eventDictionary.keys())
# eventProbality = list(eventDictionary.values())

# rewardsForChests  = {
#                     chestColourList[reward]: (reward + 1) * (reward + 1) * 1000
#                     for reward in range(len(chestColourList))
# }

# gameLength1 = 5
# goldRequired = 0
# print("Welcome on my game called KOMNATA!")
# print("""You have only five steps to make,
#     see yourself how much gold you collect!!!
# """)

# while gameLength1 > 0:
#     gameAnswer = input("Do you want to move forward?")
#     if(gameAnswer == "yes"):
#         print("Great, let's see what you got...")
#         gameLength1 -= 1
#         drawnEvent = random.choices(eventList, eventProbality)[0]
#         if(drawnEvent == Event.Chest):
#             print("You've drawn a Chest")
#             drawnColor = random.choices(chestColourList, chestColourProbability)[0]
#             print("The chest color is:", drawnColor.value)
#             gamerreward = rewardsForChests[drawnColor]
#             goldRequired += gamerreward
#         elif(drawnEvent == Event.Empty):
#             print("You've drawn nothing")
#     else:
#         print("You can go just straight man")
#         continue
# print("Congratulation!!! You earned: ", goldRequired, "golds!")

# przybliżenia !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def findAproximateValue(value):
    lowestValue = value * 0.9
    highestValue = value * 1.1
    return random.randint(lowestValue, highestValue)

#operacje na plikach !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#podstawowe metody otwierania plików
# r - R - read 
# w - W - write
# a - A - append (dopisywanie)

with open("test", "w") as file: #mamy odwołanie do pliku - uchwycenie (HANDLE)
    file.write("sample")
    file.write("sample2")
    file.close() # żeby zapisać dane w pliku, koniecznie trzeba zamknąć plik

with open("oceany.txt", "r", encoding="UTF-8") as file:
    oceany = file.read().splitlines() # jeżeli chcemy przeczytać wszystko i pozbyć się lini, z każdej lini zrobi osobną wartośc w tablicy
    oceany2 = file.readlines() # czyta wszystkie linie i zapisuje w tablicy

with open("oceany.txt", "a", encoding="UTF-8") as file:
    print(file.tell()) #sprawdza w którym miejscu zakończyliśmy, warto zauważyć że append użyliśmy 
    file.write("\nNowy ocean") #dopisuje nowy ocean na koniec, /n daje od nowej linii

# mnogir tryby otwierania plików!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# r+ do czytania i pisania
# w+ do pisania i czytania, różni się tym, że usunie zawartośc istniejącego pliku lub stworzy plik gdy go nie było
# a+ "wieczny tryb" dopisywania i przy okazji czytania
# UWAGA! wskaźnik dopisywania jest zawsze na końcu, jeżeliplik nie istniał stworzy go
with open("oceany.txt", "a+", encoding="UTF-8") as file:
    file.write("\n nowy ocean 2")
    file.seek(0) #zaczyna czytać od początku
    print(file.readline())
    print(file.tell())    

imiona_nazwiska = []
imiona = []
nazwiska = []

with open("imionanazwiska.txt", "r", encoding="UTF-8") as file:
    imiona_nazwiska = file.read().splitlines()
    # print(imiona_nazwiska) 

for name in imiona_nazwiska:
    name_parts = name.split()
    if len(name_parts) == 1:
        imiona.append(name_parts[0])
    else:
        imiona.append(name_parts[0])
        nazwiska.append(name_parts[1])

with open("imiona.txt", "w") as file:
    for name in imiona:
        file.write(name + "\n")

with open("nazwiska.txt", "w") as file:
    for name in nazwiska:
        file.write(name + "\n")

# print(imiona)
# print(nazwiska) 

#JSON !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
import json

film = {"title": "Ale ja nie będę tego robił!", 
        "release_year": 1969, 
        "won_oscar": True, 
        "actors": ["Arkadiusz Włodarczyk", "Wiolleta Włodarczyk"], 
        "budget": None, 
        "credits": {"director": "Arkadiusz Włodarczyk", 
                    "writer": "Alan Burger", 
                    "animator": "Anime Animatrix"}}

#json.dumps(data) - zapisuje dane w postaci stringowej json
#json.dump(data, nameOfFileHandler, ensure_ascii = False) - zapisuje do pliku w postaci json

encodingFilm = json.dumps(film, ensure_ascii=False)

with open("sample.json", "w", encoding="UTF-8") as file:
    json.dump(film, file, ensure_ascii=False)

#odczyt plików JSON !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
encodedRetriveMovied = '{"title": "Ale ja nie będę tego robił!", "release_year": 1969, "won_oscar": true, "actors": ["Arkadiusz Włodarczyk", "Wiolleta Włodarczyk"], "budget": null, "credits": {"director": "Arkadiusz Włodarczyk", "writer": "Alan Burger", "animator": "Anime Animatrix"}}'

decodeMovie = json.loads(encodedRetriveMovied)
# decodeMovie2 = json.load(encodedRetriveMovied)

print(decodeMovie)

encodingFilm2 = json.dumps(film, ensure_ascii=False, indent=4, sort_keys=True) #tutaj dodatkowo robimy wcięcia na 4 spacje i od nowego wiersza, dodatkowo mamy posortowane klucze alfabetycznie

#PyPi - spis paczek pythona
#pip - instalator paczek

import requests 
import json

# def check_website(url):
#     try:
#         # Wykonaj żądanie GET z limitem czasu
#         response = requests.get(url, timeout=5)
        
#         # Sprawdź status odpowiedzi
#         if response.status_code == 200:
#             print(f"Strona {url} istnieje (status: {response.status_code}).")
#         else:
#             print(f"Strona {url} zwróciła status: {response.status_code}.")
#     except requests.exceptions.ConnectionError:
#         print(f"Nie udało się połączyć z {url}. Strona może nie istnieć.")
#     except requests.exceptions.Timeout:
#         print(f"Żądanie do {url} przekroczyło limit czasu.")
#     except requests.exceptions.RequestException as e:
#         print(f"Wystąpił błąd: {e}")

# Przykład użycia
# check_website("http://example.com")  # Strona istnieje
# check_website("http://gr3333e.pl")   # Strona prawdopodobnie nie istnieje

r = requests.get("https://jsonplaceholder.typicode.com/todos/")
# tasks = json.loads(r.text)

def countTaskFrequency(tasks):
     completedTaskFrequencyByUser = dict()
     for entry in tasks:
        if(entry["completed"] == True):
            try:
                completedTaskFrequencyByUser[entry["userId"]] += 1
            except:
                completedTaskFrequencyByUser[entry["userId"]] = 1
     return completedTaskFrequencyByUser

def users_with_top_completed_tasks(completedTaskFrequency):
     userIdWithMaxCompletedTasks = []
     maxAmountOfCompletedTask = max(completedTaskFrequency.values())
     for userId, numberOfCompletedTask in completedTaskFrequency.items():
        if(numberOfCompletedTask == maxAmountOfCompletedTask):
            userIdWithMaxCompletedTasks.append(userId)
     return userIdWithMaxCompletedTasks

try: 
    tasks = r.json()
except json.decoder.JSONDecodeError:
    print("Niepoprawny format")
else:
    completedTaskFrequency = countTaskFrequency(tasks)
    result = users_with_top_completed_tasks(completedTaskFrequency)

print(result)
 

#sposób 1 
r = requests.get("https://jsonplaceholder.typicode.com/users/")
users = r.json()
# print(users)

for user in users:
    if (user["id"] in result):
        print("Wygrana należy do:", user["name"])

#sposób 2
stringForSend = "https://jsonplaceholder.typicode.com/users?"
for user in result:
    print(user)
    stringForSend += f"id={user}&"  # Dodaj parametry do URL

stringForSend = stringForSend.rstrip("&")
r = requests.get(stringForSend)
user = r.json()
print(user)

#działanie na zdjęciach biblioteka pillow

from PIL import Image
im = Image.open("XD.jpg")
print("Wysokość zdjęcia wynosi:", im.size[1])
print("Szerokość zdjęcia wynosi:", im.size[0])