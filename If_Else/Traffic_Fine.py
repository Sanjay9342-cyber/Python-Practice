S=int(input())
if S<0:
    print("Invalid input")
elif S<=50:
    print("No fine")
elif S<=70:
    print(50)
elif S<=100:
    print(100)
else:
    print(200)
