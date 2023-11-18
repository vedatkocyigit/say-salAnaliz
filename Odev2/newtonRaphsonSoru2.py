e = 2.71828182845904
x0 = 2
root = 0
counter = 0
iterationSize = 4

def f(x):
    global e
    return (4 * e**(-0.5 * x)) - x

def f2(x):
    global e;
    return -2 * (e**(-0.5 * x)) - 1

def calculate(x):
    global root, counter, iterationSize

    root = x - f(x) / f2(x)
    counter += 1

    print(f"{counter}. Kök Tahmini: {root}")


    if counter != iterationSize:
        calculate(root)

calculate(x0)
