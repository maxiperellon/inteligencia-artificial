//Alumnos: Casado-Fiochetti-Perellón
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include <unistd.h>
//Ejercicio 2: Agente Basado en Modelo

int mover(int direc, int pos);

int main(int argc, char const *argv[])
{
//Estados
	int limpio = 0 ,sucio = 1;
//Posicion y dirección 
	int pos = 0, direc;
//Char baldosas
	char estBaldosa[4] = {0, 1, 1, 1}, desc[4] = {2, 2, 2, 2};

	direc = 1;

	while(1){
	//Comienza con un estado desconocido de la limpieza
		if (desc[pos] == 2){
	
			if (estBaldosa[pos] == sucio){
			//Si esta sucia limpia
				estBaldosa[pos] = limpio;
				printf("Baldosa limpia %d\n", estBaldosa[pos]);
			//De desconocido el estado pasa a limpio
				desc[pos] = limpio;
				sleep(1);
			}else{
				printf("La baldosa ya estaba limpia %d\n", estBaldosa[pos]);
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

