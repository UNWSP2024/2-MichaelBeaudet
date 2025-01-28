#Author: Michael Beaudet
#Title: Week 2 Program 3
#Date: 1/28/25
def calculate_total_purchase():
    
    sales_tax_percent = 0.07

    subtotal = 0 

    item1 = float(input("Enter price of item 1: $"))
    item2 = float(input("Enter price of item 2: $"))
    item3 = float(input("Enter price of item 3: $"))
    item4 = float(input("Enter price of item 4: $"))
    item5 = float(input("Enter price of item 5: $"))

    subtotal = item1 + item2 +item3 +item4 + item5

    sales_tax = subtotal * sales_tax_percent
    total = subtotal + sales_tax

    total = round(total, 2)

    print("Total:", total)

calculate_total_purchase()