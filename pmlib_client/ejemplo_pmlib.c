#include <stdio.h>
#include "pmlib.h"
#include <sys/time.h>
#include <stdlib.h>
int main (int argc, char *argv[])
{
	server_t servidor;
	counter_t contador;
	counter_t contador2;
	line_t lineas;
	device_t disp;
	char **lista;
	int i, num_devices;
	char name[20];
	struct timeval start, end;

        int frequency= 0;
        int aggregate= 1;

	LINE_SET_ZERO(&lineas);
	LINE_SET_ALL(&lineas);
	
	for (i=0; i<128;i++){
		if (LINE_ISSET(i, &lineas)) printf("1");
		else printf("0");
	}
        printf("\n");

        printf("Empieza pm_set_server\n");
	pm_set_server("150.128.83.55", 6526, &servidor);
	
	
	printf("Empieza pm_get_devices\n");
	pm_get_devices(servidor, &lista, &num_devices);  

	printf("Number of devices: %d\n", num_devices);      
	for(i=0; i<num_devices; i++)
		printf("%s\n", lista[i]);

	printf("Empieza pm_get_device_info\n");
	pm_get_device_info(servidor, lista[0], &disp);
	printf("%s\n", disp.name);
	printf("%d\n", disp.max_frecuency);
	printf("%d\n", disp.n_lines);

	printf("Empieza pm_create_counter\n");
	pm_create_counter("DC2Meter1", lineas, !aggregate, frequency, servidor, &contador);

	printf("Empieza pm_start_counter\n");
	pm_start_counter(&contador);
	sleep(1);
	printf("Empieza pm_stop_counter\n");
	pm_stop_counter(&contador);

		
	for(i=0; i<3; i++){
	  printf("Empieza pm_continue_counter\n");
	  pm_continue_counter(&contador);

	  sleep(2);
	
	  printf("Empieza pm_stop_counter\n");
	  pm_stop_counter(&contador);
	 
	}
        

	pm_get_counter_data(&contador);

        pm_print_data_stdout(contador, lineas, -1);
	pm_print_data_text("out_cnt1.txt", contador, lineas, -1);
	pm_print_data_csv("out_cnt1.csv", contador, lineas, -1);
	pm_print_data_paraver("out_cnt1.prv", contador, lineas, -1, "us");
	
	printf("Empieza pm_finalize_counter\n");
	pm_finalize_counter(&contador);	 //Siempre es la última operación sobre un contador
	

	pm_create_counter("DC2Meter1", lineas, aggregate, frequency, servidor, &contador2);
	printf("Empieza pm_start_counter2\n");
	pm_start_counter(&contador2);	
	sleep(5);	
	printf("Empieza pm_stop_counter2\n");	
	pm_stop_counter(&contador2);

	printf("Empieza pm_continue_counter2\n");
	pm_continue_counter(&contador2);
        sleep(10);
	printf("Empieza pm_stop_counter2\n");
	pm_stop_counter(&contador2);

	pm_get_counter_data(&contador2);

        LINE_CLR(23,  &lineas); //Pone a 0 la línea 23, no se obtendrán sus resultados en la llamada a pm_print_data.
	pm_print_data_text("out_cnt2.txt",contador2, lineas, 0);
	
        printf("Empieza pm_finalize_counter2\n");
	pm_finalize_counter(&contador2);	


	return 0;
}
