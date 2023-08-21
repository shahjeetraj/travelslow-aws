exp = input("Expression: ")
exp = exp.strip().lower().replace("  "," ")
spl_exp = exp.split(" ")
x = float(spl_exp[0])
y = spl_exp[1]
z = float(spl_exp[2])

if y == "*":
    print(x * z)
elif y == "/":
    print(x / z)
elif y == "+":
    print(x + z)
elif y == "-":
    print(x - z)
else: print("Invalid Expression")