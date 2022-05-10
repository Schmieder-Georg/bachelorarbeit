from cProfile import label
from turtle import color
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
plt.style.use('ggplot')


def plot_all(data, x):
    print(data[13:26, 0])
    fig = plt.figure("MWZ", dpi=300)
    ax = fig.add_subplot()
    ax.scatter(x, data[0:13, 0], label="S1")
    ax.scatter(x, data[0:13, 1], label="M0")
    ax.scatter(x, data[0:13, 2], label="M1")
    ax.scatter(x, data[0:13, 3], label="T0")
    ax.scatter(x, data[0:13, 4], label="T1")
    ax.scatter(x, data[0:13, 5], label="T2")

    ax.legend()
    plt.xticks(x)
    ax.set_title(r'$M(WZ)$')
    ax.set_xlabel("GM Model [GeV]")
    ax.set_ylabel(r'$S = \frac{Z_{GM}(0)}{Z_{EFT}(0)}$')
    plt.savefig(
        "E:/Georg/Dokumente/Studium/bachelorarbeit/Plots/gm_relevanze/MWZ_all")


def plot_comp(data, x):
    operator = ["S1", "M0", "M1", "T0", "T1", "T2"]
    for i in range(6):
        fig = plt.figure("MWZ ", dpi=300)
        plt.scatter(x, data[0:13, i], label=r'$1 \times \sigma_{GM}$')
        plt.scatter(x, data[26:39, i], label=r'$2 \times \sigma_{GM}$')
        plt.scatter(x, data[52:65, i], label=r'$0.5 \times \sigma_{GM}$')
        plt.legend()
        plt.xticks(x)
        plt.title(r'$M(WZ)$ cross-section comparison for '+operator[i])
        plt.xlabel("GM Model [GeV]")
        plt.ylabel(r'$S = \frac{Z_{GM}(0)}{Z_{EFT}(0)}$')
        plt.savefig(
            "E:/Georg/Dokumente/Studium/bachelorarbeit/Plots/gm_relevanze/MWZ_comparision_"+operator[i])
        plt.clf()


def plot_op(data, x):
    operator = ["S1", "M0", "M1", "T0", "T1", "T2"]
    for i in range(6):
        fig = plt.figure("MTWZ ", dpi=300)
        plt.scatter(x, data[13:26, i], label=operator[i], color='tab:blue')
        plt.legend()
        plt.xticks(x)
        plt.title(r'$M(WZ)$ for '+operator[i])
        plt.xlabel("GM Model [GeV]")
        plt.ylabel(r'$S = \frac{Z_{GM}(0)}{Z_{EFT}(0)}$')
        plt.savefig(
            "E:/Georg/Dokumente/Studium/bachelorarbeit/Plots/gm_relevanze/MTWZ_op_"+operator[i])
        plt.clf()


def main():
    x = [225, 275, 325, 375, 425, 475, 525,
         550, 600, 700, 800, 900, 1000]
    x = list(map(str, x))
    file_pandas = pd.read_csv(
        "E:/Georg/Dokumente/Studium/bachelorarbeit/Plots/gm_relevanze/GM_relevanze.csv", sep=",", header=None)
    data = file_pandas.to_numpy()

    plot_comp(data, x)


if __name__ == "__main__":
    main()
