# Compiler and flags
CC = gcc
CFLAGS = -Wall -Wextra -std=c11

# Files
SRC = main.c life.c
OBJ = $(SRC:.c=.o)
TARGET = conway

# Default target — build executable
all: $(TARGET)

$(TARGET): $(OBJ)
	$(CC) $(CFLAGS) -o $(TARGET) $(OBJ)

# Compile .c files into .o files
%.o: %.c life.h
	$(CC) $(CFLAGS) -c $< -o $@

# Install target — copies executable to ~/bin (creates dir if needed)
install: $(TARGET)
	mkdir -p ~/bin
	cp $(TARGET) ~/bin/
	@echo "Installed $(TARGET) to ~/bin"

# Clean target — removes object files and the executable
clean:
	rm -f $(OBJ) $(TARGET)
	@echo "Cleaned up build files"
