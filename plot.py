#!/usr/bin/env python

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Load our matplotlibrc config. (Not done automagically to keep things clear.)
matplotlib.rc_file("../matplotlibrc")


def main():
    solutions_2 = np.load("solutions_2.npy")
    solutions_4 = np.load("solutions_4.npy")

    fig, axs = plt.subplots(2, 1)
    bins = np.linspace(-1, 3, 100)
    for i, sym, ax in zip([0, 1], "xy", axs, strict=False):
        values_2 = np.ravel(solutions_2[:, i::2])
        ax.hist(values_2, bins, histtype="step")
        values_4 = np.ravel(solutions_4[:, i::2])
        ax.hist(values_4, bins, histtype="step")
        ax.set_xlabel(f"{sym}")
    fig.savefig("hists.png")


if __name__ == "__main__":
    main()
