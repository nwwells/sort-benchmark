CXXFLAGS=-Wall -O3

all: time Time.class

time: time.cpp

Time.class: Time.java
	javac Time.java

run:
	@python results.py ./time
	@python results.py java Time
	@python results.py python time.py

clean:
	@rm -vf Time.class ./time
