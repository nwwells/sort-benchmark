CXXFLAGS=-Wall -O3
CFLAGS=-Wall -std=c99 -O3

all: time JavaTime.class gotime c-time

time: time.cpp

c-time: c-time.c

gotime: time.go
	go build -o gotime time.go

JavaTime.class: JavaTime.java
	javac JavaTime.java

run: all
	@python results.py ./time
	@python results.py java JavaTime
	@python results.py python python-time.py
	@python results.py node node-time.js
	@python results.py groovy groovyTime.groovy
	@python results.py ./gotime
	@python results.py go run time.go
	@python results.py ./c-time
	@python results.py perl perl-time.pl

clean:
	@rm -vf JavaTime.class time gotime c-time
