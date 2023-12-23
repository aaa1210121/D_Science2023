import numpy as np
import matplotlib.pyplot as plt


def transition_matrix(n):
    # TODO_D1

    P = np.zeros((n, n))

    state = np.arange(n)

    cond0 = state == 0
    P[cond0, state[cond0] + 1] = 0.6

    cond1 = (state < n / 2) & (state > 0)
    P[cond1, state[cond1] + 1] = 0.6
    P[cond1, state[cond1] - 1] = 0.35
    P[cond1, 0] = 0.05
    P[state[cond0] + 1, cond0] = 0.4

    cond2 = (state >= n / 2) & (state < n - 1)
    P[cond2, state[cond2] + 1] = 0.5
    P[cond2, state[cond2] - 1] = 0.4
    P[cond2, 0] = 0.1

    P[0, 0] = 0.4
    cond3 = state == (n - 1)
    P[n - 1, n - 1] = 0.5
    P[cond3, state[cond3] - 1] = 0.4
    P[cond3, 0] = 0.1

    return P


def propagate(x0, P, k):
    xk = None
    xk = x0 @ np.linalg.matrix_power(P, k)
    # TODO_D2

    return xk


def create_sample(s0, P, k):
    trajectories = []
    # # TODO_D6
    prev_state = s0
    for i in range(k + 1):
        trajectories.append(prev_state)
        current_state = np.random.choice(np.arange(10), p=P[prev_state])
        prev_state = current_state
    return trajectories


def plot_distribution(x):
    plt.plot(x)
    plt.xticks(np.arange(0, len(x), step=1))
    plt.ylim(0, max(x) + 0.1)
    plt.xlabel("State (i)")
    plt.ylabel("Probability")
    plt.title("Probability Distribution")
    plt.savefig("Lab04_D3.png", dpi=150)


def plot_histogram(x):
    plt.hist(x, bins=max(x) + 1, range=(-0.5, max(x) + 0.5))
    plt.xticks(np.arange(0, max(x) + 1, step=1))
    plt.xlabel("State (i)")
    plt.ylabel("Number of smaple")
    plt.title("State Histogram")
    plt.savefig("Lab04_D7.png", dpi=150)


def main():
    P = transition_matrix(n=10)
    # TODO_D3

    x0 = np.zeros(10)
    x0[0] = 1
    x8 = propagate(x0, P, k=8)
    print(x8)
    plot_distribution(x8)

    # TODO_D4

    x11 = propagate(x0, P, k=11)
    print(x11)
    plot_distribution(x11)

    # TODO_D5
    x0 = np.random.rand(10)
    x0 = x0 / np.sum(x0)
    print(x0)

    # TODO_D6
    a = create_sample(s0=0, P=P, k=20)
    print(a)

    # TODO_D7

    last_steps = []
    for i in range(1000):
        sample = create_sample(s0=0, P=P, k=8)
        state_last = sample[-1]
        last_steps.append(state_last)
    plot_histogram(last_steps)


if __name__ == "__main__":
    main()
