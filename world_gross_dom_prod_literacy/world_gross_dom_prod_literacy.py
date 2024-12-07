import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Параметры модели
a = 1.085e-5  # ($ * год)^(-1)
b = 6.51e-12  # (чел * год)^(-1)
c = 8.2e-6    # ($ * год)^(-1)
m = 420       # $

# Начальные данные
N0 = 170000000  # чел
S0 = 17.47      # $
l0 = 0.052      # доля (от 0 до 1)

# Временной интервал
t_span = (1, 2050)
t_eval = np.linspace(t_span[0], t_span[1], 2050)

# Определение системы уравнений
def model(t, y):
    N, S, l = y
    dN_dt = a * S * N * (1 - l)
    dS_dt = b * N * S
    dl_dt = c * S * l * (1 - l)
    return [dN_dt, dS_dt, dl_dt]

# Решение системы
def solve_system():
    return solve_ivp(model, t_span, [N0, S0, l0], t_eval=t_eval)

# Функция для построения графиков
def plot_results(sol):
    t = sol.t
    N, S, l = sol.y

    # Численность населения
    plt.figure(figsize=(10, 6))
    plt.plot(t, N / 1e6, label="N(t) Численность населения (млн чел.)", color="blue")
    plt.title("Динамика численности населения")
    plt.xlabel("Время (лет)")
    plt.ylabel("Численность населения (млн чел.)")
    plt.grid()
    plt.legend()
    plt.show()

    # ВВП на душу населения
    plt.figure(figsize=(10, 6))
    plt.plot(t, S, label="S(t) (ВВП на душу населения)", color="green")
    plt.title("Динамика ВВП на душу населения")
    plt.xlabel("Время (лет)")
    plt.ylabel("ВВП на душу населения ($)")
    plt.grid()
    plt.legend()
    plt.show()

    # Доля грамотного населения
    plt.figure(figsize=(10, 6))
    plt.plot(t, l, label="l(t) (доля грамотного населения)", color="red")
    plt.title("Динамика грамотности населения")
    plt.xlabel("Время (лет)")
    plt.ylabel("Доля грамотного населения, %")
    plt.grid()
    plt.legend()
    plt.show()

    # Логарифмический график численности населения
    plt.figure(figsize=(10, 6))
    plt.plot(t, N / 1e6, label="N(t) Численность населения (млн чел.)", color="blue")
    plt.yscale('log')
    plt.title("Динамика численности населения (логарифмический масштаб)")
    plt.xlabel("Время (лет)")
    plt.ylabel("Численность населения (млн. чел.)")
    plt.grid(which='both', linewidth=0.5)
    plt.legend()
    plt.show()

    # Логарифмический график ВВП на душу населения
    plt.figure(figsize=(10, 6))
    plt.plot(t, S, label="S(t) (ВВП на душу населения)", color="green")
    plt.yscale('log')
    plt.title("Динамика ВВП на душу населения")
    plt.xlabel("Время (лет)")
    plt.ylabel("ВВП на душу населения ($)")
    plt.grid(which='both', linewidth=0.5)
    plt.legend()
    plt.show()

    # Логарифмический график доли грамотного населения
    plt.figure(figsize=(10, 6))
    plt.plot(t, l, label="l(t) (доля грамотного населения)", color="red")
    plt.yscale('log')
    plt.title("Динамика грамотности населения (логарифмическая шкала по оси времени)")
    plt.xlabel("Время (лет, логарифмическая шкала)")
    plt.ylabel("Доля грамотного населения")
    plt.legend()
    plt.show()

# Основная функция
def main():
    sol = solve_system()

    # Вывод численных значений
    time_points = [0, 10, 25, 50, 75, 100, 200, 300, 400, 500, 1000, 1500, 1800, 1900, 2000]  # Точки времени для вывода
    indices = [np.argmin(np.abs(sol.t - t)) for t in time_points]
    print("Численные результаты:")
    for i, t_point in enumerate(time_points):
        idx = indices[i]
        N_val = sol.y[0][idx]
        S_val = sol.y[1][idx]
        l_val = sol.y[2][idx]
        print(f"t = {t_point:.1f} лет: N = {N_val:.4f}, S = {S_val:.4f}, l = {l_val:.4f}")

    plot_results(sol)

if __name__ == "__main__":
    main()
