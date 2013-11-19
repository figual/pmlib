#include <stdio.h>
#include "pmlib.h"

int main (int argc, char *argv[])
{
	server_t server;
	counter_t contador;
	line_t lines;	
        int set= -1, frequency= 0, aggregate= 1;

	pm_set_server("150.128.83.55", 6526, &server);
	pm_set_lines("7-8", &lines);
	//LINE_SET_ALL(&lines);
	pm_create_counter("PDU", lines, !aggregate, frequency, server, &contador);

	pm_continue_counter(&contador);
       	sleep(5);
	pm_stop_counter(&contador);

	pm_get_counter_data(&contador);

//	set= 0;
	pm_print_data_text("out.txt", contador, lines, set);
	pm_print_data_csv("out.csv", contador, lines, set);
	pm_print_data_paraver("out.prv", contador, lines, set, "us");
	pm_print_data_stdout(contador, lines, 0);

	pm_finalize_counter(&contador);	
	return 0;
}
