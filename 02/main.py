""" Method 1 """
#ievadīt skaitļus
num = int(input("Give me a number to check: "))
check = int(input("Give me a number to divide by: "))
#noosaka vai pirmais ievadītas skaitlis dalās ar 4 bez atlikuma
if num % 4 == 0:
    print(num, "is a multiple of 4")
#nosaka vai pirmais ievadītais skaitlis ir pāra skaitlis
elif num % 2 == 0:
    print(num, "is an even number")
#Ja pirmais ievad skaitlis nedalās ar 4 vai 2 bez atlikuma, tad tas ir nepāra skaitlis
else:
    print(num, "is an odd number")
#Noskaidro vai pirmais skaitlis dalās ar otro bez atlikuma
if num % check == 0:
    print(num, "divides evenly by", check)
#Ja nedalās bez atlikuma
else:
    print(num, "doesn't divide evenly by", check)

""" Method 2 """
#ievada skaitli
num = int(input("Enter a number: "))
#"Mod" ir skaitļa dalījums ar 2 atlikums
mod = num % 2
#Ja skaitli izdalot ar 2 ir atlikums, tad izprintē, ka tas ir nepāra skaitlis
if mod > 0:
    print("You picked an odd number.")
#Ja nē, tad izprintē, ka tas ir pāra skaitlis
else:
    print("You picked an even number.")
