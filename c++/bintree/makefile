ifeq ($(OS), Windows_NT)
	INCLUDES := includes\\
	BUILD := build\\
	BIN := bin\\
	EXECUTABLE := $(BIN)bintree.exe
	SOURCE := source\\
	DELETE := del
else
	INCLUDES := includes/
	BUILD := build/
	BIN := bin/
	EXECUTABLE := $(BIN)bintree
	SOURCE := source/
	DELETE := rm
endif

CPP := g++
#CPPFLAGS := -std=c++17 -Wall -Wextra -Wpedantic -pedantic-errors -Werror -g
CPPFLAGS := -std=c++17 -Wall -Wextra -g

all: $(EXECUTABLE)

$(EXECUTABLE): $(BUILD)main.o $(BUILD)bintree.o
	$(CPP) $(CPPFLAGS) $(BUILD)main.o $(BUILD)bintree.o -o $(EXECUTABLE)

$(BUILD)main.o: $(SOURCE)main.cpp
	$(CPP) $(CPPFLAGS) -c $(SOURCE)main.cpp -I$(INCLUDES) -o $(BUILD)main.o

$(BUILD)bintree.o: $(SOURCE)bintree.cpp
	$(CPP) $(CPPFLAGS) -c $(SOURCE)bintree.cpp -I$(INCLUDES) -o $(BUILD)bintree.o

clean:
	-$(DELETE) $(EXECUTABLE) $(BUILD)*