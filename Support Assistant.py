import datetime
import os
folder_name = str(datetime.date.today())
os.makedirs(folder_name, exist_ok=True)


print("Welcome to your Support Assistant")

print()

name = input("What is your name? ")
name = name.lower()
device = input("What device are you using? ")

device_names = {
    "iphone": "iPhone",
    "ipad": "iPad",
    "imac": "iMac",
    "macbook pro": "MacBook Pro",
    "macbook air": "MacBook Air",
    "macbook neo": "MacBook Neo",
}

device_display = device_names.get(device.lower(), device.title())

try:
    with open(f"{folder_name}/{name}_{device_display}.txt", "r") as file:
        contents = file.read()
    print(f"Issues found:\n{contents}")
except FileNotFoundError:
    print("No issues logged yet. ")

while True:

    problem = input("What problem are you experiencing? ")
    priority = input("Rate the urgency as Low, Medium or High! ")
    priority = priority.lower()

    while priority not in ["low", "medium", "high"]:
        print("please enter Low, Medium or High. ")
        priority = input("Rate the urgency as Low, Medium or High! ")
        priority = priority.lower()

    print()

    print("Support Summary")
    print("---------------")

    print(f"Customer: {name.title()}")
    print(f"Device: {device_display}")
    print(f"Problem: {problem.title()}")
    print(f"priority: {priority.capitalize()}")

    if priority == "high":
        print("This issue should be prioritised.")
    elif priority == "medium":
        print("This issue should be handled soon.")
    else:
        print("This issue can be scheduled for later.")

    with open(f"{folder_name}/{name}_{device_display}.txt", "a") as file:
        file.write(f"{name.title()}, {device_display}, {problem.capitalize()}, {priority.capitalize()}\n")        

    again = input("Would you like to log another issue? (Yes/No) ")
    if again.lower() != "yes":
        break

print(folder_name)