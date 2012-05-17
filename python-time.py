import random
import time


for i in xrange(1000):
    array = [random.randint(1, 100000) for i in xrange(1000000)]
    start = time.time() * 1000000
    array.sort()
    end = time.time() * 1000000
    print "Elapsed time: %i microseconds" % (end - start)
