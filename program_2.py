#Author: Michael Beaudet
#Title Week 2 Program 2
#Date 1/28/25
def average_age():
    age1 = int(input("Enter the age of your first friend: "))
    age2 = int(input("Enter the age of your second friend: "))
    age3 = int(input("Enter the age of your third friend: "))
    age4 = int(input("Enter the age of your fourth friend: "))
    age5 = int(input("Enter the age of your fifth friend: "))

    average = (age1 + age2 +age3 +age4 +age5) / 5

    print('The average age is:',average)

average_age()