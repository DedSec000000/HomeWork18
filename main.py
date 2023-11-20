x = int(input("Give me a number to calculate: "))
def F(x):
    if x == 0 or x == 1:
        return x
    elif x < 0:
        print("Sorry, the number is negative.")
    else:
        return x * F(x - 1)
result = F(x)
print("factorial is ",F(x))
















