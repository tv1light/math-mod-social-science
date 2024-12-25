from scenarios.pandemic_scenario import pandemic_scenario
from scenarios.catastrophe_scenario import catastrophe_scenario
from scenarios.default_scenario import default_scenario
from utils.plot_utils import plot_population, plot_gdp, plot_literacy


def main():
    choice_c = 1
    while choice_c == 1:
        print("Выберите сценарий для анализа:")
        print("1. Нормальное развитие")
        print("2. Пандемия")
        print("3. Глобальная катастрофа")
        choice = input("Введите номер сценария: ")

        if choice == "1":
            sol = default_scenario()
            title = "Сценарий: Нормальное развитие"
            t, y = sol.t, sol.y
        elif choice == "2":
            t, y = pandemic_scenario()
            title = "Сценарий: Пандемия"
        elif choice == "3":
            t, y = catastrophe_scenario()
            title = "Сценарий: Глобальная катастрофа"
        else:
            print("Неверный выбор!")
            return

        N, S, l = y

        # Построение графиков
        print(f"Результаты для {title}")
        plot_population(t, N)
        plot_gdp(t, S)
        plot_literacy(t, l)
        choice_c = input("Продолжить: ")


if __name__ == "__main__":
    main()
