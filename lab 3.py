#1
x1 = int(input(" enter x1 : "))
y1 = int(input("enter y1 : "))
r  = int(input(" enter radius : "))
y2 = int(input("enter y2 : "))

if r<0:
    print("invalid radius")
else:
     d = ((x2-x1)**2 + (y2-y1)**2)**0.5
if d<r:
     print("point is on the boundry")
else:
    print("point is outside the circle")
       


#2
s = int(input("enter the side of pentagon :"))
if s<= 0 : 
    print("invalid slide")
else : 
    area = (5*s**2)/(4*0.7265)
    print("area of pentagon = ",area)




#3
a=int(input("enter first angle"))
b=int(input("enter second angle:"))
c=int(input("enter third angle:"))

if a<=0 or b<=0 or c<=0 :
    print ("invalid angles")
elif a+b+c!= 180 :
    print("cannot form a triangle")
elif a==90 or b==90 or c==90:
    print("right angled triangle")
elif a>90 or b>90 or c>90 :
    print("obtuse angled triangle")
else:
    print("acute-angled triangle")
 



#4

n = int(input("Enter a 4 digit number: "))

if n < 1000 or n > 9999:
    print("Invalid number")
else:
    first_two = n // 100
    last_two = n % 100

    print("Sum of first two digits =", first_two // 10 + first_two % 10)
    print("Sum of last two digits =", last_two // 10 + last_two % 10)

if (first_two // 10 + first_two % 10) == (last_two // 10 + last_two % 10):
    print("Both sums are equal")
else:
    print("Both sums are not equal")
 


#5 
n= int(input("enter a 5 digit number:"))
if n<10000 or n>99999 :
    print("invalid number")
else:
    d1 = n// 10000
    d2 = (n//1000) % 10
    d3 = (n//100) % 10
    d4 = (n//10) % 10 
    d5 = n%10
    
    largest=max(d1,d2,d3,d4,d5)
    
print("largest digit=", largest)
    
if d1==largest:
    print("position from left = 1") 
elif d2==largest:
    print("position from the left=2")
elif d3==largest:
    print('position from left =3')
elif d4==largest:
    print("position from the left=4")
else: 
    print("position from left=5")
 
    
 #6
a=int(input("enter a :"))
b=int(input("enter b :"))
c=int(input("enter c :"))

temp=a
a=c
c=bb=temp

print("new value of a =",a)
print("new value of b =",b)
print("new value of c =",c)

#7
n=int(input("enter a 3-digit number:"))
if n<100 or n>999:
    print("invalid number")
else:
    d1=n//100
    d2=(n//10)%10
    d3=n%10
    
    digit_sum = d1+d2+d3
    if n% digit_sum==0:
        print("it is a harshad number")
    else:
        print("it is not a harshad number")

#8
V = int(input("Enter initial quantity of water: "))
N = int(input("Enter number of days: "))

if V < 0 or N < 0:
    print("Invalid input")
else:
    water = V * (0.95 ** N) + 200 * (1 - 0.95 ** N)
    
    print("Quantity of water after", water)

#9
a1 = int(input("Enter a1: "))
b1 = int(input("Enter b1: "))
c1 = int(input("Enter c1: "))

a2 = int(input("Enter a2: "))
b2 = int(input("Enter b2: "))
c2 = int(input("Enter c2: "))

D = a1 * b2 - a2 * b1

if D == 0:
    print("Lines are parallel or coincident")

else:
    x = (c1 * b2 - c2 * b1) / D
    y = (a1 * c2 - a2 * c1) / D

    print("x =", x)
    print("y =", y)



    
          
    

    
    
    
    
    
    
    