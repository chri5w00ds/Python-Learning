print("Welcome to Chris's Support Assistant")

print()

name = input("What is your name? ")
device = input("What device are you using? ")
problem = input("What problem are you experiencing? ")
priority = input("Rate the urgency as Low, Medium or High! ")

print()

print("Support Summary")
print("---------------")

print(f"Customer: {name}")
print(f"Device: {device}")
print(f"Problem: {problem}")

if priority == "High":
    print("This issue should be prioritised.")
elif priority == "Medium":
    print("This issue should be handled soon.")
else:
    print("This issue can be scheduled for later.")

