CXXFLAGS=-Wall -O3

all: time JavaTime.class gotime

time: time.cpp

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

clean:
	@rm -vf JavaTime.class time gotime
