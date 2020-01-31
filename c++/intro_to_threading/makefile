ifeq ($(OS), Windows_NT)
	INCLUDES := includes\\
	BUILD := build\\
	BIN := bin\\
	EXECUTABLE := $(BIN)classic_rpg.exe
	SOURCE := source\\
	DELETE := del
else
	INCLUDES := includes/
	BUILD := build/
	BIN := bin/
	EXECUTABLE := $(BIN)classic_rpg
	SOURCE := source/
	DELETE := rm
endif


CPP := g++
#CPPFLAGS := -std=c++17 -Wall -Wextra -Wpedantic -pedantic-errors -Werror -g
CPPFLAGS := -std=c++17 -Wall -Wextra -g

all: $(EXECUTABLE)

$(EXECUTABLE): $(BUILD)main.o $(BUILD)Fireball.o $(BUILD) $(BIN)
	$(CPP) $(CPPFLAGS) $(BUILD)main.o $(BUILD)Fireball.o -o $(EXECUTABLE)

$(BUILD)main.o: $(SOURCE)main.cpp $(BUILD)
	$(CPP) $(CPPFLAGS) -c $(SOURCE)main.cpp -I$(INCLUDES) -o $(BUILD)main.o

$(BUILD)Fireball.o: $(SOURCE)Fireball.cpp $(BUILD)
	$(CPP) $(CPPFLAGS) -c $(SOURCE)Fireball.cpp -I$(INCLUDES) -o $(BUILD)Fireball.o

$(BUILD):
	mkdir $(BUILD)

$(BIN):
	mkdir $(BIN)
clean:
	-$(DELETE) $(EXECUTABLE) $(BUILD)*