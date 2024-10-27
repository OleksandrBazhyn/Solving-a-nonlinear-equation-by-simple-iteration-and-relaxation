import math
from prettytable import PrettyTable

def g(x):
    return -math.sqrt(1 - 5 * math.sin(x))

def f(x):
    return x**2 + 5 * math.sin(x) - 1

def simple_iteration(x0, tol=1e-4, max_iter=1000):
    print("Метод простої ітерації")
    t = PrettyTable(["Крок", "Значення g(x)"])
    print(f"Наближене значення: ", x0)
    x = x0
    for i in range(max_iter):
        x_new = g(x)
        t.add_row([i+1,x_new])
        if abs(x_new - x) < tol:
            print(t)
            return x_new, i+1
        x = x_new
    print(t)
    return x, max_iter

def relaxation_method(x0, alpha=0.1, tol=1e-4, max_iter=1000):
    print("Метод релаксації")
    t = PrettyTable(["Крок", "Значення x - alpha * f(x)"])
    print(f"Наближене значення: ", x0)
    x = x0
    for i in range(max_iter):
        x_new = x - alpha * f(x)
        t.add_row([i+1,x_new])
        if abs(x_new - x) < tol:
            print(t)
            return x_new, i+1
        x = x_new
    print(t)
    return x, max_iter

# Початкове наближення
x0 = -1.0

# Знаходження кореня методом простої ітерації
root_si, steps_si = simple_iteration(x0)

# Знаходження кореня методом релаксації
root_rel, steps_rel = relaxation_method(x0)

print(f"Метод простої ітерації: корінь = {root_si:.4f}, кроків = {steps_si}")
print(f"Метод релаксації: корінь = {root_rel:.4f}, кроків = {steps_rel}")
