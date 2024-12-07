from .base_model import solve_system

def catastrophe_scenario():
    # Параметры нормального сценария (до катастрофы)
    normal_params = (1.085e-5, 6.51e-12, 8.2e-6)
    catastrophe_params = (normal_params[0] * 0.5, normal_params[1] * 1.1, normal_params[2] * 0.7)  # Измененные параметры

    # Начальные условия
    N0, S0, l0 = 170000000, 17.47, 0.052
    initial_conditions = [N0, S0, l0]

    # Разделение временного интервала на две части: до и после катастрофы
    t_split = 1951  # Год наступления катастрофы
    t_span_pre = (1, t_split)
    t_span_post = (t_split, 2050)
    t_eval_pre = range(t_span_pre[0], t_span_pre[1] + 1)
    t_eval_post = range(t_span_post[0], t_span_post[1] + 1)

    # Решение до катастрофы
    sol_pre = solve_system(initial_conditions, t_span_pre, t_eval_pre, normal_params)

    # Используем конечные значения первого этапа как начальные условия второго этапа
    final_conditions_pre = [sol_pre.y[0, -1] // 1.5, sol_pre.y[1, -1] // 1.5, sol_pre.y[2, -1] // 1.5]

    # Решение после катастрофы
    sol_post = solve_system(final_conditions_pre, t_span_post, t_eval_post, catastrophe_params)

    # Объединение результатов
    t_combined = list(sol_pre.t) + list(sol_post.t)
    y_combined = [
        list(sol_pre.y[0]) + list(sol_post.y[0]),  # Численность населения
        list(sol_pre.y[1]) + list(sol_post.y[1]),  # ВВП на душу населения
        list(sol_pre.y[2]) + list(sol_post.y[2]),  # Грамотность
    ]

    return t_combined, y_combined
