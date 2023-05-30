import random
import time
random.seed(time.time())

print("enter the number of pleyers")
n = int(input())
my_dict = { }

for i in range(n):
    print("enter the player number", end='')
    print(i)
    key = random.randint(1, 1000)
    value = input()
    my_dict[key] = value


sorted_dict = dict(sorted(my_dict.items()))
print(" ------------------------------------ ")
print(" ")
if n%2==0:
    x=n/2
else:
    x=(n-1)/2

count = 0
print("--first team ---")
for key, value in sorted_dict.items():
    if count < x:
        print(f" {value}")
        count += 1
    elif (count > x or count == x ) and count < x*2:
        if count == x:
            print(" ")
            print("--sacond team ---")
            print(" ")
        print(f" {value}")
        count += 1
    else:
        print(" ---player out ---")
        print(f" {value}"+" this player is out")

