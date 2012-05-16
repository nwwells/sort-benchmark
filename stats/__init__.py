import math

class running_stat(object):
    def __init__(self):
        self.n = 0
        self.M_old = 0.0
        self.S_old = 0.0
        self.max = -float('inf')
        self.min = float('inf')

    def push(self, x):
        self.n += 1

        self.M_new = self.M_old + (x - self.M_old) / self.n
        self.S_new = self.S_old + (x - self.M_old) * (x - self.M_new)

        self.M_old = self.M_new
        self.S_old = self.S_new

        if x < self.min:
            self.min = x
        if x > self.max:
            self.max = x

    @property
    def mean(self):
        r = 0.0
        if self.n > 0:
            r = self.M_new
        return r

    def _variance(self):
        r = 0.0
        if self.n > 1:
            r = self.S_new / (self.n)
        return r

    @property
    def stddev(self):
        return math.sqrt(self._variance())

    def __str__(self):
        return 'min: {0.min:.3f}, avg: {0.mean:.3f},' \
               ' max: {0.max:.3f}, stddev: {0.stddev:.3f}'.format(self)
