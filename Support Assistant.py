print("Welcome to Chris's Support Assistant")

print()

name = input("What is your name? ")
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