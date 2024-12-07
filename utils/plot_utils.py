import matplotlib.pyplot as plt

def plot_population(t, N):
    plt.figure(figsize=(10, 6))
    plt.plot(t, N, label="Численность населения (млн чел.)", color="blue")
    plt.title("Динамика численности населения")
    plt.xlabel("Время (лет)")
    plt.ylabel("Численность населения (млн чел.)")
    plt.grid()
    plt.legend()
    plt.show()

def plot_gdp(t, S):
    plt.figure(figsize=(10, 6))
    plt.plot(t, S, label="ВВП на душу населения ($)", color="green")
    plt.title("Динамика ВВП на душу населения")
    plt.xlabel("Время (лет)")
    plt.ylabel("ВВП ($)")
    plt.grid()
    plt.legend()
    plt.show()

def plot_literacy(t, l):
    plt.figure(figsize=(10, 6))
    plt.plot(t, l, label="Доля грамотного населения", color="red")
    plt.title("Динамика грамотности населения")
    plt.xlabel("Время (лет)")
    plt.ylabel("Доля грамотного населения")
    plt.grid()
    plt.legend()
    plt.show()
