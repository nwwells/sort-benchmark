import re
import subprocess
import sys
import time

from stats import running_stat


start = time.time()
program = ['./xtime']
program.extend(sys.argv[1:])
p = subprocess.check_output(program, stderr=subprocess.STDOUT)
total_time = time.time() - start

number_pattern = re.compile(r'(\d+)')
memory_pattern = re.compile(r'(\d+kB)')

rs = running_stat()
output = p.strip().split('\n')
for i in output[:-1]:
    number = number_pattern.search(i)
    if number is not None:
        number = number.group()
        rs.push(float(number))
rams = memory_pattern.search(output[-1]).group(1)
print('{name:25s} '
        '   total time: {total:10.2f}s'
        '   ram: {ram:>15}'
        '   per loop:  mean: {rs.mean:15.1f}'
        '   stddev: {rs.stddev:15.1f}'
        '   min: {rs.min:10}   max: {rs.max:15}'
        ''.format(**{
    'name': ' '.join(program[1:]),
    'total': total_time,
    'rs': rs,
    'ram': rams,
}))
