A=int(input())
B=int(input())
C=int(input())
if A>B and A>C:
    print("Machine A produces the highest value")
elif B>A and B>C:
    print("Machine B produces the highest value")
elif C>A and C>B:
    print("Machine C produces the highest value")
else:
    print("All machines have equal production value")
