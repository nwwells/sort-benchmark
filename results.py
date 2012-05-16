import re
import subprocess
import sys
import time

from stats import running_stat


start = time.time()
program = sys.argv[1:]
p = subprocess.check_output(program)
number_pattern = re.compile(r'(\d+)')
total_time = time.time() - start

rs = running_stat()
c = 0
for i in p.split('\n'):
    number = number_pattern.search(i)
    if number is not None:
        number = number.group()
        rs.push(float(number))
    c += 1
print('{0} {1} total time: {2}'.format(program, rs, total_time))
