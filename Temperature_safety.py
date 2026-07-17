n=int(input())
if n<0:
    print("Invalid input")
else:
    m=tuple(map(int, input().split()))
    unsafe=False
    for i in m:
        if i>=100:
            unsafe=True
            break
    if unsafe:
        print("Unsafe")
    else:
        print("Safe")
