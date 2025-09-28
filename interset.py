p = 0
r = 0
t = 0

while p <= 0:
    p = float(input("Enter the principle value: "))
    if p <=0 :
        print("can't be less that or equal to 0")


while r <= 0:
    r = float(input("Enter the interset rate: "))
    if r <=0 :
        print("can't be less that or equal to 0")



while t <= 0:
    t = float(input("Enter the time in years: "))
    if t <=0 :
        print("can't be less that or equal to 0")

totalBalance = p * pow((1+ r /100), t)
print(f"Balance after {t} years is : ${totalBalance:.2f}")