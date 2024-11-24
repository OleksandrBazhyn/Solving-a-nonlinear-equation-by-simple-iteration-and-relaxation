import numpy as np
import matplotlib.pyplot as plt

# Визначення функції f(x)
def f(x):
    return x**2 + 5 * np.sin(x) - 1

# Визначення g(x) = sqrt(1 - 5 * sin(x))
def g(x):
    # Перевірка, щоб значення під коренем були невід'ємними
    with np.errstate(invalid='ignore'):
        return np.sqrt(1 - 5 * np.sin(x))

# Похідна g'(x) = -5 * cos(x) / (2 * sqrt(1 - 5 * sin(x)))
def g_derivative(x):
    with np.errstate(divide='ignore', invalid='ignore'):
        denominator = 2 * np.sqrt(1 - 5 * np.sin(x))
        numerator = -5 * np.cos(x)
        result = numerator / denominator
        result[denominator == 0] = np.nan  # Уникнення ділення на 0
        return result

# Створюємо масив значень x
x_values = np.linspace(-10, 10, 400)

# Обчислюємо значення функцій
f_values = f(x_values)
g_values = g(x_values)
g_derivative_values = g_derivative(x_values)

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
plt.plot(x_values, g_values, label="g(x) = sqrt(1 - 5*sin(x))", color="green")

# Графік похідної g'(x)
plt.plot(x_values, g_derivative_values, label="g'(x)", color="orange", linestyle="--")

# Вісь y=0 для наочності
plt.axhline(0, color='red', linestyle='--', label='y=0')

# Налаштування графіка
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Графіки f(x), g(x) та g\'(x)')
plt.grid(True)
plt.show()
