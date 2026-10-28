# Makefile del Sistema bancario (FPOO). No hace falta editarlo.
#
#   make        compila todo lo que haya en src/ y src/modelo/ (ejecutable: banco)
#   make run    compila y ejecuta
#   make clean  borra lo compilado
#   make entrega arma el .zip para subir al Campus (entrega-<usuario>-sistema-bancario.zip)
#
# Funciona en Linux, macOS y Windows (con MinGW-w64/MSYS2 y make). Solo usa g++.

CXX      = g++
CXXFLAGS = -std=c++17 -Wall -Wextra -g -Isrc -Isrc/modelo -MMD -MP

ifeq ($(OS),Windows_NT)
EXE = .exe
else
EXE =
endif

ifeq ($(wildcard build/.),)
$(shell mkdir build)
endif

vpath %.cpp src src/modelo

SRC  = $(wildcard src/*.cpp) $(wildcard src/modelo/*.cpp)
OBJ  = $(addprefix build/, $(notdir $(SRC:.cpp=.o)))
BIN  = banco$(EXE)

all: $(BIN)

$(BIN): $(OBJ)
	$(CXX) $(CXXFLAGS) $^ -o $@

build/%.o: %.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

run: $(BIN)
	./$(BIN)

clean:
ifeq ($(OS),Windows_NT)
	-del /Q build\*.o build\*.d $(BIN) 2>nul
else
	rm -f build/*.o build/*.d $(BIN)
endif

entrega:
	@python3 herramientas/entrega.py || python herramientas/entrega.py

-include $(OBJ:.o=.d)

.PHONY: all run clean entrega
