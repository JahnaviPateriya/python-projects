# Project 1: Pizza Billing System
# Made by Jahnavi 🚀

print("=" * 15, "PIZZA BILLING SYSTEM", "=" * 15)

print("\n🍕 Welcome to Pizza Hut!\n")

bill = 0

print("""Choose your pizza:
1. Small  - ₹100
2. Medium - ₹200
3. Large  - ₹300
""")

# .strip() removes extra spaces
# .lower() converts input to lowercase
mypizza = input("Choose your pizza: ").strip().lower()

if mypizza == "small":
    bill += 100
elif mypizza == "medium":
    bill += 200
elif mypizza == "large":
    bill += 300
else:
    print("❌ Invalid pizza choice!")

extra_cheese = input("Extra cheese? (+₹30) (yes/no): ").strip().lower()

if extra_cheese == "yes":
    bill += 30

cold_drink = input("Cold drink? (+₹50) (yes/no): ").strip().lower()

if cold_drink == "yes":
    bill += 50

print("-" * 50)
print("🧾 YOUR TOTAL BILL: ₹", bill)
print("😊 Thank you! Visit Again!")
print("-" * 50)