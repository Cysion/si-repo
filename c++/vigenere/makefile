ifeq ($(OS), Windows_NT)
	INCLUDES := includes\\
	BUILD := build\\
	BIN := bin\\
	EXECUTABLE := $(BIN)vigenere.exe
	SOURCE := source\\
	DELETE := del
else
	INCLUDES := includes/
	BUILD := build/
	BIN := bin/
	EXECUTABLE := $(BIN)vigenere
	SOURCE := source/
	DELETE := rm
endif

CPP := g++
CPPFLAGS := -std=c++17 -Wall -Wextra -Wpedantic -pedantic-errors -Werror -g
#CPPFLAGS := -std=c++17 -Wall -Wextra -g

all: $(EXECUTABLE)

$(EXECUTABLE): $(BUILD)main.o $(BUILD)vigenere.o
	$(CPP) $(CPPFLAGS) $(BUILD)main.o $(BUILD)vigenere.o -o $(EXECUTABLE)

$(BUILD)main.o: $(SOURCE)main.cpp
	$(CPP) $(CPPFLAGS) -c $(SOURCE)main.cpp -I$(INCLUDES) -o $(BUILD)main.o

$(BUILD)vigenere.o: $(SOURCE)vigenere.cpp
	$(CPP) $(CPPFLAGS) -c $(SOURCE)vigenere.cpp -I$(INCLUDES) -o $(BUILD)vigenere.o

clean:
	-$(DELETE) $(EXECUTABLE) $(BUILD)*