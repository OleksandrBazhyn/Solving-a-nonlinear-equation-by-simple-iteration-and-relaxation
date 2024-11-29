import numpy as np
from prettytable import PrettyTable

def g(x):
    first = np.divide(1, (1 + x**2))
    second = x + 5 * np.sin(x) - 1
    value = x + first * second
    return max(min(value, 10**10), -10**10)  # обмеження значень

# g'(x)
def g_prime(x):
    first = 10 * x * np.sin(x)
    second = 5 * (x**2 + 1)
    third = np.cos(x)
    fourth = first - second * third - 4 * x
    fifth = x**4 + 2 * x**2 + 1
    value = np.divide(fourth, fifth)
    return max(min(value, 10**10), -10**10)  # обмеження значень

def f(x):
    value = x**2 + 5 * np.sin(x) - 1
    return max(min(value, 10**10), -10**10)  # обмеження значень

def f_prime(x):
    value = 2 * x + 5 * np.cos(x)
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
b = 0  # верхня межа
step = 0.1  # крок для дискретизації

x0 = -3
initial_guesses = [-3.0, 0]

# Знаходження кореня методом простої ітерації
root_si, steps_si = simple_iteration(x0)

M1(a, b, g_prime, step)
m1(a, b, g_prime, step)