Sort Benchmark
==============
I got tired of not having a good retort for how much faster C/C++ 
is than everything else in the world, so I did a very simple benchmark 
with the standard sort implementation in a number of languages.

Interesting results
-------------------

<table>
<tr><th>C++       </th><td>4.2-5.7ms </td><td>28 LoC</td><td>1.5 hours to dev</td></tr>
<tr><th>Java      </th><td>0.9-9.0ms </td><td>19 LoC</td><td>10 min to dev</td></tr>
<tr><th>Groovy    </th><td>0.9-23.7ms</td><td>11 LoC</td><td>10 min to dev</td></tr>
<tr><th>Python    </th><td>4.2-5.6ms </td><td> 8 LoC</td><td>10 min to dev</td></tr>
<tr><th>Javascript</th><td>6-8ms     </td><td> 9 LoC</td><td>10 min to dev</td></tr>
</table>

Notes
-----
This was my first time coding in C++ which affects LoC and dev time. I 
think performance will remain the same even with expert devs, since I'm 
using the standard sort function

Better Python and JS devs could probably bring the dev time down to 5 
minutes

Java and Groovy both had a higher initial runs (8ms and 18 ms, 
respectively), but after the 3rd or 4th loop consistently delivered sub-
millisecond performance. I assume this is because of the initial class 
access time and setting up global constants.

Thoughts
--------
C++ is not faster than Java or Groovy.

It's not even consistently faster than Python or JS.

It's about a whole order of magnitude slower to develop in than any 
modern language (unless you've already climbed the learning curve)

It's 3 times more verbose than modern scripting languages

Java and/or the JVM are wicked fast

Pointers suck

Running
-------
Just compile (or not) and run. You'll get 100 lines of "Time elapsed" 
messages for each program

#### Java Compile & Run
    javac Time.java
    java Time

#### C++ Compile & Run
    g++ time.cpp
    ./a.out //not sure if this is platform specific?

#### Others
    groovy time.groovy
    python pyTime.py
    node time.js

Going Forward
-------------
I invite my C++ and Python friends to fork my github project and 
improve the performance.

I further invite my Perl and Ruby friends to fork and implement the 
benchmark in your respective languages.

All other languages are not invited (just kidding)

I might make a build script that will compile and run all the progams
and generate a report.