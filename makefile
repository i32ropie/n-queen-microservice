CPPFLAGS = -g -std=c++11 -c -DNDEBUG
OBJECT = main.o
BIN = main

all: $(BIN)

main: $(OBJECT)
	g++ -o $(BIN) $(OBJECT)

main.o: *.cpp *.hpp
	g++ $(CPPFLAGS) main.cpp

clean:
	@rm -rf $(OBJECT) $(BIN) soluciones/*
