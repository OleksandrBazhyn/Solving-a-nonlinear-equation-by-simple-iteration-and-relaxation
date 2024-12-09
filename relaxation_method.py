import numpy as np
from prettytable import PrettyTable

def f(x):
    value = x**2 + 5 * np.sin(x) - 1
    return max(min(value, 10**10), -10**10)  # обмеження значень

def f_prime(x):
    value = 2 * x + 5 * np.cos(x)
    return max(min(value, 10**10), -10**10)  # обмеження значень

def relaxation_method(x0, tau=0.1, tol=1e-4, max_iter=100):
    print("Метод релаксації")
    f_prime_value = f_prime(x0)
    
    if (f_prime_value > 0.0):
        t = PrettyTable(["Ітерація", "Значення x - tau * f(x)"])
        print(f"Наближене значення: ", x0)
        x = x0
        for i in range(max_iter):
            x_new = x + tau * f(x)

            t.add_row([i + 1, x_new])

            if abs(x_new - x) < tol:
                print(t)
                return x_new, i + 1
            x = x_new

        print(t)
        return None, max_iter
    else:
        t = PrettyTable(["Ітерація", "Значення x + tau * f(x)"])
        print(f"Наближене значення: ", x0)
        x = x0
        for i in range(max_iter):
            x_new = x + tau * f(x)

            t.add_row([i + 1, x_new])

            if abs(x_new - x) < tol:
                print(t)
                return x_new, i + 1
            x = x_new

        print(t)
        return None, max_iter

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
    print(f'Max: f\'({x_at_max}): {max_value}')

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
    print(f'Min: f\'({x_at_min}): {min_value}')


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
tau = 0.12

x0 = -3
initial_guesses = [-3.0, 0]

# Знаходження коренів методом релаксації
root_r_value, steps_r_value = relaxation_method(x0, tau)

print(f"Метод релаксації: найбільший за модулем від'ємний корінь = {root_r_value:.4f}, ітерацій = {steps_r_value}")

M1(a, b, f_prime, step)
m1(a, b, f_prime, step)