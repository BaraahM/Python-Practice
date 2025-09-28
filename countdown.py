import time

x = int(input("Enter the time in seconds: "))

for i in range(0 , x):
    print(i)
    time.sleep(1)

print("OOps")