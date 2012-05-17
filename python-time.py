import numpy as np
import time


for i in xrange(1000):
    a = np.random.random((1000000))
    start = time.time() * 1000000
    a.sort()
    end = time.time() * 1000000
    print "Elapsed time: %i microseconds" % (end - start)
