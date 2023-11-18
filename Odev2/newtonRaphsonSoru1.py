x0 = 1
root = 0
counter = 0
iterationSize = 4

def f(x):
    return x**(1/3);

def f2(x):
    return (x**(-2/3))/3;

def calculate(x):
    global root, counter, iterationSize

    root = x - f(x) / f2(x)
    counter += 1

    print(f"{counter}. Kök Tahmini: {root}");


    if counter != iterationSize:
        calculate(root)

calculate(x0)
