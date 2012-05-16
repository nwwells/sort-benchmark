CXXFLAGS=-Wall -O3

all: time JavaTime.class

time: time.cpp

JavaTime.class: JavaTime.java
	javac JavaTime.java

run: all
	@python results.py ./time
	@python results.py java JavaTime
	@python results.py python python-time.py
	@python results.py node node-time.js
	@python results.py groovy groovyTime.groovy

clean:
	@rm -vf JavaTime.class ./time
