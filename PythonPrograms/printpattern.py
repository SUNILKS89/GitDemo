# Python program to print following pattern
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *
n = int(input("enter number of rows:"))

for i in range(1,n+1):
    print("*" * i)
for i in range(n-1,0,-1):
    print("*" * i)