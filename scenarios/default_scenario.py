from .base_model import solve_system

def default_scenario():
    # Параметры нормального сценария
    params = (1.085e-5, 6.51e-12, 8.2e-6)  # a, b, c
    N0, S0, l0 = 170000000, 17.47, 0.052   # Начальные условия
    initial_conditions = [N0, S0, l0]
    t_span = (1, 2050)                     # Временной интервал
    t_eval = range(1, 2051)

    # Решение системы
    sol = solve_system(initial_conditions, t_span, t_eval, params)
    return sol
