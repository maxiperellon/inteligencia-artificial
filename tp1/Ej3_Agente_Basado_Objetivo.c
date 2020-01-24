//Alumnos: Casado-Fiochetti-Perellón
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include <unistd.h>
//Ejercicio 3: Agente Basado en Objetivos

int mover(int direc, int pos);

int main(int argc, char const *argv[])
{
//Estados
	int limpio = 0 ,sucio = 1, cont = 0;
//Posicion y dirección 
	int pos = 0, direc;
//Char baldosas
	char estBaldosa[4] = {0, 0, 1, 1}, desc[4] = {2, 2, 2, 2};

	direc = 1;

	while(cont != 4){
	//Comienza con un estado desconocido de la limpieza
		if (desc[pos] == 2){
	
			if (estBaldosa[pos] == sucio){
			//Si esta sucia limpia
				estBaldosa[pos] = limpio;
				printf("Baldosa limpia %d\n", estBaldosa[pos]);
			//De desconocido el estado pasa a limpio
				desc[pos] = limpio;
				cont++;
				sleep(1);
			}else{
				printf("La baldosa ya estaba limpia %d\n", estBaldosa[pos]);
				cont++;
				desc[pos] = limpio;
			}
			
		}else{
			if (pos == 3){
				direc = -1;
			}
			if (pos == 0){
				direc = 1;
			}
			pos = mover(direc, pos);
		}
	}
	printf("Todas las baldosas se encuentran limpias.\n Adios!\n");
	return 0;
	
	exit(1);
	
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

