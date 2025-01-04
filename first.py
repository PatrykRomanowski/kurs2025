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


