import matplotlib.pyplot as plt
import numpy as np


def plot_population(t, N):
    N = np.array(N)

    plt.figure(figsize=(10, 6))
    plt.plot(t, N, label="Численность населения (млн чел.)", color="blue")
    plt.title("Динамика численности населения")
    plt.xlabel("Время (лет)")
    plt.ylabel("Численность населения (млн чел.)")
    plt.grid()
    plt.legend()
    plt.show()

def plot_gdp(t, S):
    S = np.array(S)


    plt.figure(figsize=(10, 6))
    plt.plot(t, S / 1e4, label="ВВП на душу населения ($)", color="green")
    plt.title("Динамика ВВП на душу населения")
    plt.xlabel("Время (лет)")
    plt.ylabel("ВВП ($)")
    plt.grid()
    plt.legend()
    plt.show()

def plot_literacy(t, l):
    l = np.array(l)
    plt.figure(figsize=(10, 6))
    plt.plot(t, l, label="Доля грамотного населения", color="red")
    plt.title("Динамика грамотности населения")
    plt.xlabel("Время (лет)")
    plt.ylabel("Доля грамотного населения")
    plt.grid()
    plt.legend()
    plt.show()
