import numpy as np
import dash_core_components as dcc
import plotly.graph_objects as go
from scipy.integrate import odeint

def sir_model_with_distancing(y, t, N, beta, gamma, delta):
    S, I, R = y
    Sdot = - (1 - delta) * beta * S * I / N
    Idot = (1 - delta) * (beta * S * I) / N - gamma * I
    Rdot = gamma * I
    return Sdot, Idot, Rdot

@np.vectorize
def solve(delta, R0=2.67, N=1e4, initial_fraction=0.001, days=90, tau=8.5):
    I_0 = initial_fraction * N
    R_0 = 0.0
    S_0 = N - I_0 - R_0
    gamma = 1/tau
    beta = R0 * gamma
    t = np.linspace(0, days, days)

    y_0 = S_0, I_0, R_0

    return odeint(sir_model_with_distancing, y_0, t, args=(N, beta, gamma, delta)).T
