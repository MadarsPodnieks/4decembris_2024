#dots saraksts
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#Ievda skaitli
num = int(input("Choose a number: "))
#Jauns saraksts
new_list = []
#Cik simboli ir iekšā "a" sarakstā
for i in a:
#Ja simbolu skaits ir mazāks
    if i < num:
        new_list.append(i)

print(new_list)