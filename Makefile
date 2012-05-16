CXXFLAGS=-Wall -O3

all: time Time.class

time: time.cpp

Time.class: Time.java
	javac Time.java

run: all
	@python results.py ./time
	@python results.py java Time
	@python results.py python time.py
	@python results.py node time.js

clean:
	@rm -vf Time.class ./time
