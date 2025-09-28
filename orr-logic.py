num = int(input("Enter a num between 0-10: "))

while num < 1 or num > 10:
    print(f"{num} is not valid ")
    num = int(input("Enter a num between 0-10: "))

print(f"ur number is {num}")