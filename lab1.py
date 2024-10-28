import numpy as np
from prettytable import PrettyTable

def g(x):
    value = np.sqrt(1 - 5 * np.sin(x))
    return max(min(value, 10**10), -10**10)  # обмеження значень

def f(x):
    value = x**2 + 5 * np.sin(x) - 1
    return max(min(value, 10**10), -10**10)  # обмеження значень

# g'(x)
def g_prime(x):
    cosX = np.cos(x)
    sinX = np.sin(x)
    first = (5 * cosX)
    second = (2 * np.sqrt(1 - 5 * sinX))
    value = - first/second
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

def relaxation_method(x0, tau=0.1, tol=1e-4, max_iter=100):
    print("Метод релаксації")
    
    if (x0 >= 0):
        t = PrettyTable(["Крок", "Значення x - tau * f(x)"])
        print(f"Наближене значення: ", x0)
        x = x0
        for i in range(max_iter):
            x_new = x - tau * f(x)

            t.add_row([i + 1, x_new])

            if abs(x_new - x) < tol:
                print(t)
                return x_new, i + 1
            x = x_new

        print(t)
        return None, max_iter
    else:
        t = PrettyTable(["Крок", "Значення x + tau * f(x)"])
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
    if np.abs(max_value) > 1:
        print("Достатні умови збіжності не виконуються.")
    return max_value, x_at_max

# Задаємо проміжок [a, b] та крок
a = -3  # нижня межа
b = 3  # верхня межа
step = 0.1  # крок для дискретизації

x0 = -2.5
initial_guesses = [-3.0, 3.0]

# Знаходження коренів методом релаксації
root_r_value1, steps_r_value1 = relaxation_method(initial_guesses[0])
root_r_value2, steps_r_value2 = relaxation_method(initial_guesses[1])

# Знаходження кореня методом простої ітерації
root_si, steps_si = simple_iteration(x0)

# Викликаємо функцію для знаходження максимуму
max_value, x_at_max = verif_sufficient_convergence_conditions(a, b, g_prime, step)

print(f"Максимальне значення g'(x) на проміжку [{a}, {b}]: {max_value} при x = {x_at_max}")
print(f"Метод простої ітерації: корінь = {root_si:.4f}, кроків = {steps_si}")
print(f"Метод релаксації: найбільший за модулем від'ємний корінь = {root_r_value1:.4f}, кроків = {steps_r_value1}")
