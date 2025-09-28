p = 0
r = 0
t = 0

#r = int(input("Enter the interset rate per year: "))#interset rate
#t = int(input("Enter the time period: ")) #time period elapsed

while p <= 0:
    p = float(input("Enter the principle value: "))#inital balance
    if p <=0 :
        print("can't be less that or equal to 0")

print(f"The total amount you owe: {p}")