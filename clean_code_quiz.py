import random

random_number = random.randint(0,40)
if random_number < 10:
    print("******************")
    print(f"The number is between 0 and 10")
    print("******************")
elif random_number < 20:
    print("******************")
    print(f"The number is between 10 and 20")
    print("******************")
elif random_number < 30:
    print("******************")
    print(f"The number is between 20 and 30")
    print("******************")
else:
    print("******************")
    print(f"The number is between 30 and 40")
    print("******************")
