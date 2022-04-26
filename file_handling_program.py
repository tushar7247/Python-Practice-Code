
#program by recursion
'''
def fact(x):
    y=1
    if x==1 or x==0:
       return y
    else:
        y=x*fact(x-1)
        return y

import time
f=open("filehandling.txt","w")
f.write("Recursion")
f.write("\n")
for i in range(5,995,5):
    start = time.time()
    fact(i)
    end = time.time()
    total_time = end-start
    f.write(str(total_time))
    f.write("\n")


f.write("Iteration")

f.close()
'''


def fact(x):
    fact=1
    if x==1 or x==0:
       return 1
    else:
        for i in range(1,x+1):
            fact = fact*i
        return fact

user_input=5
y=fact(user_input)
print(user_input,y)   
z="Factorial of"+ str(user_input)+"is"+str(y)
f = open("sample.txt","w")
f.write(z)
f.write("\n")
f.close()

#************* for reading operation***************
f = open("sample.txt" ,"r")
z= f.read()
print(z)
f.close()
