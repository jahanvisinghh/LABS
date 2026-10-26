#1
'''n=int(input("enter a number"))
if n%5==0:
    print("hi")
else:
    print("bye")'''
    
    
#2
'''X=int(input("enter the no."))
Y=int(input("enter the no."))
H=int(input("enter the no."))
Area= 0.5*(X+Y)*H
print("Area of trapezoid",Area)'''

#3
'''weight=int(input("enter weight in kg:"))
height=int(input("enter height in metres:"))
BMI= weight/height**2
print("BMI=",BMI)
if BMI<18.5:
    print("Underweight")
elif BMI<25:
    print("Normal weight")
elif BMI<30:
    print("slightly over weight")
elif BMI<35:
    print("obese")
else:
    print("clinically obese")'''
    
#4
'''n=input("enter an alphabet")
if n in "aeiou AEIOU":
    print("vowel")
else:
    print("consonant")'''
    
#5
'''n=2.19e14
m=4.68e14

growth=m-n
percentage=(growth/n)*100
print("percentage of bacterial growth=",percentage)'''

#6
'''months=int(input("enter no. of months:"))
years=months//12
remaining_months=months%12

print("years=",years)
print("months=",remaining_months)'''

#8
'''cost=int(input("enter cost:"))
reverse=int(input("enter reverse:"))
if reverse >cost:
    print("profit")
elif reverse<cost:
    print("loss")
else:
    print("Break even")'''
    
#9
'''n=int(input("enter no. of widget:"))
if n<100:
    cost=n*0.25
else:
    cost=n*0.20
    
print("total cost=",cost)'''

#10
'''pounds=int(input("enter no.of pounds:"))
cash=int(input("enter amount of cash:"))

cost=pounds*2.50
if cash>=cost:
    change=cash-cost
    print("change=",format(change,"2f"))
else:
    more=cost-cash
    print("you own",format(more,"2f"))'''
    
#11
'''n = int(input("enter first no.:"))
m = int(input("enter second no.:"))
s = int(input("enter third no.:"))

if n>m:
    if n>s:
        largest=n
    else:
        largest=s
else:
    if m>s:
        largest=m
    else:
        largest=s
print("largest number",largest)'''

#12
'''n=int(input("enter basic salary:"))
m=0.20*n
s=0.05*n
o=0.10*n
total_salary= n+m+s+o
print("m=",m)
print("s=",s)
print("o=",o)
print("total_salary=",total_salary)'''

#13
'''n=int(input("enter gross salary"))
if n<300000:
    tax=0
    slab="0%"
elif n<=1000000:
    tax=0.10*n
    slab="10%"
elif n<=2500000:
    tax=0.20*n
    slab="20%"
else:
    tax=0.30*n
    slab="30%"
print("income tax slab=",slab)
print("incometax=",tax)'''

#14
'''n=int(input("enter taxable income:"))
if n<=20000:
  tax=0.02*n
elif n<=50000:
  tax=400+0.025*(n-20000)
else:
    tax=1150+0.035*(n-50000)
print("tax=",tax)'''


        
    
    
    
    
    

