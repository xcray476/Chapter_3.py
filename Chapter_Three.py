#Please debug these sections of code, until they work properly
#Section One

ans1 = input("Please enter one number: ")
ans2 = input("ans1 is equal to ans2")

an1 = int(ans1)

sum1 = an1 + ans2

print(sum1)

#Section Two

a = 3
b = 4.5

print(a + b)

#Section Three

c = 2
v = 3.2

print(v/c)

a=9
b=5

if a > b: 
    print("a is greater than b")

if a < b:
    print("a is less than b")
  
if a == b:
    print("a is equal to b") 

##list

l1 = ["7","8","3"]

if "8" in l1:
    print("Yes.")

if "8" not in l1:
    print("No.")


st1 = "mothersday"

if "day" in st1:
    print("Yes.")

if "day" not in st1:
    print("No.")

print(len(l1))

if len(l1) > 4:
    print("That list is long.")
if len(l1) < 5:
    print("The list is short.")
