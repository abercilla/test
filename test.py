#FUNCTION TO BETTER HANDLE REPETITION

def order_comparison(file):

    #open file to make readable
    the_file = open(file)

    #use melon cost from above
    melon_cost = 1.00

    #start loop to iteraete over each line, format it, and pull out necessary info
    for line in the_file:
        line = line.rstrip()
        words = line.split('|')

        #assign each piece of the relevant line to a variable
        customer_name = words[1] 
        num_melons =  float(words[2])
        customer_paid = float(words[3]) #convert both nums to floats 

        #set expected price equal to # of melons bought * cost (1.00)
        customer_expected = num_melons * melon_cost
        
        #compare expected cost vs actual cost
        if customer_expected < customer_paid:
            print(f"{customer_name} has overpaid for their melons. They paid ${customer_paid:.2f},",
            f"expected ${customer_expected:.2f}")
        elif customer_expected > customer_paid:
            print(f"{customer_name} underpaid for their melons. They paid ${customer_paid:.2f},",
            f"expected ${customer_expected:.2f}")


    the_file.close()

#call function with text file name 
order_comparison("customer-orders.txt")

#******************************************************

#OLD CODE TO BE OPTIMIZED WITH FUNCTION

# melon_cost = 1.00

# customer1_name = "Joe"
# customer1_melons = 5
# customer1_paid = 5.00

# customer2_name = "Frank"
# customer2_melons = 6
# customer2_paid = 6.00

# customer3_name = "Sally"
# customer3_melons = 3
# customer3_paid = 3.00

# customer4_name = "Sean"
# customer4_melons = 9
# customer4_paid = 9.50

# customer5_name = "David"
# customer5_melons = 4
# customer5_paid = 4.00

# customer6_name = "Ashley"
# customer6_melons = 3
# customer6_paid = 2.00

# customer1_expected = customer1_melons * melon_cost
# if customer1_expected != customer1_paid:
#     print(f"{customer1_name} paid ${customer1_paid:.2f},",
#           f"expected ${customer1_expected:.2f}"
#           )

# customer2_expected = customer2_melons * melon_cost
# if customer2_expected != customer2_paid:
#     print(f"{customer2_name} paid ${customer2_paid:.2f},",
#           f"expected ${customer2_expected:.2f}"
#           )

# customer3_expected = customer3_melons * melon_cost
# if customer3_expected != customer3_paid:
#     print(f"{customer3_name} paid ${customer3_paid:.2f},",
#           f"expected ${customer3_expected:.2f}"
#           )

# customer4_expected = customer4_melons * melon_cost
# if customer4_expected != customer4_paid:
#     print(f"{customer4_name} paid ${customer4_paid:.2f},",
#           f"expected ${customer4_expected:.2f}"
#           )

# customer5_expected = customer5_melons * melon_cost
# if customer5_expected != customer5_paid:
#     print(f"{customer5_name} paid ${customer5_paid:.2f},",
#           f"expected ${customer5_expected:.2f}"
#           )

# customer6_expected = customer6_melons * melon_cost
# if customer6_expected != customer6_paid:
#     print(f"{customer6_name} paid ${customer6_paid:.2f},",
#           f"expected ${customer6_expected:.2f}"
#           )

#define function to call for each day
def aggregate_produce(day, file):

    #print the day for log
    print(f"Day {day} ")

    #open file to make readable
    the_file = open(file)

    #start loop to iteraete over each line, format it, and pull out necessary info
    for line in the_file:
        line = line.rstrip()
        words = line.split('|')

        melon = words[0]
        count = words[1]
        amount = words[2]

        print(f"Delivered {count} {melon}s for total of ${amount}")

    the_file.close()

#call function for each day and each file
aggregate_produce(1, "um-deliveries-20140519.txt")
aggregate_produce(2, "um-deliveries-20140520.txt")
aggregate_produce(3, "um-deliveries-20140521.txt")
    