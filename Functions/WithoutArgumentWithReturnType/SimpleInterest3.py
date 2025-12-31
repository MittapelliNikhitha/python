def simple_interest():
    p = float(input("Enter principal: "))
    t = float(input("Enter time: "))
    r = float(input("Enter rate: "))
    return (p * t * r) / 100

si = simple_interest()
print("Simple Interest is:", si)
