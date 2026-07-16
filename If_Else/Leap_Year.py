Y=int(input())
if Y<0:
    print("Invalid Year")
elif Y%400==0 or Y%4==0 and Y%100!=0:
    print("Leap Year")
else:
    print("Not a Leap Year")
