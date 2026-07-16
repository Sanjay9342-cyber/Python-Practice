S=int(input())
P=int(input())
Y=int(input())
if P>100:
    print("Invalid input")
elif P>=90 and Y>=5:
    print(int(S*0.2))
elif P>=75 and Y>=3:
    print(int(S*0.10))
else:
    print("No bonus")
