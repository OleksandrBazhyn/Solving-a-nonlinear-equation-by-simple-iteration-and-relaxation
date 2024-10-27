import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2 + 5 * np.sin(x) - 1

# Створюємо масив значень x
x_values = np.linspace(-10, 10, 400)
# Обчислюємо значення функції f(x) для кожного x
y_values = f(x_values)

# Пошук інтервалів, де функція змінює знак
sign_changes = np.where(np.diff(np.sign(y_values)))[0]

# Виведення інтервалів
for change in sign_changes:
    print(f"Корінь лежить в проміжку між {x_values[change]} та {x_values[change + 1]}")

# Побудова графіка
plt.plot(x_values, y_values, label="f(x)")
plt.axhline(0, color='red', linestyle='--', label='y=0')
plt.legend()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Графік f(x)')
plt.grid(True)
plt.show()
