CC=gcc

CC_OPTIONS=-Wall 
#-DLOG 

OBJ= pm_set_server.o \
     pm_start_counter.o \
     pm_stop_counter.o \
     pm_get_counter_data.o \
     pm_get_and_print_data_paraver.o \
     pm_finalize_counter.o \
     pm_continue_counter.o \
     pm_create_counter.o \
     pm_get_device_info.o \
     pm_get_devices.o \
     pm_set_lines.o \
     pm_print_data_text.o \
     pm_print_data_csv.o \
     pm_print_data_paraver.o \
     pm_print_data_stdout.o \
     pm_fprint_counter_info.o 
LIB=pmlib.a

INSTALL=/usr/local/pmlib

all: $(LIB)

$(LIB):$(OBJ)
	ar -cr $(LIB) $(OBJ)
	ranlib $(LIB)

.c.o:
	$(CC) $(CC_OPTIONS) -c $<

install: all
	install -m 644 pmlib.a $(INSTALL)/lib/
	install -m 644 line.h pmlib.h $(INSTALL)/include/

clean:
	rm -rf $(OBJ) $(LIB)
