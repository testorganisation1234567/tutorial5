import random

random_number = random.randint(0,40)

def print_message(low, high):
    print("******************")
    print(f"The number is between {low} and {high}")
    print("******************")

if random_number < 10:
    print_message(0, 10)
elif random_number < 20:
    print_message(10, 20)
elif random_number < 30:
    print_message(20, 30)
else:
    print_message(30, 40)
