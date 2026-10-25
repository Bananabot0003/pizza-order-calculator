## pizza restaurant 

print("Welcome to Tony's pizzaria, when you need to go, we got the dough!")
print("How may I help you today?")


def Pizza_size():
    print("What size pizza would you like? We have small $8 dollars, medium $12 dollars, and large $20 dollars.")
    size = input("Please enter your choice: ").lower()
    ##error handling for invalid size input
    if size not in ["small", "medium", "large"]:
        print("Invalid size. Please choose small, medium, or large.")
        return Pizza_size()
    ##size cost calculation
    elif size== "small":
        subtotal = 8.00
    elif size == "medium":
        subtotal = 12.00
    elif size == "large":
        subtotal = 20.00
    return subtotal



def topping_count():
    print("are pizzas come with two toppings, would you like to add more? Each additional topping is $1.00")
    toppings = input("Please enter yes or no: ")
    ##error handling for invalid topping input
    if toppings not in ["yes", "no"]:
        print("Invalid input. Please enter yes or no.")
        return topping_count()
    ##topping cost calculation
    elif toppings == "yes":
        num_toppings = int(input("How many additional toppings would you like? "))
        toppings = num_toppings
    else:
        return 0

def delivery_fee():
    print("Would you like your pizza delivered? Delivery is $5.00 plus $0.20 per mile after 10 miles.")
    delivery = input("Please enter yes or no: ")
    ##error handling for invalid delivery input
    if delivery not in ["yes", "no"]:
        print("Invalid input. Please enter yes or no.")
        return delivery_fee()
    ##delivery cost calculation
    if delivery == "yes":
        miles = int(input("How many miles away are you? "))
        if miles <= 10:
            delivery = 5.00
        else:
            delivery = 5.00 + (miles - 10) * 0.20
    else:
        return 0

def checkout():
    print("Thank you for your order! Your total cost is: $" + str(calculate_total_cost(size, toppings, delivery)))
    print("Your pizza size is: " + str(size) + ", with " + str(toppings) + " additional toppings, and delivery fee of $" + str(delivery))
    print("Does everything look correct? Please enter yes or no.")
    correct = input().lower()
    if correct not in ["yes", "no"]:
        print("Invalid input. Please enter yes or no.")
        return checkout()
    elif correct == "yes":
            print("Thank you for your order! Your pizza will be ready soon.")
            return calculate_total_cost(size, toppings, delivery)
    elif correct == "no":
        return incorrect()

def incorrect():
    print("What would you like to change? Please enter size, toppings, or delivery.")
    incorrect = input().lower()
    if incorrect not in ["size", "toppings", "delivery"]:
        print("Invalid input. Please enter size, toppings, or delivery.")
        return incorrect()
    elif incorrect == "size":
        return Pizza_size()
    elif incorrect == "toppings":
        return topping_count()
    elif incorrect == "delivery":
        return delivery_fee()

def calculate_total_cost(size, toppings, delivery):
    total = size + toppings + delivery
    return total


size = Pizza_size()
toppings = topping_count()
delivery = delivery_fee()
calculate_total_cost(size, toppings, delivery)
print("Your total cost is: $" + str(calculate_total_cost(size, toppings, delivery)))
## could fiz to allow multi pizza 