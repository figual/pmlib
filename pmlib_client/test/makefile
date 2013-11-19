CC=gcc

LIBS  = ../pmlib.a -I..
CFLAGS = -Wall 

EXE = ej0.x    \
      ej1.x    \
      ej2.x    \
      ej3.x    \
      ej4.x    

all: $(EXE)

%.x: %.c
	gcc $< $(CFLAGS) $(LIBS) -o $@

clean:
	rm -rf *.x
