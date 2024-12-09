import numpy as np
from prettytable import PrettyTable

def g(x):
    first = -1 * np.divide(1, (5 * np.cos(x) + 2 * x))
    value = x + first * f(x)
    return max(min(value, 10**10), -10**10)  # обмеження значень

# g'(x)
def g_prime(x):
    sinX = np.sin(x)
    cosX = np.cos(x)
    x2 = x ** 2
    first = 25 * (sinX ** 2) + 5 * (x2 - 3) * sinX - 2 * x2 + 2
    second = 25 * cosX + 20 * x * cosX + 4 * x2
    value = -1 * np.divide(first, second)
    return max(min(value, 10**10), -10**10)  # обмеження значень

def f(x):
    value = x**2 + 5 * np.sin(x) - 1
    return max(min(value, 10**10), -10**10)  # обмеження значень

def simple_iteration(x0, tol=1e-4, max_iter=100):
    print("Метод простої ітерації")
    t = PrettyTable(["Крок", "Значення g(x)"])
    print(f"Наближене значення: ", x0)
    x = x0
    for i in range(max_iter):
        x_new = g(x)
        t.add_row([i + 1, x_new])
        if abs(x_new - x) < tol:
            print(t)
            return x_new, i + 1
        x = x_new
    print(t)
    return x, max_iter

def M1(min_interval_value, max_interval_value, prime_function, step):
    max_value = float('-inf')
    x_at_max = min_interval_value

    x = min_interval_value
    while x <= max_interval_value:
        value = np.abs(prime_function(x))
        if value > max_value:
            max_value = value
            x_at_max = x
        x += step
    print(f'Max: g\'({x_at_max}): {max_value}')

def m1(min_interval_value, max_interval_value, prime_function, step):
    min_value = float('inf')
    x_at_min = min_interval_value

    x = min_interval_value
    while x <= max_interval_value:
        value = np.abs(prime_function(x))
        if value < min_value:
            min_value = value
            x_at_min = x
        x += step
    print(f'Min: g\'({x_at_min}): {min_value}')


def verif_sufficient_convergence_conditions(min_interval_value, max_interval_value, prime_function, step):
    max_value = float('-inf')  # Ініціалізація максимальної змінної
    x_at_max = min_interval_value  # Змінна для збереження x, при якому досягається максимум

    # Дискретизація проміжку і пошук максимуму
    x = min_interval_value
    while x <= max_interval_value:
        value = prime_function(x)  # Викликаємо передану функцію
        if value > max_value:
            max_value = value
            x_at_max = x
        x += step
    if np.abs(max_value) > 0:
        print("Достатні умови збіжності не виконуються.")
    return max_value, x_at_max

# Задаємо проміжок [a, b] та крок
a = -3  # нижня межа
b = -2  # верхня межа
step = 0.1  # крок для дискретизації

x0 = -3

# Знаходження кореня методом простої ітерації
root_si, steps_si = simple_iteration(x0)
print(f'max_xє[{a}, {b}](|-x|) = {root_si}; steps = {steps_si}.')

M1(a, b, g_prime, step)
m1(a, b, g_prime, step)