w=int(input())
b=int(input())
if w%100!=0:
    print("Invalid input")
elif b<(w+10):
    print("Insufficient balance")
else:
    print(b-(w+10))
