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

$(EXECUTABLE): $(BUILD)main.o $(BUILD)Fireball.o
	$(CPP) $(CPPFLAGS) $(BUILD)main.o $(BUILD)Fireball.o -o $(EXECUTABLE)

$(BUILD)main.o: $(SOURCE)main.cpp
	$(CPP) $(CPPFLAGS) -c $(SOURCE)main.cpp -I$(INCLUDES) -o $(BUILD)main.o

$(BUILD)Fireball.o: $(SOURCE)Fireball.cpp
	$(CPP) $(CPPFLAGS) -c $(SOURCE)Fireball.cpp -I$(INCLUDES) -o $(BUILD)Fireball.o

clean:
	-$(DELETE) $(EXECUTABLE) $(BUILD)*