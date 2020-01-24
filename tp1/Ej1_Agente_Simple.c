//Alumnos: Casado-Fiochetti-Perellón
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include <unistd.h>
//Ejercicio 1: Agente Reactivo Simple 

int mover(int direc, int pos);

int main(int argc, char const *argv[])
{
//Estados
	int limpiar = 0 ,sucio = 1, pos = 0, direc;
//Char Baldosa
	char estBaldosa[4] = {1, 1, 1, 1};
	
	direc = 1;

	while(1){
		
		if (estBaldosa[pos] == sucio){

			estBaldosa[pos] = limpiar;
			printf("Baldosa limpia %d\n", estBaldosa[pos]);
			sleep(1);

		}else{
			if (pos == 4){
				direc = -1;
				sleep(1);
			}
			if (pos == 0){
				direc = 1;
				sleep(1);
			}
			pos = mover(direc, pos);
			
		}
	}

	return 0;
	
}

int mover(int direc, int pos){

	if (direc == 1){
		pos++;
		printf("Me movi a la derecha %d \n", pos);
		sleep(1);
	}
	if(direc == -1){
		pos--;
		printf("Me movi a la izquierda %d \n", pos);
		sleep(1);
	}
	return pos;
}

