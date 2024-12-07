from scipy.integrate import solve_ivp

# Основная модель
def model(t, y, params):
    a, b, c = params
    N, S, l = y
    dN_dt = a * S * N * (1 - l)
    dS_dt = b * N * S
    dl_dt = c * S * l * (1 - l)
    return [dN_dt, dS_dt, dl_dt]

# Решение системы
def solve_system(initial_conditions, t_span, t_eval, params):
    return solve_ivp(model, t_span, initial_conditions, t_eval=t_eval, args=(params,))
