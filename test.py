def test():
    a=int(input("input an integer:\n"))
    b=int(input("input another integer:\n"))

    if a>b:
        return a-b
    elif a<=b and a>0:
        return b-a
    else:
        return a+b
print(test())