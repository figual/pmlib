#!/usr/bin/make -f

all:
	@echo "Usage: make doc"
	@echo
	@echo "Runs doxygen Doxyfile and compiles the refman.pdf"


doc:
	doxygen Doxyfile
	cd latex; make
