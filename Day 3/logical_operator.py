
#! logical operators in python are those conditions which check is the condition in code is true or not and only executes if it is true

a = 31

if a > 20 and a%2==0:
    print ("a is a big even number")
elif a < 20 and a%2==0:
    print("a is a small even number")
else:
    print("a is an odd number")