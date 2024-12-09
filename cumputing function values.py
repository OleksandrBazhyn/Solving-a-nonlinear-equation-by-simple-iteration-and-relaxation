import numpy as np
import matplotlib.pyplot as plt

# Визначення функції f(x)
def f(x):
    return x**2 + 5 * np.sin(x) - 1

# Визначення функції g(x)
def g(x):
    first = -1 * np.divide(1, (5 * np.cos(x) + 2 * x))
    value = x + first * f(x)
    return np.clip(value, -10**10, 10**10)  # обмеження значень

# Похідна g'(x)
def g_prime(x):
    sinX = np.sin(x)
    cosX = np.cos(x)
    x2 = x ** 2
    first = 25 * (sinX ** 2) + 5 * (x2 - 3) * sinX - 2 * x2 + 2
    second = 25 * cosX + 20 * x * cosX + 4 * x2
    value = -1 * np.divide(first, second)
    return np.clip(value, -10**10, 10**10)  # обмеження значень

# Створюємо масив значень x
x_values = np.linspace(-10, 10, 400)

# Обчислюємо значення функцій
f_values = f(x_values)
g_values = g(x_values)
g_prime_values = g_prime(x_values)

# Пошук інтервалів, де функція f(x) змінює знак
sign_changes = np.where(np.diff(np.sign(f_values)))[0]

# Виведення інтервалів
for change in sign_changes:
    print(f"Корінь лежить в проміжку між {x_values[change]} та {x_values[change + 1]}")

# Побудова графіків
plt.figure(figsize=(10, 6))

# Графік f(x)
plt.plot(x_values, f_values, label="f(x)", color="blue")

# Графік g(x)
plt.plot(x_values, g_values, label="g(x)", color="green")

# Графік похідної g'(x)
plt.plot(x_values, g_prime_values, label="g'(x)", color="orange", linestyle="--")

# Вісь y=0 для наочності
plt.axvline(0, color='grey', linestyle='--')

# Вісь x=0 для наочності
plt.axhline(0, color='grey', linestyle='--')

# Налаштування графіка
plt.legend()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Графіки f(x), g(x) та g\'(x)')
plt.grid(True)
plt.show()
