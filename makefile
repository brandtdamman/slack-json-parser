# Designated compiler
CC		= gcc

# Flags
CFLAGS	= -pthread -Wall

# Executable name
TARGET	= slackjp

# Additional code files
SUPPORT	= commands.c

# Compilation
$(TARGET): $(TARGET).c $(SUPPORT)
	$(CC) $(CFLAGS) -o $(TARGET) $(TARGET).c $(SUPPORT)