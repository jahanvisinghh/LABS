#1
 print("hello jklu")
 print("i am learning python")



#2
 name =input("enter the student name:")
 branch=input("enter the students branch:")
 print("wlcome",name)
 print("brach",branch)

#3
 length= int(input("enter the length of the rectangle:"))
 breadth=int(input("enter the breadth of the rectangle:"))
 area=length*breadth
 print("area of the rectangle",area)

#4
 length=int(input("enter the length in feet"))
 width=int(input("enter the width in feet"))
 #convert  feet into  meters
 length=length*0.3048
 width=width*0.3048
 area=length*width
 print("area = ",area,"square metres")

#5
 x=int(input("enter the  positive integer x:"))
 y=int(input("enter the positive integer y: "))
 if x<0 or y<0:
     print("invalid input")
 elif x==0:
     print("invalid input")
 elif y%x == 0:
     print(y,"is divisible by",x)
 else: 
     print(y,"is not divisible by",x)

#6
 n=int(input("enter the number:"))
 if n % 2 :
     print("the remainder",n%2)
 elif n % 2 == 0:
     print("even")
 else:
     print("odd")

#7
 radius= int(input("radius of the circle:"))
 area = 3.14*radius*radius
 if radius<0 or radius>100 :
     print("invalid input")
 else:
     print("area of the circle",area)

#8 
 C=int(input("enter the temperature in celcius"))
 F=C*9%5+32
 K=C+273.15
 print("farenheit",F)
 print("kelvin",K)

#9
 seconds=int(input("enter the number of seconds"))
 if seconds<1 or seconds>86400:
     print("invalid input")
 else:
     hours= seconds//3600
     minutes=  (seconds%3600)//60
     secs= seconds%60

 print(f"{hours:02d}:{minutes:02d}:{secs:02d}")

#10.1
 attended_classes = int(input("enter the no. of classes attended:"))
 total_classes = int(input("enter the total no. of classes :"))

 percentage : (attended_classes / total_classes )* 100
 print(" atendencepercentage", percentage)

 if percentage>= 75:
     print("eligible")
 else:
     print("not eligible")

#10.2
 units = int(input("enter electricity units consumed :"))

 if units < 0 :
     print("invalid input")

 elif units <= 100 :
     bill = units*5
     print("Electricity bill=" , bill)

 elif units <= 200:
     bill=(100*5)+((units-100)*7)
     print("electricity bill=", bill)

 else:
     bill = (100*5)+(100*7) +((units-200)*10)
     print("electricity bill=",bill)

# 10.3
 pin=input("enter your 4-digit pin")

 if len(pin)==4 and pin.isdigit():
     print("valid pin")
 else:
     print("invalid pin ")

        






