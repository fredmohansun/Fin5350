import numpy as np


class option(object):

    def __init__(self, S, K, type):
        self.S = S
        self.K = K
        self.t = type
        self.payout = 0
        self.type = 0

    def numtype(self):
        try:
            a = {'c': 1, 'C': 1, 'p': 2, 'P': 2}
            self.type = a[self.t]
        except:
            print("invalid type")

    def get_payout(self):
        if self.type != 1 and self.type != 2:
            self.numtype()
        if self.type == 1:
            self.payout = max(self.S-self.K, 0)
        elif self.type == 2:
            self.payout = max(self.K-self.S, 0)


def main():
    S0 = 41.0
    K = 40.0
    N = 4.0
    T = 1.0
    h = T/N
    sigma = .30
    r = .08
    u = np.exp(r*h+sigma*np.sqrt(h))
    d = np.exp(r*h-sigma*np.sqrt(h))
    pu = (np.exp(r*h)-d)/(u-d)
    pd = 1 - pu
    N = int(N)
    Firstoption = option(S0, K, 'p')
    Tree = np.empty((N, N), dtype=option)
    Tree[0, 0] = Firstoption
    Price = np.zeros((N, N))
    for i in range(1, N):
        for j in range(i):
            Tree[j, i] = option(Tree[j, i-1].S * u, Tree[j, i-1].K,
                                Tree[j, i-1].t)
            Tree[j, i].get_payout()
        Tree[j+1, i] = option(Tree[j, i-1].S * d, Tree[j, i-1].K,
                              Tree[j, i-1].t)
        Tree[j+1, i].get_payout()
    for i in range(N):
        Price[i, N-1] = Tree[i, N-1].payout
    for i in range(N-2, -1, -1):
        for j in range(i+1):
            Price[j, i] = max(Tree[j, i].payout, np.exp(-r*h)*(pu * Price[j,
                                                                          i+1]
                                                               + pd *
                                                               Price[j+1,
                                                                     i+1]))
    print(Price)


if __name__ == '__main__':
    main()
