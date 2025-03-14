'''
Author:Amal k philip
Date:22-11-2024
Description:Program to construct patterns of stars (*), using a nested for loop.
'''
num=int(input("Enter the rows:"))
print("Increasing triangle pattern")
for i in range(0,num):
    for k in range(0,i):
        print("*",end=" ")
    print("*")

print("Decreasing triangle pattern")
for i in range(num,0,-1):
    for k in range(0,i-1):
        print("*", end=" ")
    print("*")

print("Hill pattern")
for i in range(0,num):
    for j in range(num-i-1):
        print(" ",end=" ")
    for k in range((i*2)+1):
        print("*",end=" ")
    print()

print("Reverse hill pattern")
for i in range(num,0,-1):
    for j in range(num - i):
        print(" ", end=" ")
    for k in range((i * 2) - 1):
        print("*", end=" ")
    print()
