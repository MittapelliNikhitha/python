def simple_interest(p, t, r):
    si = (p * t * r) / 100
    print("Simple Interest is:", si)

p = float(input("Enter principal: "))
t = float(input("Enter time: "))
r = float(input("Enter rate: "))

simple_interest(p, t, r)
