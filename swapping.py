print("Swap the values of two data variable using a third temporary variable\n")
Num=input("Enter the type of variable which you want to swap : ")
if(Num=="int"):
    a=int(input("Enter 1st integer number : "))
    b=int(input("Enter 2nd integer number : "))
    
else:
    a=float(input("Enter 1st float number : "))
    b=float(input("Enter 2nd float number : "))
    
temp=a
a=b
b=temp
print("value of a=",a,"\nvalue of b=",b)
print("\nAfter Swapping :\n")
print("value of a=",a,"\nvalue of b=",b)

print("Swap the values of two data variable using arithmetic\n")
Num=input("Enter the type of variable which you want to swap : ")
if(Num=="int"):
    a=int(input("Enter 1st integer number : "))
    b=int(input("Enter 2nd integer number : "))
    print("value of a=",a,"\nvalue of b=",b)
    a=a+b
    b=a-b
    a=a-b
    print("\nAfter Swapping :\n")
    print("value of a=",a,"\nvalue of b=",b)
else:
    a=float(input("Enter 1st float number : "))
    b=float(input("Enter 2nd float number : "))
    print("value of a=",a,"\nvalue of b=",b)
    a=a+b
    b=a-b
    a=a-b
    print("\nAfter Swapping :\n")
    print("value of a=",a,"\nvalue of b=",b)

print("Swap the values of two data variable using python method\n")
Num=input("Enter the type of variable which you want to swap : ")
if(Num=="int"):
    a=int(input("Enter 1st integer number : "))
    b=int(input("Enter 2nd integer number : "))
    
else:
    a=float(input("Enter 1st float number : "))
    b=float(input("Enter 2nd float number : "))

a,b=b,a
print("\nAfter Swapping :\n")
print("value of a=",a,"\nvalue of b=",b)