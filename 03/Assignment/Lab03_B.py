import numpy as np
from random import randrange

# b-1

np.set_printoptions(suppress=True) #, formatter={"float": "{:0.1f}".format}
b_1 = np.arange(5, -5.2, -0.2)
print(b_1)

# b-2

a = np.arange(0, 1.01, 0.01)
b_2 = np.power(10, a)
print(b_2)

# b-3

b_3 = np.arange(1, 101).reshape(10, 10, order="F")
print(b_3)

# b_4

b_4 = np.arange(1, 13).reshape(12, 1) * np.arange(1, 13)
print(b_4)

A = None

B = None

C = None

D = None

def E(X):
    return X[::2, ::2]


def F(X):
    return X[1:-1, 1:-1]


def G(X):
    # The shape of return value will be (M, 2)
    above = np.diag(X, k=1)
    below = np.diag(X, k=-1)
    return np.column_stack((above, below))


# Do NOT modifiy the main function
def main():
    print('A: \n', A, '\n')
    print('B: \n', B, '\n')
    print('C: \n', C, '\n')
    print('D: \n', D, '\n')

    M = randrange(3, 8)
    X = np.random.randint(10, size=(M, M))

    print('X: \n', X, '\n')
    print('E: \n', E(X), '\n')
    print('F: \n', F(X), '\n')
    print('G: \n', G(X), '\n')


if __name__ == "__main__":
    main()