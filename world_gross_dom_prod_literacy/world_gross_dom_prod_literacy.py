import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Параметры модели
a = 1.085e-5  # ($ * год)^(-1)
b = 6.51e-12  # (чел * год)^(-1)
c = 8.2e-6    # ($ * год)^(-1)
m = 420       # $

# Начальные данные
N0 = 170_000_000  # чел
S0 = 17.47        # $
l0 = 0.052        # доля (от 0 до 1)

# Временной интервал (например, 0 до 100 лет)
t_span = (0, 2000)
t_eval = np.linspace(t_span[0], t_span[1], 1000)

# Определение системы уравнений
def model(t, y):
    N, S, l = y
    dN_dt = a * S * N * (l - l)  # Это всегда 0
    dS_dt = b * N * S
    dl_dt = c * S * l * (1 - l)
    return [0, dS_dt, dl_dt]

# Решение системы
sol = solve_ivp(model, t_span, [N0, S0, l0], t_eval=t_eval)

# Вывод численных значений в определённые моменты времени
time_points = [0, 10, 25, 50, 75, 100]  # Точки времени для вывода
indices = [np.argmin(np.abs(sol.t - t)) for t in time_points]
print("Численные результаты:")
for i, t in enumerate(time_points):
    print(f"t = {t:.1f} лет: S = {sol.y[1][indices[i]]:.4f}, l = {sol.y[2][indices[i]]:.4f}")

# Построение графиков
plt.figure(figsize=(12, 10))

# Графики S(t) и l(t) в линейном масштабе
plt.subplot(2, 1, 1)
plt.plot(sol.t, sol.y[1], label="S(t) (ВВП на душу населения)", color="green")
plt.plot(sol.t, sol.y[2], label="l(t) (доля грамотного населения)", color="red")
plt.title("Динамика ВВП и грамотности (линейный масштаб)")
plt.xlabel("Время (лет)")
plt.ylabel("Значения")
plt.legend()
plt.grid()

# Графики S(t) и l(t) в логарифмическом масштабе
plt.subplot(2, 1, 2)
plt.semilogy(sol.t, sol.y[1], label="S(t) (ВВП на душу населения)", color="green")
plt.semilogy(sol.t, sol.y[2], label="l(t) (доля грамотного населения)", color="red")
plt.title("Динамика ВВП и грамотности (логарифмический масштаб)")
plt.xlabel("Время (лет)")
plt.ylabel("Значения (лог)")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
