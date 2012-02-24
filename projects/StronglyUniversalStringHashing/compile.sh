gcc -O3 -funroll-loops -mno-sse2 -o hashfunctionsrealnosse hashfunctionsreal.c
gcc -O3 -funroll-loops -mno-sse2 -o hashfunctions32nosse hashfunctions32.c
gcc -O3 -funroll-loops -o hashfunctionsreal hashfunctionsreal.c
gcc -O3 -funroll-loops -o hashfunctions32 hashfunctions32.c
