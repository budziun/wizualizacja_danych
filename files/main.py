#zad 1
n = int(input("podaj liczbe n"))
if n<0 or n>100:
    print("n is too large")
    exit()
for i in range(n+1):
    for j in range(n+1):
        print(i,"*",j,"=",i*j,end='\t')
    print()

#zad 2
def dzielnik(p,q):
    while(q):
        p,q=q,p%q
    return p

a= int(input("Podaj a:"))
b= int(input("Podaj b:"))

d= dzielnik(a,b)
p=a//d
q=b//d

print(f"Ulamek nieskracalny dla {a}/{b} to {p}/{q}")

#zad 3
import math
n = int(input("podaj n"))

e1=(1+(1/n))**n
e2=0
for k in range(n+1):
    e2 += 1/math.factorial(k)
print("e1=",e1)
print("e2=",e2)

#zad 4
a= int(input("podaj a"))
b= int(input("podaj b"))

def nwd(a,b):
    while(b):
        a,b=b,a%b
    return a

c= nwd(a,b)
print(c)#zad 1
n = int(input("podaj liczbe n"))
if n<0 or n>100:
    print("n is too large")
    exit()
for i in range(n+1):
    for j in range(n+1):
        print(i,"*",j,"=",i*j,end='\t')
    print()

#zad 2
def dzielnik(p,q):
    while(q):
        p,q=q,p%q
    return p

a= int(input("Podaj a:"))
b= int(input("Podaj b:"))

d= dzielnik(a,b)
p=a//d
q=b//d

print(f"Ulamek nieskracalny dla {a}/{b} to {p}/{q}")

#zad 3
import math
n = int(input("podaj n"))

e1=(1+(1/n))**n
e2=0
for k in range(n+1):
    e2 += 1/math.factorial(k)
print("e1=",e1)
print("e2=",e2)

#zad 4
a= int(input("podaj a"))
b= int(input("podaj b"))

def nwd(a,b):
    while(b):
        a,b=b,a%b
    return a

c= nwd(a,b)
print(c)