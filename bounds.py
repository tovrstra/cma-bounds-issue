#!/usr/bin/env python

from functools import partial
from multiprocessing.pool import Pool

import cma
import numpy as np


class WobblyRosenbrock:
    def __init__(self, ndim, rng, ncos=None):
        self.ndim = ndim
        if ncos is None:
            ncos = ndim
        self.ncos = ncos
        self.vecs = rng.normal(0, 10, (ncos, ndim)) / np.sqrt(ndim)
        self.phases = rng.uniform(0, 2 * np.pi, ncos)

    def __call__(self, pars):
        """Generalized Rosenbrock (uncoupled version) with cosine noise."""
        assert pars.ndim == 1
        assert len(pars) % 2 == 0
        assert pars.size > 0
        a = 1
        b = 100
        eps = 0.1
        x, y = pars.reshape(-1, 2).T
        term_rosen = ((a - x) ** 2 + b * (y - x**2) ** 2).sum()
        term_wobble = eps * np.cos(np.dot(self.vecs, pars) + self.phases).sum()
        return term_rosen + term_wobble


def run(i, bounds, npar):
    rng = np.random.default_rng(42)
    rosenbrock = WobblyRosenbrock(npar, rng)
    x0 = rng.uniform(*bounds, npar)
    # assert rosenbrock(np.ones(len(x0))) == 0.0
    xopt_b, es_b = cma.fmin2(
        rosenbrock,
        x0,
        0.5,
        {
            "bounds": bounds,
            "verb_log": 0,
            "verbose": -9,
        },
    )
    print(f"Done {i}")
    return xopt_b


def main():
    bounds = [-1, 3]
    npar = 28
    with Pool(36) as p:
        solutions = p.map(partial(run, bounds=bounds, npar=npar), range(1000))
    solutions = np.array(solutions)
    np.save("solutions_{bounds[1]-bounds[0]}.npy", solutions, allow_pickle=False)


if __name__ == "__main__":
    main()
