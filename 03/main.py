#dots saraksts
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#Ievda skaitli
num = int(input("Choose a number: "))
#Jauns saraksts
new_list = []
#Cik simboli ir iekšā "a" sarakstā
for i in a:
#Ja simbolu skaits ir mazāks par ievadīto skaitli
    if i < num:
#Tad Jaunam sarakstam pievieno simbolu skaitu
        new_list.append(i)
#Izprintēt Jauno sarakstu
print(new_list) 