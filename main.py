# sum of whole numbers
num = int(input("Enter a whle number: "))
if num < 0:
    print("Please enter a non-negative integer.")
else:
    total = sum(range(num + 1))
    print(f"The sum of whole numbers up to {num} is{total}")