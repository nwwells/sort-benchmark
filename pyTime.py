import random
import time
array = [random.randint(1,100000) for i in xrange(10000)]
start = time.time() * 1000000
array.sort()
end = time.time() * 1000000
print "Elapsed time: %i microseconds" % (end - start)
